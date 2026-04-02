# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:41:27 2026

@author: ski
"""

names = ['Anderson','Brown','Clark','Davis','Evans',
         'Frank','Garcia','Harris','Irwin','Jones', 'Klark']

scores = [69, 85, 92, 78, 88, 90, 76, 95, 80, 84, 91]

count = 0
for n in names:
    count += 1

def display(a, b):
    index = 0
    while index < count:
        print(a[index], b[index])
        index += 1

def reverse(a, b):
    index = count - 1
    while index >= 0:
        print(a[index], b[index])
        index -= 1

print("In order:")
display(names, scores)

print("\nIn reverse order:")
reverse(names, scores)