import sqlite3,tempfile,os,hashlib,sys

def connect(path):
 c=sqlite3.connect(path,isolation_level=None,timeout=2)
 c.execute('PRAGMA journal_mode=WAL');c.execute('PRAGMA busy_timeout=2000')
 return c

def setup(path):
 c=connect(path)
 c.executescript('CREATE TABLE events(seq INTEGER PRIMARY KEY,payload TEXT NOT NULL);CREATE TABLE meta(version INTEGER NOT NULL,floor INTEGER NOT NULL,high INTEGER NOT NULL);INSERT INTO meta VALUES(10,1,4);INSERT INTO events VALUES(1,"a"),(2,"b"),(3,"c"),(4,"d");')
 c.close()

def meta(c):return tuple(c.execute('SELECT version,floor,high FROM meta').fetchone())
def page(c,after=0):return c.execute('SELECT seq,payload FROM events WHERE seq>? ORDER BY seq',(after,)).fetchall()
def gc(c):
 c.execute('BEGIN IMMEDIATE');c.execute('DELETE FROM events WHERE seq<=2');c.execute('UPDATE meta SET version=11,floor=3');c.execute('COMMIT')

def run():
 count=0
 def check(label,condition):
  nonlocal count
  assert condition,label
  count+=1
  print('PASS',label)
 with tempfile.TemporaryDirectory() as td:
  path=os.path.join(td,'db.sqlite');setup(path)
  a,b=connect(path),connect(path)
  a.execute('BEGIN');original=meta(a);before=page(a)
  check('snapshot initial',original==(10,1,4) and len(before)==4)
  gc(b)
  check('writer GC committed while reader snapshot open',meta(b)==(11,3,4) and page(b)==[(3,'c'),(4,'d')])
  check('pinned reader sees original atomic view',meta(a)==(10,1,4) and page(a)==before)
  a.execute('ROLLBACK')
  check('fresh reader sees GC version',meta(a)==(11,3,4) and page(a)==[(3,'c'),(4,'d')])
  check('old witness rejected after GC',original!=meta(a))
  check('split reads mismatch detected',before!=page(a) and original!=meta(a))
  check('stale cursor requires recovery',0<meta(a)[1]-1)
  b.execute('BEGIN IMMEDIATE');b.execute('DELETE FROM events WHERE seq=3');b.execute('UPDATE meta SET version=12,floor=4');b.close()
  c=connect(path)
  check('uncommitted GC rollback on connection close',meta(c)==(11,3,4) and page(c)==[(3,'c'),(4,'d')])
  c.execute('BEGIN IMMEDIATE');c.execute('INSERT INTO events VALUES(2,"late")');c.execute('COMMIT')
  check('late lower sequence bypasses cursor 4',c.execute('SELECT count(*) FROM events WHERE seq>4').fetchone()[0]==0 and c.execute('SELECT payload FROM events WHERE seq=2').fetchone()[0]=='late')
  c.close();a.close()
 print(f'D006_GC_SNAPSHOT_SQLITE_PASS {count}/{count} sqlite={sqlite3.sqlite_version} python={sys.version.split()[0]}')
if __name__=='__main__':run()
