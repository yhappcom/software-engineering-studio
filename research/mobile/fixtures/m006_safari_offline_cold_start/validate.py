from selenium import webdriver
from pathlib import Path
import subprocess,time,json,urllib.request,traceback
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
def wait_controller(d,label,seconds=30):
    end=time.time()+seconds
    while time.time()<end:
        try:
            controlled=bool(d.execute_script('return Boolean(navigator.serviceWorker.controller)'))
            obs.append({'t':round(time.time(),3),'label':label,'controlled':controlled,'title':d.title})
            if controlled:return
        except Exception as e:obs.append({'t':round(time.time(),3),'label':label,'error':repr(e)})
        time.sleep(.5)
    raise AssertionError(f'timeout {label}: service-worker controller absent')
def origin_down():
    try:urllib.request.urlopen('http://127.0.0.1:8770/',timeout=1);return False
    except Exception:return True
server=subprocess.Popen(['python3','server.py'],cwd=ROOT,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
d=None
try:
    time.sleep(1)
    d=webdriver.Safari();d.get('http://127.0.0.1:8770/');wait_title(d,'M006_APP_READY','online-app')
    # registerSW() deliberately reloads the first uncontrolled document once the
    # worker is ready.  After that navigation the app script resets the title to
    # M006_APP_READY, so document.title is not a valid controller oracle.
    d.execute_script('registerSW();');wait_controller(d,'online-controlled')
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
    print(json.dumps({'verdict':'SAFARI_OFFLINE_COLD_START_PASS','observations':obs},indent=2),flush=True)
except Exception as e:
    print(json.dumps({'verdict':'SAFARI_OFFLINE_COLD_START_FAIL','error':repr(e),'observations':obs},indent=2),flush=True)
    traceback.print_exc()
    raise
finally:
    if d:
        try:d.quit()
        except:pass
    if server.poll() is None:
        server.terminate()
