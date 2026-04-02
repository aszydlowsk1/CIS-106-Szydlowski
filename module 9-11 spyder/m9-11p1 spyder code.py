# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:47:42 2026

@author: ski
"""

def ceprice(quantity, uprice):
    total = quantity * uprice
    
    if total > 10000:
            total *= .9
            
    return total
    
def main():
    tprice = 0
    
    while True:
        quantity = float(input("Enter quantity: "))
        if quantity == 0:
            break
        price = float(input("Enter unit price: "))
        
        eprice = ceprice(quantity, price)
        
        print(f"Quantity: {quantity}")
        print(f"Unit price: ${price:.2f}")
        print(f"Extended price: ${eprice:.2f}")
        print("-" * 30)
        
        tprice += eprice
        
    print(f"Total Extended Price: ${tprice:.2f}")
    
main()