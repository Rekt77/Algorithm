# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:59:11 2019

@author: Rekt77
"""
from itertools import islice
import sys

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
    n = int(input())
    f = Fibonacci_numbers()
    print(list(islice(f, 0, n))[n-1])