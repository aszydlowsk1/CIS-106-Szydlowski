# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:25:21 2026

@author: ski
"""

def calcprice(msrp, make, model, ev):
    make = make.lower()
    model = model.lower()
    ev = ev.lower()
    if ev == "yes":
        disc = 0.30
    elif make == "honda" and model == "accord":
        disc = 0.10
    elif make == "toyota" and model == "rav4":
        disc = 0.15
    else:
        disc = 0.05
    discprice = msrp * (1 - disc)
    finprice = discprice * 1.07
    return finprice, discprice

def main():
    totmsrp = 0
    totsales = 0
    count = 0
    while True:
        ans = input("Enter car? (Yes/No): ").lower()
        if ans != "yes":
            break
        make = input("Make: ")
        model = input("Model: ")
        ev = input("Electric? (yes/no): ")
        msrp = float(input("MSRP: "))
        finprice, discprice = calcprice(msrp, make, model, ev)
        print(f"{make} {model} msrp:${msrp:,.2f} discount:${discprice:,.2f} final price after tax:${finprice:,.2f}")
        totmsrp += msrp
        totsales += finprice
        count += 1
    print(f"cars:{count} totmsrp:${totmsrp:,.2f} totsales:${totsales:,.2f}")

main()