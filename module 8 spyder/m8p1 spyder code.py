# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:33:20 2026

@author: ski
"""



principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))


tinterest = 0




print(f"{'Year':<5}{'Beginning Balance':>20}{'Ending Balance':>20}")


for year in range(1, 6):
    
    interest = principal * rate
    balance = principal + interest
    
    tinterest += interest

    
    print(f"{year}${principal:>12}${balance:>22,.2f}")

    principal = balance



print(f"\nTotal interest earned: ${tinterest:,.2f}")




    


    

 
