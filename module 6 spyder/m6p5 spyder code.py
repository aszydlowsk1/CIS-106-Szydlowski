# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:17:37 2026

@author: adrian szydlowski
"""



name = input("Enter employee name: ")
salary = int(input(f"Enter {name}'s salary: "))
job = int(input(f"Enter {name}'s job level: "))

if job >= 10:
    bonus = .25
elif job >= 5 and job <= 9:
    bonus = .2
else:
    bonus = .1
    
ebonus = salary * bonus

print(f"{name}'s job level of {job} alongside a salary of {salary} grants a bonus of {ebonus}$")