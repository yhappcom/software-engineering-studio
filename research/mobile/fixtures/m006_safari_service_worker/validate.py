from selenium import webdriver
from pathlib import Path
import json,time
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

d=webdriver.Safari()
try:
    d.get('http://127.0.0.1:8769/')
    d.execute_script('registerSW();')
    wait(d,"return document.title==='M006_SW_READY_V1'",'v1-controlled')
    ROOT.joinpath('version.txt').write_text('V2\n')
    d.execute_script('updateSW();')
    wait(d,"return document.title==='M006_SW_CONTROLLER_CHANGED'",'controller-changed-to-new-worker')
    d.refresh(); d.execute_script('registerSW();')
    wait(d,"return document.title==='M006_SW_READY_V2'",'v2-controlled')
    d.quit()
    d=webdriver.Safari(); d.get('http://127.0.0.1:8769/'); d.execute_script('registerSW();')
    wait(d,"return document.title==='M006_SW_READY_V2'",'restart-registration-persistence')
    print(json.dumps({'verdict':'SAFARI_SW_REGISTER_UPDATE_RESTART_PASS','observations':obs},indent=2))
finally:
    try:d.quit()
    except:pass
