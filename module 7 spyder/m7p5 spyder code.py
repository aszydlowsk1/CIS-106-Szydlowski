# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:07:53 2026

@author: ski
"""

answer = input("Do you want to start the program? ")

orderamount = 0
tdiscount = 0

while answer.lower()  == "yes":
   
    
    quantity = float(input("\nEnter quantity: "))
    price = float(input("\nPrice of item: "))
    
    eprice = quantity * price
    
    if eprice > 10000.00:
        discount = .25
    else:
        discount = .1
        
    adiscount = eprice * discount
    total = eprice - adiscount
    
    tdiscount += adiscount
    orderamount += 1
    
    print(f"\nThe extended price is {eprice}$\nafter a discount of {discount}\nthe new total is {total}")
    
    
    answer = input("\nDo you want to run the program again? ")
    
print(f"\nThe total discounted amount over {orderamount} orders is {tdiscount}$")

