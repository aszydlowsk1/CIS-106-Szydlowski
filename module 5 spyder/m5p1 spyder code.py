# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 13:00:36 2026

@author: adrian szydlowski
"""

quantity = float(input("Enter your quantity: "))

if quantity <= 1000:
    price = 5.00
else:
    price = 3.00

eprice = price * quantity 

total = eprice * 1.07

print(f"Your order of {quantity} items at {price}$ per item comes out to {eprice}$ " \
      f"and after a tax of {eprice * .07}$ your total comes out to {total}$")








