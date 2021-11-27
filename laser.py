#!/usr/bin/env python
# coding: utf-8

# import libraries
import os
import requests
import json
import time

class laser():
    def __init__(self):
        self.ip = ''
        self.lst = []
        
    def config(self, net):
        lines = []
        matchstr = ""
        out = os.popen('nmap -sP ' + net).read()
        out = os.popen('arp').read()

        lines = out.splitlines()
        for i in range(len(lines)):
            if "00:02:01:61:49:9e" in lines[i]:
                matchstr = lines[i].split()[0]      
        self.ip = matchstr
        
    def measure(self, port):
        url = 'http://' + self.ip
        portstr = "/iolinkmaster/port[{}]/iolinkdevice/pdin/getdata".format(port)
        myobj = {"code":"request","cid":4711, "adr":portstr}
        x = requests.post(url, json = myobj)
        y = json.loads(x.text)
        
        if y["code"] == 200:
            return False
        else:
            return True

    def collectData(self):
        while True:
            for p in range(5,6):
                res = self.measure(p)
                time.sleep(0.001)
            if res == True:
                break


if __name__ == '__main__':
    #print("### LASER ###")
    try:
        l = laser()
        print("\nLaser - Configuring")
        l.config('192.168.178.0/24')
        
        print("Laser - Waiting for coin")
        l.collectData()
        print("Laser - Coin detected")

    except KeyboardInterrupt:
        pass