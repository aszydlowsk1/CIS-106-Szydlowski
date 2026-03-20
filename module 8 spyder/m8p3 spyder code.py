# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 00:10:30 2026

@author: ski
"""

file = open("m8p3.odt", "r")

tbonus = 0


while True:
    name = file.readline().strip()
    
    if not name:
        break
    
    rsalary = file.readline().strip()
    salary = float(rsalary)

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    tbonus += bonus


    print(f"Employee: {name}")
    print(f"Salary: ${salary:,.2f}")
    print(f"Bonus: ${bonus:,.2f}\n")
    
file.close()


print(f"-------------------------- \nTotal Bonuses Paid: ${tbonus:,.2f}")