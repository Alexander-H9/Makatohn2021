#!/usr/bin/env python
# coding: utf-8

import os
from gtts import gTTS

def tts(idx, lng):
    coins = [(2, "2 €"), (1, "1 €"), (0.5, "0.5 €"), (0.2, "0.2 €"), (0.1, "0.1 €"), (0.05, "0.05 €"), (0.02, "0.02 €"), (0.01, "0.01 €")]
    coin_val = coins[idx][0]
    coin_desc = coins[idx][1] 
    
    print("\nCoin: " + coin_desc)
    
    with open('account.txt', 'r') as f:
        balance = float(f.read())
    f.close
    
    balance += coin_val
    balance = round(balance, 2)
    
    print("Account balance: " + str(balance) + " €"  + "\n")
    
    with open('account.txt', 'w') as f:
        f.write(str(balance))
    f.close
    
    tts_text = str(coin_desc) + " Coin. " + str(balance) + " € in the bank."
    tts = gTTS(tts_text, lang=lng)
    tts.save('coin.mp3')
    os.system('mpg321 -q coin.mp3')