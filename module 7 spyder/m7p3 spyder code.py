# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:26:45 2026

@author: ski
"""

count = 0

answer = input("Do you want to begin the program? ")

while answer == "yes":
    name = input("Enter student's last name: ")
    exam1 = float(input("Enter first exam grade: "))
    exam2 = float(input("Enter second exam grade: "))
    
    average = (exam1 + exam2)/2
    
    print(f"the average of {name}'s grades is {average}")
    
    count +=1
    
    answer = input("Would you like to continue? ")

print(f"This code has been run {count} times")