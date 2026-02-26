# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 13:13:29 2026

@author: adrian szydlowski
"""

item = input("select an item (A or B): ").upper()

quantity = int(input("Enter item quantity: "))

if item == "A":
    eprice = quantity * 10.00
else:
    eprice = quantity * 20.00
    
if item == "A":
        uprice = 10.00
else:
        uprice = 20.00

print(f"The unit price for item {item} is {uprice}$ and" \
      f" the extended price is {eprice}$")
    
    