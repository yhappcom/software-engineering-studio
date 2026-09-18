#!/usr/bin/env python3
"""Bounded Linux/SQLite ENOSPC injection at libc pwrite boundary.

Requires: Linux /proc, gcc, Python sqlite3, LD_PRELOAD support.
This is deliberate syscall fault injection, NOT a physically full filesystem/device.
"""
from pathlib import Path
import os, subprocess, tempfile, textwrap, sqlite3

SHIM = r'''
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
static int target(int fd){
  char link[64], path[512];
  snprintf(link,sizeof link,"/proc/self/fd/%d",fd);
  ssize_t n=readlink(link,path,sizeof(path)-1); if(n<0)return 0;
  path[n]=0; const char *needle=getenv("FAULT_PATH");
  return needle && strstr(path,needle);
}
ssize_t pwrite64(int fd,const void*b,size_t c,off64_t o){
  static ssize_t(*real)(int,const void*,size_t,off64_t);
  if(!real) real=dlsym(RTLD_NEXT,"pwrite64");
  if(target(fd)){errno=ENOSPC; return -1;}
  return real(fd,b,c,o);
}
ssize_t pwrite(int fd,const void*b,size_t c,off_t o){
  static ssize_t(*real)(int,const void*,size_t,off_t);
  if(!real) real=dlsym(RTLD_NEXT,"pwrite");
  if(target(fd)){errno=ENOSPC; return -1;}
  return real(fd,b,c,o);
}
'''
CHILD = r'''
import sqlite3,sys
p=sys.argv[1]
c=sqlite3.connect(p)
try:
    c.execute("insert into ledger(v) values (200)")
    c.commit()
    print("UNEXPECTED_COMMIT")
except sqlite3.OperationalError as e:
    print("ERROR", e.sqlite_errorcode, e.sqlite_errorname, str(e))
    try: c.rollback()
    except sqlite3.Error: pass
'''

def main():
    with tempfile.TemporaryDirectory() as td:
        d=Path(td); db=d/'iofault.db'; shim=d/'fault.so'; child=d/'child.py'
        c=sqlite3.connect(db)
        c.execute('create table ledger(v integer not null)')
        c.execute('insert into ledger values (100)')
        c.commit(); c.close()
        src=d/'fault.c'; src.write_text(SHIM); child.write_text(CHILD)
        subprocess.run(['gcc','-shared','-fPIC','-O2','-o',str(shim),str(src),'-ldl'],check=True)
        env=os.environ.copy(); env['LD_PRELOAD']=str(shim); env['FAULT_PATH']=db.name
        r=subprocess.run([os.sys.executable,str(child),str(db)],env=env,text=True,capture_output=True,check=True)
        print(r.stdout.strip())
        c=sqlite3.connect(db)
        rows=c.execute('select v from ledger order by rowid').fetchall()
        integrity=c.execute('pragma integrity_check').fetchone()[0]
        print('ROWS',rows); print('INTEGRITY',integrity)
        assert 'ERROR 13 SQLITE_FULL' in r.stdout
        assert rows == [(100,)]
        assert integrity == 'ok'

if __name__ == '__main__': main()
