#!/usr/bin/env python
# coding: utf-8

val = input("Amount to withdraw in €: ")

with open('account.txt', 'r') as f:
    balance = f.read()
f.close

balance = float(balance) - float(val)

with open('account.txt', 'w') as f:
    f.write(str(balance))
f.close