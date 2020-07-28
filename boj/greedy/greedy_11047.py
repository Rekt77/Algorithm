# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:51:48 2019

@author: ReKt77
"""

import sys

def Optimizer(coins, price):
    counter = 0
    for coin in reversed(coins):
        if price == 0:
            break
        if price == coin:
            counter +=1
            price = 0
        if price > coin:
            result = price//coin
            counter += result
            price -= result * coin
    return counter


if __name__ == "__main__":
    
    num, price = map(lambda x : int(x), sys.stdin.readline().strip().split())
    coins=list()

    for _ in range(num):
        coin = int(sys.stdin.readline().strip())
        if coin > price:
            break
        coins.append(coin)

    print(Optimizer(coins, price))
