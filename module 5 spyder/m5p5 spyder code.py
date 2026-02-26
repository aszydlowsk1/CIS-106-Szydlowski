# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 14:06:45 2026

@author: adrian szydlowski
"""

name = input("Enter last name: ")
gincome = float(input("Enter your gross income: "))
dependants = int(input("How many dependants do you have: "))

agincome = gincome - (dependants * 12000)

if agincome > 50000:
    tax = .2
else:
    tax = .1

inctax = agincome * tax

if inctax <= 0:
    inctax = 100

print(f"The gross income of {name} is {gincome}$ and taking"\
      f" into account {dependants} dependants the adjusted gross income" \
      f" is {agincome}$ which ends up leaving {inctax}$ in taxes")



