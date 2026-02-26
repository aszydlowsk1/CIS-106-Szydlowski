# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 19:06:25 2026

@author: adrian szydlowski
"""



pprice = float(input("what is your purchase price per share? "))
cprice = float(input("what is the current price per share? "))
quantity = int(input("how many shares are owned? "))

print(f"your net profit from your shares is {(cprice - pprice) * quantity} dollars")





