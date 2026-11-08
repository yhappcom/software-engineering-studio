import sqlite3,tempfile,pathlib,hmac,hashlib,json
K=b'public-demo-key'; checks=[]
def check(name,actual,expected=True):
 checks.append((name,actual==expected)); assert actual==expected,(name,actual)
def mac(d):return hmac.new(K,json.dumps(d,sort_keys=True).encode(),hashlib.sha256).hexdigest()
with tempfile.TemporaryDirectory() as t:
 p=pathlib.Path(t); stream=p/'stream.sqlite'; auth=p/'authority.sqlite'; backup=p/'snapshot.sqlite'
 s=sqlite3.connect(stream); a=sqlite3.connect(auth)
 s.execute('create table events(seq integer primary key,payload text)');s.executemany('insert into events values(?,?)',[(1,'old1'),(2,'old2')]);s.commit()
 a.execute('create table authority(stream text primary key,epoch integer not null)');a.execute('insert into authority values(?,?)',('ownerA',7));a.commit()
 def witness(epoch):
  d={'stream':'ownerA','epoch':epoch,'cursor':2};return d,mac(d)
 old,signature=witness(7)
 s.backup(sqlite3.connect(backup))
 a.execute('update authority set epoch=8 where stream=?',('ownerA',));a.commit()
 s.execute('update events set payload=? where seq=2',('new2',));s.commit()
 s.close();s=sqlite3.connect(stream);s.execute('delete from events');s.commit();src=sqlite3.connect(backup);src.backup(s);src.close()
 check('restored_payload',s.execute('select payload from events where seq=2').fetchone()[0]=='old2')
 check('old_mac_cryptographically_valid',mac(old)==signature)
 check('external_epoch_rejects_replay',old['epoch']!=a.execute('select epoch from authority').fetchone()[0])
 fresh,fs=witness(8);check('new_epoch_accepted',fresh['epoch']==a.execute('select epoch from authority').fetchone()[0] and mac(fresh)==fs)
 # Negative: external authority also restored / reset (bad implementation)
 a.execute('update authority set epoch=7');a.commit()
 check('authority_rollback_replays_old_token',old['epoch']==a.execute('select epoch from authority').fetchone()[0] and mac(old)==signature)
 # Negative: metadata epoch monotonic but event contents mutate without epoch increment
 a.execute('update authority set epoch=8');a.commit()
 s.execute('update events set payload=? where seq=2',('forged2',));s.commit()
 check('epoch_only_does_not_bind_page_contents',fresh['epoch']==a.execute('select epoch from authority').fetchone()[0] and mac(fresh)==fs and s.execute('select payload from events where seq=2').fetchone()[0]=='forged2')
 s.close();a.close()
print('D006_EXTERNAL_AUTHORITY',sum(x[1] for x in checks),'/',len(checks),'sqlite',sqlite3.sqlite_version)
for n,ok in checks:print(n,'PASS' if ok else 'FAIL')
