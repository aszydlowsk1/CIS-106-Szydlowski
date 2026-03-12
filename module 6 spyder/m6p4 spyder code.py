# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:51:17 2026

@author: adrian szydlowski
"""

quantity = int(input("Enter the amount of tickets you would like to purchase: "))

if quantity >= 25:
    price = 50
elif quantity >= 10 and quantity <= 24:
    price = 60
elif quantity >= 5 and quantity <= 9:
    price = 70
elif quantity <= 4:
    price = 75

cost = price * quantity

print(f"The cost of {quantity} tickets at {price}$ per ticket comes out to {cost}$")
