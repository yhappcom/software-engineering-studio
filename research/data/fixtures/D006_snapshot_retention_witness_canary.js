// D006 synthetic retention witness model; no real Firebase, keys or product data.
// Run: node research/data/fixtures/D006_snapshot_retention_witness_canary.js
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const key = Buffer.from('synthetic-only-not-a-real-server-key');
const stable = x => JSON.stringify(x);
const sign = p => crypto.createHmac('sha256',key).update(stable(p)).digest('hex');
const seal = p => ({p,mac:sign(p)});
function verify(w,ctx,view){
 if(!w || typeof w.mac!=='string'||!w.p) return 'REJECT';
 const expected=sign(w.p);
 if(!/^[a-f0-9]{64}$/.test(w.mac) || !crypto.timingSafeEqual(Buffer.from(w.mac,'hex'),Buffer.from(expected,'hex')))return 'REJECT';
 const p=w.p;
 if(p.owner!==ctx.owner||p.generation!==ctx.generation||p.cursor!==ctx.cursor)return 'REJECT';
 if(p.version!==view.version||p.floor!==view.floor||p.high!==view.high)return 'STALE_RETRY';
 if(p.cursor<p.floor-1)return 'RECOVERY_REQUIRED';
 if(p.high<p.cursor)return 'REJECT';
 return 'ACCEPT';
}
const ctx={owner:'A',generation:'g1',cursor:4};
const v1={version:10,floor:5,high:7};
const v2={version:11,floor:7,high:7};
const witness=seal({...ctx,...v1});
const cases=[
 ['valid snapshot',witness,ctx,v1,'ACCEPT'],
 ['GC after metadata',witness,ctx,v2,'STALE_RETRY'],
 ['forged true', {p:witness.p,mac:'true'},ctx,v1,'REJECT'],
 ['changed floor', {...witness,p:{...witness.p,floor:7}},ctx,v1,'REJECT'],
 ['wrong owner',witness,{...ctx,owner:'B'},v1,'REJECT'],
 ['wrong generation',witness,{...ctx,generation:'g2'},v1,'REJECT'],
 ['wrong cursor',witness,{...ctx,cursor:3},v1,'REJECT'],
 ['stale authenticated cursor',seal({...ctx,version:11,floor:7,high:7}),ctx,v2,'RECOVERY_REQUIRED'],
 ['malformed MAC', {...witness,mac:'x'.repeat(64)},ctx,v1,'REJECT'],
 ['future high below cursor',seal({...ctx,version:10,floor:5,high:3}),ctx,{version:10,floor:5,high:3},'REJECT']
];
for(const [name,w,c,v,expected] of cases) assert.equal(verify(w,c,v),expected,name);
console.log('D006_SNAPSHOT_RETENTION_WITNESS_SYNTHETIC_PASS '+cases.length+'/'+cases.length);
