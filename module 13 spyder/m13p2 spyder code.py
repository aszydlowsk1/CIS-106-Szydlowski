# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:13:38 2026

@author: ski
"""

students = {
    "Alice": [85, 90, 88],
    "Bob": [92, 87, 91],
    "Charlie": [78, 82, 80],
    "Diana": [88, 85, 90],
    "Ethan": [95, 93, 96]
}

def student_averages(data):
    averages = []
    for name, grades in data.items():
        avg = sum(grades) / len(grades)
        averages.append([name, avg])
    return averages

def class_averages(data):
    num_students = len(data)
    num_grades = len(next(iter(data.values())))
    totals = [0] * num_grades
    for grades in data.values():
        for i in range(num_grades):
            totals[i] += grades[i]

    averages = [total / num_students for total in totals]
    return averages

student_avg_list = student_averages(students)
class_avg_list = class_averages(students)

print(f"{'Student Name':<15} {'Average':<10}")
print("-" * 25)

for name, avg in student_avg_list:
    print(f"{name:<15} {avg:<10.2f}")

print("\nClass Averages for Each Grade:")
print("-------------------------------------------------------")

for i, avg in enumerate(class_avg_list, start=1):
    print(f"Grade {i:<10}: {avg:.2f}")