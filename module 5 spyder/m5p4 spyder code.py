# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 13:48:14 2026

@author: adrian szydlowski
"""

name = input("What is the name of your appliance? ")
acost= float(input("What is the cost of your applicance? "))

if acost > 1000:
    warranty = acost *.1
else:
    warranty = acost * .05
total = (1 + warranty) * acost

print(f"The cost of {name} is {acost} and the cost of the warranty is" \
      f" {warranty}$ for a total of {total}$")