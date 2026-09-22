from selenium import webdriver
from pathlib import Path
import subprocess,time,json,urllib.request
ROOT=Path(__file__).parent
obs=[]
def wait_title(d,title,label,seconds=30):
    end=time.time()+seconds
    while time.time()<end:
        try:
            actual=d.title
            obs.append({'t':round(time.time(),3),'label':label,'title':actual})
            if actual==title:return
        except Exception as e:obs.append({'t':round(time.time(),3),'label':label,'error':repr(e)})
        time.sleep(.5)
    raise AssertionError(f'timeout {label}: wanted {title}')
def origin_down():
    try:urllib.request.urlopen('http://127.0.0.1:8770/',timeout=1);return False
    except Exception:return True
server=subprocess.Popen(['python3','server.py'],cwd=ROOT,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
d=None
try:
    time.sleep(1)
    d=webdriver.Safari();d.get('http://127.0.0.1:8770/');wait_title(d,'M006_APP_READY','online-app')
    d.execute_script('registerSW();');wait_title(d,'M006_CONTROLLED','online-controlled')
    cache_ok=d.execute_async_script("const done=arguments[0]; caches.open('m006-offline-v1').then(async c=>done(Boolean(await c.match('/'))&&Boolean(await c.match('/app.js')))).catch(()=>done(false));")
    obs.append({'label':'cache-precondition','value':cache_ok})
    assert cache_ok,'cache precondition failed'
    d.quit();d=None
    server.terminate();server.wait(timeout=5)
    assert origin_down(),'origin still reachable after server termination'
    obs.append({'label':'origin-down','value':True})
    d=webdriver.Safari();d.get('http://127.0.0.1:8770/?offline-cold-start=1')
    wait_title(d,'M006_APP_READY','offline-cold-start-app')
    controlled=d.execute_script('return Boolean(navigator.serviceWorker.controller)')
    obs.append({'label':'offline-controller','value':controlled})
    assert controlled,'offline page loaded without service-worker controller'
    print(json.dumps({'verdict':'SAFARI_OFFLINE_COLD_START_PASS','observations':obs},indent=2))
finally:
    if d:
        try:d.quit()
        except:pass
    if server.poll() is None:
        server.terminate()
