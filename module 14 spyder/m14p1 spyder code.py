# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:40:09 2026

@author: ski
"""

class Employee:
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary}")

    def calculate_bonus(self, rate):
        return self.salary * rate

emp1 = Employee()

emp1.name = "Alice"
emp1.salary = 50000

emp1.display_info()

rate = float(input("Enter bonus rate: "))

bonus = emp1.calculate_bonus(rate)

print(f"Bonus amount: ${bonus}")
