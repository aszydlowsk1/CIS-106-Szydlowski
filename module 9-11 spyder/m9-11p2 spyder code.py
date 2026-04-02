# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:10:32 2026

@author: ski
"""


def taverage(hits, atbat):
    if atbat == 0:
        return 0
    return hits / atbat

def main():
    count = 0
    
    while True:
        name = input("Enter players name(enter end to end): ")
        
        if name == "end":
            break
        
        hits = float(input("Enter number of hits: "))
        atbat = float(input("Enter number of at bats: "))
        
        average = taverage(hits, atbat)
        
        print(f"Player: {name}")
        print(f"Batting average: {average:.3f}")
        print("-------------------------------------")

        count += 1
        
    print(f"\nTotal number of players entered: {count}")

main()
