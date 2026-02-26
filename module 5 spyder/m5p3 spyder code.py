# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 13:36:14 2026

@author: adrian szydlowski
"""

quantity = int(input('How many books would you like to order? '))
bcost = float(input("How much does each book cost? "))

ecost = quantity * bcost

if ecost <= 50.00:
    shipping = 25.00
else:
    shipping = 0


if ecost <= 50.00:
    tcost = ecost + shipping
else:
    tcost = ecost
    

print(f"For your order of {quantity} books at {bcost}$ per book your"\
      f" extended cost is {ecost}$ and your shipping is {shipping}$ for a" \
          f" total of {tcost}$")







