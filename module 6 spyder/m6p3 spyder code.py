# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:59:36 2026

@author: adrian szydlowski
"""

amount = float(input("Enter your principle amount for your account: "))
years = float(input("Enter your years to maturity for your account: "))

if amount > 100000 and years == 5:
    interest = 1.06
elif amount >= 50000 and amount <= 100000 and years == 10 :
    interest = 1.05
elif amount >= 50000 and amount <= 100000 and years == 5 :
    interest = 1.04
else:
    interest = 1.02
    
print(f"The interest you will accumulate on an account with a principle of {amount}$ " 
      f"and {years} years to maturity after one year with an interest" 
      f" rate of {interest} is {amount * interest}$")
