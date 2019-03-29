# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 01:32:05 2019

@author: ReKt77
"""

from itertools import islice

class Fibonacci_numbers():
    def __init__(self):
        self.prev = 0
        self.curr = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

if __name__ == "__main__" :
    K = int(input())
    for i in range(K):
        n = int(input())
        f = Fibonacci_numbers()
        fib = list(islice(f, 0, n))
        if n==0:
            print("1 0")
        elif n==1:
            print("0 1")
        else:
            print("%d %d"%(fib[n-2],fib[n-1]))