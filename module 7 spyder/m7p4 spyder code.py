# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:26:10 2026

@author: ski
"""
tpay = 0
count = 0

answer = input("Would you like to start the program? ")

while answer.lower() == "yes":
    name = input("Enter employee name: ")
    hours = float(input("Enter hours worked: "))
    pay = float(input("Enter pay rate: "))
    
    if hours > 40:
        ehours = hours - 40
        gpay = (40 * pay) + (ehours * pay * 1.5)
    elif hours <= 40:
        gpay = hours * pay
    
    print(f"Gross pay of Employee {name} is {gpay}$")
    
    count += 1
    tpay += gpay
    
    answer = input("Do you want to enter another employee? ")
    

agpay = tpay / count
    
print(f"\nNumber of employees: {count} \nTotal gross pay is: {tpay}$\nAverage gross pay is: {agpay}$")

