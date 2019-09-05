#!/usr/lib/python3.6

import json
import requests
import subprocess

def main():

    webhook_url = #   add here  
    
    load = subprocess.check_output('uptime')
    load = load.decode('utf-8')

    memory = subprocess.check_output("free | grep Mem | awk '{print int($3/$2 * 100)}' ", shell = True)
    memory = memory.decode('utf-8')

    uname = subprocess.check_output('hostname')
    uname = uname.decode('utf-8')

    process = subprocess.check_output("ps -ef | wc -l", shell = True)
    process = process.decode('utf-8')
    
    message = "["+uname[:-1]+"]" + load[28:-1] + ", mem% :" + memory[:-1] +"%, #process : "+process

    payload = {"text": message }
    requests.post(
            webhook_url, data = json.dumps(payload),
            headers={'Content-Type': 'application/json'}
            )
    
if __name__=='__main__':
    main()

