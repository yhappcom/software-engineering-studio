from selenium import webdriver
from pathlib import Path
import json,time,traceback
ROOT=Path(__file__).parent
obs=[]
def wait(driver,pred,label,seconds=30):
    end=time.time()+seconds
    while time.time()<end:
        try:
            val=driver.execute_script(pred)
            obs.append({'t':round(time.time(),3),'label':label,'value':val,'title':driver.title})
            if val: return val
        except Exception as e: obs.append({'t':round(time.time(),3),'label':label,'error':repr(e)})
        time.sleep(.5)
    raise AssertionError(f'timeout: {label}')

def emit(verdict, **extra):
    print(json.dumps({'verdict':verdict,'observations':obs,**extra},indent=2), flush=True)

d=webdriver.Safari()
try:
    d.get('http://127.0.0.1:8769/')
    d.execute_script('registerSW();')
    # Registration can reload an uncontrolled document. Use browser-owned
    # controller state across that navigation, then query the worker version
    # from a fresh invocation in the controlled document.
    wait(d,"return Boolean(navigator.serviceWorker.controller)",'v1-controller-after-initial-registration')
    d.execute_script('registerSW();')
    wait(d,"return document.title==='M006_SW_READY_V1'",'v1-version-confirmed')
    ROOT.joinpath('version.txt').write_text('V2\n')
    d.execute_script('updateSW();')
    wait(d,"return document.title==='M006_SW_CONTROLLER_CHANGED'",'controller-changed-to-new-worker')
    d.refresh(); d.execute_script('registerSW();')
    wait(d,"return document.title==='M006_SW_READY_V2'",'v2-controlled')
    d.quit()
    d=webdriver.Safari(); d.get('http://127.0.0.1:8769/'); d.execute_script('registerSW();')
    # A fresh WebDriver session can likewise begin with an uncontrolled
    # document and reload after discovering the persisted registration. The
    # pre-navigation invocation cannot set the V2 title afterward, so first
    # prove restored control from browser-owned state, then re-query V2.
    wait(d,"return Boolean(navigator.serviceWorker.controller)",'restart-controller-persistence')
    d.execute_script('registerSW();')
    wait(d,"return document.title==='M006_SW_READY_V2'",'restart-v2-version-confirmed')
    emit('SAFARI_SW_REGISTER_UPDATE_RESTART_PASS')
except Exception as e:
    emit('SAFARI_SW_REGISTER_UPDATE_RESTART_FAIL',exception=repr(e),traceback=traceback.format_exc())
    raise
finally:
    try:d.quit()
    except:pass
