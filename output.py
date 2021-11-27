#!/usr/bin/env python
# coding: utf-8

import os
from gtts import gTTS

def tts(idx, lng):
    coins = ["2 €", "1 €", "0.5 €", "0.2 €", "0.1 €", "0.05 €", "0.02 €", "0.01 €"]
    coin = coins[idx]
    
    print("\nResult: " + coin + "\n")
    tts = gTTS(coin, lang=lng)
    tts.save('coin.mp3')
    os.system('mpg321 -q coin.mp3')