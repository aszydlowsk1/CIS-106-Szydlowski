# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:57:57 2026

@author: ski
"""

a = 0
b = 1

print("\nFibonacci sequence:\n")

for i in range(20):
    print(a, end=", ")


    c = a + b
    a = b
    b = c
    
    