# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:31:05 2026

@author: ski
"""


def cforecast(month, sale):
    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    elif month in ["oct", "nov", "dec"]:
        percent = 0.25
    else:
        percent = 0

    nsale = sale * (1 + percent)

    return nsale

def main():
    while True:
        answer = input("Do you want to enter data: ").lower()
        
        if answer != "yes":
            break
        
        name = input("Enter name: ")
        month = input("Enter month: ")
        sale = float(input("Enter sales: "))
        
        forecast = cforecast(month, sale)

        print(f"Name: {name}")
        print(f"Month: {month}")
        print(f"Next Month Forecast Sales: ${forecast:.2f}")
        print("----------------------------------")

main()

