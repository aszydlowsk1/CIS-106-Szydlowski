# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:30:00 2026

@author: ski
"""

names = ['Anderson','Brown','Clark','Davis','Evans',
         'Frank','Garcia','Harris','Irwin','Jones', "Klark"]

def display(a):
    index = 0
    while True:
        try:
            print(a[index])
            index +=1
        except:
            print("\n")
            break

def reverse(a):
    count = 0
    while True:
        try:
            a[count]
            count += 1
        except:
            break

    index = count - 1
    while index >= 0:
        print(a[index])
        index = index - 1

display(names)
reverse(names)