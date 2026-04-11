# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:16:19 2026

@author: ski
"""

class Student:
    def compute_tuition(self):
        rates = {
            "I": 250,
            "O": 500,
            "X": 800,
            "G": 250
        }

        rate = rates.get(self.district_code, 500)
        return self.credits * rate

    def display_info(self):
        print("Student:", self.first_name, self.last_name)
        print("District Code:", self.district_code)
        print("Credits:", self.credits)


student1 = Student()

student1.first_name = input("Enter first name: ")
student1.last_name = input("Enter last name: ")
student1.district_code = input("Enter district code (I, O, X, G): ").upper()
student1.credits = int(input("Enter enrolled credits: "))

student1.display_info()

print("Tuition Owed: $", student1.compute_tuition())