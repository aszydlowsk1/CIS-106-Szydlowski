# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 20:45:42 2026

@author: Adrian Szydlowski
"""

fcost = float(input("Enter fixed cost amount: "))
unitcost = float(input("Enter unit cost:" )) 
unitprice = float(input("Enter unit price(has to be greater than unit cost): "))             

breakeven = fcost / (unitprice - unitcost) 

print("to break even ", breakeven, "units need to be sold")


