# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:36:18 2026

@author: adrian szydlowski
"""

number = int(input("Enter part number: "))
quantity = int(input("Enter amount: "))

if number == 10 or number == 55:
    cost = 1
elif number == 99:
    cost = 2
elif number == 70 or number == 80:
    cost = 3
else:
    cost = 5

total = quantity * cost

print(f"The item price for item {number} is {cost}$ per item and for {quantity} items, your total is {total}$")
70