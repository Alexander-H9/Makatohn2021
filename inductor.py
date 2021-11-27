#!/usr/bin/env python
# coding: utf-8

# import libraries
import os
import requests
import json
import time
import matplotlib.pyplot as plt

class inductor():
    def __init__(self):
        self.ip = ''
        self.lst = []
        self.data = {
            'data': self.lst
        }
        self.plot = []
        
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
        z = 1 
        t_end = time.time() + 4
        while time.time() < t_end:
            for p in range(7,8):
                res = self.measure(p)
                if not res >= 1000:
                    self.lst.append(res)
                    self.plot.append([z, res])
                    z += 1
                time.sleep(0.005)


if __name__ == '__main__':
    #print("### INDUCTOR ###")
    try:
        i = inductor()
        print("Inductor - Configuring")
        i.config('192.168.178.0/24')
        
        print("Inductor - Transmitting status")
        with open('i_status.txt', 'w') as f:
            f.write("True")
        f.close
        
        print("Inductor - Measuring coin")
        i.collectData()
        
        if not i.lst == []:
            x, y = zip(*i.plot)
            plt.scatter(x, y)
            plt.title("Coin measurement")
            plt.xlabel("Count")
            plt.ylabel("Value")
            plt.ylim([0, 1000])
            plt.savefig("plot.png")
            print("Inductor - Plotted data")
        
        with open('datalist.txt', 'w') as f:
            f.write(json.dumps(i.data))
        f.close
        print("Inductor - Exported data")

    except KeyboardInterrupt:
        pass