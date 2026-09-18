#!/usr/bin/env python3
"""Linux publication-boundary fixture.
Builds an LD_PRELOAD shim that fails fsync() only for directory FDs.
Demonstrates that rename visibility can precede successful directory synchronization.
"""
import hashlib, os, pathlib, subprocess, tempfile, textwrap

SHIM = r'''
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <sys/stat.h>
#include <unistd.h>
typedef int (*fsync_fn)(int);
int fsync(int fd){
 static fsync_fn real_fsync=NULL;
 if(!real_fsync) real_fsync=(fsync_fn)dlsym(RTLD_NEXT,"fsync");
 struct stat st;
 if(fstat(fd,&st)==0 && S_ISDIR(st.st_mode)){ errno=EIO; return -1; }
 return real_fsync(fd);
}
'''
PUBLISHER = r'''
import hashlib, os, sys
root=sys.argv[1]
final=os.path.join(root,"published.bin")
candidate=os.path.join(root,"candidate.tmp")
payload=b"new-artifact-v2\n"*100
with open(candidate,"wb") as f:
    f.write(payload); f.flush(); os.fsync(f.fileno())
os.replace(candidate,final)
dirfd=os.open(root,os.O_RDONLY|os.O_DIRECTORY)
try: os.fsync(dirfd)
finally: os.close(dirfd)
print(hashlib.sha256(open(final,"rb").read()).hexdigest())
'''

def run(root, preload=None):
    env=os.environ.copy()
    if preload: env["LD_PRELOAD"]=preload
    return subprocess.run(["python3",str(root.parent/"publisher.py"),str(root)],env=env,text=True,capture_output=True)

with tempfile.TemporaryDirectory() as t:
    base=pathlib.Path(t)
    (base/"shim.c").write_text(SHIM)
    (base/"publisher.py").write_text(PUBLISHER)
    subprocess.run(["gcc","-shared","-fPIC","-o",str(base/"shim.so"),str(base/"shim.c"),"-ldl"],check=True)
    control=base/"control"; control.mkdir()
    c=run(control)
    assert c.returncode==0 and (control/"published.bin").exists()
    fault=base/"fault"; fault.mkdir()
    f=run(fault,str(base/"shim.so"))
    assert f.returncode!=0 and (fault/"published.bin").exists()
    assert "Input/output error" in f.stderr
    print("control=success")
    print("directory_fsync_fault=EIO")
    print("final_visible_after_failed_directory_fsync=true")
    print("fault_final_sha256="+hashlib.sha256((fault/"published.bin").read_bytes()).hexdigest())
