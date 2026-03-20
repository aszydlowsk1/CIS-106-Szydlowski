# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:09:48 2026

@author: ski
"""

file = open("m8p5.odt", "r")

total = 0
count = 0

while True:
    name = file.readline().strip()
    if not name:
        break

    code = file.readline().strip()
    credits_line = file.readline().strip()
    credits = int(credits_line)

    if code.upper() == "I":
        cost = 250.00
    else:
        cost = 500.00

    tuition = credits * cost
    total += tuition
    count += 1

    print(f"Student: {name}")
    print(f"Credits Taken: {credits}")
    print(f"Tuition Owed: ${tuition:,.2f}\n")
    

file.close()

print(f"------------\n\nTotal Tuition Owed: ${total:,.2f}")
print(f"Number of Students: {count}")