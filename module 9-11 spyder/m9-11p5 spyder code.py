# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:49:38 2026

@author: ski
"""
def calcdiscount(qty, price, rate):
    total = qty * price
    discamount = total * rate
    finprice = total - discamount
    return discamount, finprice

qty = int(input("Quantity: "))
price = float(input("Price per unit: "))
rate = float(input("Discount rate: "))

discamount, finprice = calcdiscount(qty, price, rate)

print(f"qantity:{qty} price:${price:,.2f} discount:${discamount:,.2f} total:${finprice:,.2f}")