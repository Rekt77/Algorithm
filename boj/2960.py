# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 03:20:34 2019

@author: Rekt77
"""
def Eratosthenes(N, K):
    counter = 0
    numberSet = [False for _ in range(N+1)]

    for i in range(2, N+1):
        for j in range(i, N+1, i):
            if numberSet[j] is False:
                numberSet[j] = True
                counter +=1
                if(counter == K):
                    return(j)
                
            

if __name__ == "__main__":
   N, K = map(int,input().split())
   print(Eratosthenes(N,K))