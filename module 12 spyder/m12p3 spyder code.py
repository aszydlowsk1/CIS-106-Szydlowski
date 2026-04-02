# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:24:42 2026

@author: ski
"""

lastnames = ['Anderson','Brown','Clark','Davis','Evans',
             'Frank','Garcia','Harris','Irwin','Jones']
scores = [85, 92, 78, 88, 90, 76, 95, 80, 84, 91]


count = 0
for n in lastnames:
    count += 1


def display(a, b):
    index = 0
    while index < count:
        print(a[index], b[index])
        index += 1


def high_low(a, b):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0
    index = 0
    while index < count:
        if b[index] > high_var:
            high_var = b[index]
            high_index = index
        if b[index] < low_var:
            low_var = b[index]
            low_index = index
        index += 1
    print("Highest score:", a[high_index], high_var)
    print("Lowest score:", a[low_index], low_var)


print("All names and scores:")
display(lastnames, scores)

print("\nHighest and lowest scores:")
high_low(lastnames, scores)
