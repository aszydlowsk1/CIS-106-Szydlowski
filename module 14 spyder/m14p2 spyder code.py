# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:04:35 2026

@author: ski
"""

class Student:
    def compute_tuition(self):
        if self.district_code == "I":
            rate = 250
        else:
            rate = 500

        tuition = self.credits * rate
        return tuition

    def display_info(self):
        print("Student:", self.first_name, self.last_name)
        print("District Code:", self.district_code)
        print("Credits:", self.credits)

student1 = Student()

student1.first_name = input("Enter first name: ")
student1.last_name = input("Enter last name: ")
student1.district_code = input("Enter district code (I or O): ").upper()
student1.credits = int(input("Enter enrolled credits: "))

student1.display_info()

tuition = student1.compute_tuition()

print("Computed Tuition:", student1.credits, "x rate =", tuition)
print("Tuition Owed: $", tuition)