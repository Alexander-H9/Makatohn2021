#!/usr/bin/env python
# coding: utf-8

print("-----------------------------")
val = input("Amount (in €) to withdraw: ")
print("-----------------------------")

nb = None
#for cast in (int,float):
try:
    nb = float(val)
    idx = str(nb).find(".")
    if idx != -1:
        val = val[:idx+3]
        
        with open('account.txt', 'r') as f:
            balance = f.read()
        f.close

        balance = float(balance) - abs(val)

        with open('account.txt', 'w') as f:
            f.write(str(balance))
        f.close
        print("Action successful!")
        
except ValueError:
    print("Not supported!")
    pass