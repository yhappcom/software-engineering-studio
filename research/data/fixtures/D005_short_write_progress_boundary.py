#!/usr/bin/env python3
"""D005 bounded Linux/SQLite short-write progress fault fixture.

Compiles an LD_PRELOAD shim and compares one positive-progress short pwrite
with a zero-progress pwrite against a rollback-journal SQLite transaction.
"""
import os, sqlite3, subprocess, tempfile, json
from pathlib import Path

C = r'''#define _GNU_SOURCE
#include <dlfcn.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <limits.h>
static ssize_t (*rp64)(int,const void*,size_t,off64_t)=0;
static ssize_t (*rp)(int,const void*,size_t,off_t)=0;
static int fired=0;
static int target(int fd){char p[64],b[PATH_MAX];snprintf(p,sizeof p,"/proc/self/fd/%d",fd);ssize_t n=readlink(p,b,sizeof(b)-1);if(n<0)return 0;b[n]=0;const char*s=getenv("D005_TARGET");return s&&strstr(b,s);}
static size_t choose(size_t n){const char*m=getenv("D005_MODE");if(m&&strcmp(m,"zero")==0)return 0;return n>1?n/2:n;}
ssize_t pwrite64(int fd,const void*b,size_t n,off64_t o){if(!rp64)rp64=dlsym(RTLD_NEXT,"pwrite64");if(!fired&&target(fd)){fired=1;size_t k=choose(n);fprintf(stderr,"INJECT pwrite64 requested=%zu returned=%zu off=%lld\n",n,k,(long long)o);if(k==0)return 0;return rp64(fd,b,k,o);}return rp64(fd,b,n,o);}
ssize_t pwrite(int fd,const void*b,size_t n,off_t o){if(!rp)rp=dlsym(RTLD_NEXT,"pwrite");if(!fired&&target(fd)){fired=1;size_t k=choose(n);fprintf(stderr,"INJECT pwrite requested=%zu returned=%zu off=%lld\n",n,k,(long long)o);if(k==0)return 0;return rp(fd,b,k,o);}return rp(fd,b,n,o);}
'''
CHILD = r'''import sqlite3,sys
p=sys.argv[1]
c=sqlite3.connect(p);c.execute("pragma journal_mode=delete");c.execute("pragma synchronous=full")
try:
 c.execute("insert into ledger values(200)");c.commit();print("COMMIT_OK")
except Exception as e:
 print("ERROR",getattr(e,"sqlite_errorcode",None),getattr(e,"sqlite_errorname",None),str(e))
finally:c.close()
'''

def baseline(p):
    c=sqlite3.connect(p); c.execute('create table ledger(v integer not null)'); c.execute('insert into ledger values(100)'); c.commit(); c.close()

def oracle(p):
    c=sqlite3.connect(p); rows=[x[0] for x in c.execute('select v from ledger')]; integrity=c.execute('pragma integrity_check').fetchone()[0]; c.close(); return rows,integrity

def run(mode,root,so):
    p=root/f'{mode}.db'; baseline(p)
    env=os.environ.copy(); env.update(LD_PRELOAD=str(so),D005_TARGET=p.name,D005_MODE=mode)
    r=subprocess.run(['python3','-c',CHILD,str(p)],env=env,text=True,capture_output=True)
    rows,integrity=oracle(p)
    return dict(mode=mode,stdout=r.stdout.strip(),stderr=r.stderr.strip(),rows=rows,integrity=integrity)

with tempfile.TemporaryDirectory() as td:
    root=Path(td); src=root/'shim.c'; so=root/'shim.so'; src.write_text(C)
    subprocess.run(['gcc','-shared','-fPIC','-O2','-o',str(so),str(src),'-ldl'],check=True)
    out=[run('short',root,so),run('zero',root,so)]
    print(json.dumps(out,indent=2))
    assert out[0]['stdout']=='COMMIT_OK' and out[0]['rows']==[100,200] and out[0]['integrity']=='ok'
    assert 'SQLITE_FULL' in out[1]['stdout'] and out[1]['rows']==[100] and out[1]['integrity']=='ok'
