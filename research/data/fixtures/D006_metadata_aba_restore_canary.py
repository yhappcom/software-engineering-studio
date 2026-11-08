import sqlite3,tempfile,os,hmac,hashlib,json
KEY=b'public-synthetic-only'
def sign(meta):
    return hmac.new(KEY,json.dumps(meta,sort_keys=True,separators=(',',':')).encode(),hashlib.sha256).hexdigest()
def db(path):
    c=sqlite3.connect(path,isolation_level=None)
    c.execute('pragma journal_mode=wal')
    c.executescript('create table if not exists meta(k text primary key,v text not null); create table if not exists events(seq integer primary key,payload text not null);')
    return c
def put(c,meta,rows):
    c.execute('begin immediate')
    c.execute('delete from meta');c.execute('delete from events')
    c.executemany('insert into meta values(?,?)',[(k,str(v)) for k,v in meta.items()]);c.executemany('insert into events values(?,?)',rows)
    c.execute('commit')
def view(c):
    return {k:int(v) if k!='owner' else v for k,v in c.execute('select k,v from meta')}
def check(name,cond):
    assert cond,name
    print('PASS',name)
with tempfile.TemporaryDirectory() as t:
    path=os.path.join(t,'events.db');a=db(path);b=db(path)
    before={'owner':'A','generation':1,'version':10,'floor':1,'high':4,'incarnation':101}
    put(a,before,[(i,'old'+str(i)) for i in range(1,5)])
    token_old={k:v for k,v in before.items() if k!='incarnation'}
    mac_old=sign(token_old)
    check('initial_witness_matches',hmac.compare_digest(sign(token_old),mac_old))
    # Restore old metadata numbering with different data; independent writer B.
    after={**before,'incarnation':102}
    put(b,after,[(i,'new'+str(i)) for i in range(1,5)])
    check('reopened_rows_changed',a.execute('select payload from events where seq=2').fetchone()[0]=='new2')
    check('metadata_version_aba',all(view(a)[k]==v for k,v in token_old.items()))
    check('old_mac_still_valid',hmac.compare_digest(sign({k:view(a)[k] for k in token_old}),mac_old))
    check('old_page_not_current',a.execute('select payload from events where seq=2').fetchone()[0]!='old2')
    # Persistent incarnation checked and signed prevents old witness reacceptance.
    bound_old={**token_old,'incarnation':101};mac_bound=sign(bound_old)
    check('incarnation_blocks_old_witness',not hmac.compare_digest(sign(view(a)),mac_bound))
    bound_new=view(a);mac_new=sign(bound_new)
    check('new_witness_valid',hmac.compare_digest(sign(bound_new),mac_new))
    # Old witness may still verify after rollback of monotonic epoch to 101.
    put(b,before,[(i,'third'+str(i)) for i in range(1,5)])
    check('rollback_reopens_aba',hmac.compare_digest(sign(view(a)),mac_bound))
    check('rollback_data_changed',a.execute('select payload from events where seq=2').fetchone()[0]=='third2')
    a.close();b.close()
print('D006_ABA_PASS 9/9 sqlite='+sqlite3.sqlite_version)
