# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:08:57 2020

@author: davywavee
"""

import os
import sys
import time
import requests
from requests.auth import HTTPDigestAuth

addr = "172.16.10.51"
dir = "c:/Users/davel/desktop/amcrestsnaps"
i=0

if not os.path.exists(dir):
    os.makedirs(dir, 777)
    
class amcrest:
    
    def __init__(self, ip, path):
        self.ip =ip
        self.path = path
        
    def get_snapshot(self):
        snapshot = requests.get("http://" + self.ip + "/cgi-bin/snapshot.cgi?channel=1", auth = HTTPDigestAuth('admin','12345'))
        ltime = time.localtime()
        cdate = str(ltime[0])+str(ltime[1])+str(ltime[2])+str(ltime[3])+str(ltime[4])+str(ltime[5])
        fname = self.path + "/" + "snapshot" + cdate  + ".jpg"
        print(fname)
        with open(fname, 'wb') as file:
            file.write(snapshot.content)
        return(snapshot.status_code)


while True:
    try:
        snap1 = amcrest(addr, dir)
        status = snap1.get_snapshot()
        print(status)
        time.sleep(5)
        sys.exit

    except KeyboardInterrupt:
        print("all done.")
