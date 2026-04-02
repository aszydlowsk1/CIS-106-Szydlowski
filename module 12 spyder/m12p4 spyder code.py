# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:39:00 2026

@author: ski
"""

names = []
averages = []

with open('m12p4.txt', 'r') as file:
    for line in file:
        parts = line.split()
        names.append(parts[0])
        averages.append(float(parts[1]))


def display(a, b):
    index = 0
    while index < len(a):
        print(a[index], b[index])
        index += 1


def search(a, b, target):
    index = 0
    found = False
    while index < len(a):
        if a[index].lower() == target.lower():  
            print("Found:", a[index], b[index])
            found = True
            break
        index += 1
    if not found:
        print(target, "not found")


print("All players:")
display(names, averages)

while True:
    last = input("\nEnter last name to search (or 'exit' to quit): ")
    if last.lower() == 'exit':
        break
    search(names, averages, last)