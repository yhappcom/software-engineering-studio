import sqlite3,tempfile,os,threading,hashlib
from pathlib import Path
p=Path(tempfile.mkdtemp()); a=p/'authority.db'; e=p/'events.db'
def connect(f):
 c=sqlite3.connect(f,timeout=3,isolation_level=None);c.execute('PRAGMA journal_mode=WAL');return c
ca=connect(a);ce=connect(e)
ca.execute('CREATE TABLE state(epoch INTEGER, phase TEXT)');ca.execute("INSERT INTO state VALUES(1,'READY')")
ce.execute('CREATE TABLE events(epoch INTEGER, value TEXT)');ce.execute("INSERT INTO events VALUES(1,'old')")
checks=[]
def check(name,ok): checks.append((name,ok));assert ok,name
# Deliberately non-atomic split reads: stale READY authority + fresh events
old=ca.execute('SELECT epoch,phase FROM state').fetchone()
ca.execute("UPDATE state SET epoch=2,phase='PREPARING'")
ce.execute("DELETE FROM events");ce.execute("INSERT INTO events VALUES(2,'new')")
new=ce.execute('SELECT epoch,value FROM events').fetchone()
check('unsafe_stale_ready_mixed_read',old==(1,'READY') and new==(2,'new'))
check('epoch_check_rejects_mixed',old[0]!=new[0])
# stale READY with ABA event replacement, epoch unchanged: epoch-only validation fails
ca.execute("UPDATE state SET epoch=1,phase='READY'")
ce.execute("UPDATE events SET epoch=1,value='altered'")
check('epoch_only_aba_false_accept',ca.execute('SELECT epoch,phase FROM state').fetchone()==(1,'READY') and ce.execute('SELECT epoch FROM events').fetchone()[0]==1)
# fail-closed reader with second authority read; concurrent switch between reads
ca.execute("UPDATE state SET epoch=2,phase='PREPARING'")
check('preparing_reject',ca.execute('SELECT phase FROM state').fetchone()[0]!='READY')
ce.execute("UPDATE events SET epoch=2,value='new'")
ca.execute("UPDATE state SET phase='READY'")
check('ready_accept',ca.execute('SELECT epoch,phase FROM state').fetchone()==(2,'READY') and ce.execute('SELECT epoch FROM events').fetchone()[0]==2)
# Interleaving: old ready read, switch to new ready, new event read, reread detects epoch change
ca.execute("UPDATE state SET epoch=1,phase='READY'");ce.execute("UPDATE events SET epoch=1,value='old'")
first=ca.execute('SELECT epoch,phase FROM state').fetchone()
ca.execute("UPDATE state SET epoch=2,phase='PREPARING'");ce.execute("UPDATE events SET epoch=2,value='new'");ca.execute("UPDATE state SET phase='READY'")
second=ca.execute('SELECT epoch,phase FROM state').fetchone()
check('double_read_rejects_epoch_switch',first!=second)
# ABA rollback both files between two reads defeats double-read
ca.execute("UPDATE state SET epoch=1,phase='READY'");ce.execute("UPDATE events SET epoch=1,value='altered'")
third=ca.execute('SELECT epoch,phase FROM state').fetchone()
check('double_read_aba_false_accept',first==third)
# Real simultaneous connection visibility: writer commits PREPARING while reader holds WAL snapshot
reader=connect(a);writer=connect(a)
reader.execute('BEGIN'); before=reader.execute('SELECT epoch,phase FROM state').fetchone()
writer.execute("UPDATE state SET epoch=3,phase='PREPARING'")
during=reader.execute('SELECT epoch,phase FROM state').fetchone()
reader.execute('COMMIT'); after=reader.execute('SELECT epoch,phase FROM state').fetchone()
check('wal_snapshot_old_then_new',before==during and after==(3,'PREPARING'))
reader.close();writer.close();ca.close();ce.close()
print('D006_CONCURRENT_CUTOVER',len(checks),'/',len(checks),checks)
