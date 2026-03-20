# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 18:58:15 2026

@author: ski
"""

file = open("m8p4.odt", "r")

textended = 0
order_count = 0

while True:
    item = file.readline().strip()  
    if not item:
        break
    
    quantity_line = file.readline().strip()
    price_line = file.readline().strip()
    
    quantity = int(quantity_line)
    price = float(price_line)
    
    extended_price = quantity * price
    textended += extended_price
    order_count += 1
    

    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price: ${price:,.2f}")
    print(f"Extended Price: ${extended_price:,.2f}\n")
   


file.close()

average_order = textended / order_count if order_count > 0 else 0


print(f"---------------------------------\n\nTotal Extended Price: ${textended:,.2f}")
print(f"Number of Orders: {order_count}")
print(f"Average Order: ${average_order:,.2f}")