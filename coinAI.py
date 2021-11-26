#!/usr/bin/env python
# coding: utf-8

import numpy as np
import json
import os
from gtts import gTTS
from extractDataPoints import *

def tts(idx, lng):
    coins = ["2 €", "1 €", "0.5 €", "0.2 €", "0.1 €", "0.05 €", "0.02 €", "0.01 €"]
    
    tts = gTTS(coins[idx], lang=lng)
    tts.save('coin.mp3')  
    os.system('mpg321 coin.mp3')

def getKNearestNeighbors(x,X,k=1):          # realizes nearest neighbor search of x in database X
    """
    compute the k nearest neighbors for a query vector x given a data matrix X
    :param x: the query vector x
    :param X: the N x D data matrix (in each row there is data vector) as a numpy array
    :param k: number of nearest-neighbors to be returned
    :return: return list of k line indixes referring to the k nearest neighbors of x in X
    """
    d=[np.linalg.norm(X[i]-x) for i in range(len(X))]                   
    d = np.argsort(d)
    #print("sort d after index: ", d)
    print("Getting kNNs ...")
    return d[:k]

if __name__ == '__main__':
    with open("datalist.txt") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    points = list(jsonObject.values())          # convert json string in python list

    measurement = [points[0]]              # get every second elemnt of the list (time values not needed)
    measurement = measurement[0]                # only the first entry contains the data
    # print("messwerte: ", measurement)

    # Generate dummy data
    # 200 - 100 - 50 - 20 - 10 - 5 - 2 - 1
    X = np.array([[410, 396, 768, 780],     # 2 €
                  [287, 284, 494, 650],     # 1 €
                  [716, 694, 768, 600],     # 50 Cent
                  [695, 674, 715, 550],     # 20 Cent
                  [666, 656, 703, 480],     # 10 Cent
                  [378, 347, 415, 650],     # 5 Cent
                  [420, 440, 468, 540],     # 2 Cent
                  [608, 634, 619, 400],     # 1 Cent 
                  ]);                       # data matrix X: list of data vectors (=database) of dimension D=4

    # x = np.array([1.5, 0.6, 0.7, 1.3]);
    d = Data()
    # messwerte = [2,4,56,7,6,5,3,2,3,45,6,78,9,9,8,7,6,5,4,3,345,456,78,5,4,3,2,3,4,5,1]

    # print("messwerte: ", messwerte)
    if not measurement == []:
        print("Data imported")
        d.extract(measurement)
        x = np.array([d.minL, d.minR, d.maxM, d.length*10])
        #print("Data matrix X=\n",X)
        print("Test vector x=",x)

        # Print all Euklidean distances to test vector x
        #print("Euklidean distances to x: ", [np.linalg.norm(X[i]-x) for i in range(len(X))])                # compute list of Euklidean distances   

        # Search for k nearest neighbor
        k=2

        idx_knn = getKNearestNeighbors(x,X,k)                                                               # get indexes of k nearest neighbors
        #print("idx_knn=",idx_knn)

        # output results
        print("The k Nearest Neighbors of x are the following vectors:")
        for i in range(k):
            idx=idx_knn[i]
            print("The", i+1, "th nearest neighbor is: X[",idx,"]=",X[idx]," with distance ", np.linalg.norm(X[idx]-x))
        tts(idx_knn[0], "en")
    else:
        print('No data available! ')