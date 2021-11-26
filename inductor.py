#!/usr/bin/env python
# coding: utf-8

# import libraries
import os
import requests
import json
import time

class inductor():
    def __init__(self):
        self.ip = ''
        self.lst = []
        self.data = {
            'data': self.lst
        }
        
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
        res = int(y["data"]["value"], 16)>>16
        return res

    def collectData(self):
        x = 1 
        t_end = time.time() + 10
        while time.time() < t_end:
            for p in range(7,8):
                res = self.measure(p)
                if not res >= 1000:
                    self.lst.append([x, res])
                    x += 1
                time.sleep(0.005)


if __name__ == '__main__':
    try:
        i = inductor()
        i.config('192.168.178.0/24')
        
        print("Measuring ...")
        i.collectData()
        print('Measuring done')
        
        with open('datalist.txt', 'w') as f:
            f.write(json.dumps(i.data))
        f.close
        print('Data exported')

    except KeyboardInterrupt:
        pass