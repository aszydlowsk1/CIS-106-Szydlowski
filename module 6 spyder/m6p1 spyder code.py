# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:18:39 2026

@author: adrian szydlowski
"""

quantity = int(input("Input amount of widgets: "))

if quantity > 10000:
    price = 10
elif quantity <= 10000 and quantity >= 5000:
    price = 20
elif quantity < 5000:
    price = 30

tax = .07

eprice = quantity * price

taxa = eprice * tax

total = taxa + eprice

print(f"An order of {quantity} items priced at {price}$ per item, comes out to"
      f" an extended price of {eprice}$ and after {taxa}$ in taxes your total is {total}$")

