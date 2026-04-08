# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:59:22 2026

@author: ski
"""

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}


print(f"{'Student Name':<15} {'Grade':<10}")
print("-------------------------------------------------")


total = 0
for name, grade in students.items():
    print(f"{name:<15} {grade:<10}")
    total += grade


average = total / len(students)
print("-------------------------------------------------")
print(f"{'Average':<15} {average:<10.2f}")


