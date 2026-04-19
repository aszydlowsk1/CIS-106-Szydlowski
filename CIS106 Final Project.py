# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:58:08 2026

@author: ski
"""


dogs = []

def main():
    menu()

def menu():
    while True:
        print("\nDog Rescue")
        print("-----------")
        print("1. Add a Dog")
        print("2. View Dogs")
        print("3. Find Dog")
        print("4. Quit")

        choice = input("Select a choice: ")

        if choice == "1":
            addDog()
        elif choice == "2":
            viewDogs()
        elif choice == "3":
            findDog()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again.")

def addDog():
    print("\nAdd a Dog")

    name = input("Dog Name: ")
    breed = input("Dog Breed: ")
    age = input("Age: ")
    weight = input("Weight: ")

   
    dog = [name, breed, age, weight]
    dogs.append(dog)

    print("Dog added successfully!")

def viewDogs():
    print("\nView Dogs")

    if len(dogs) == 0:
        print("No dogs available.")
        return

    for i, dog in enumerate(dogs, start=1):
        print(f"\nDog #{i}")
        print(f"Name: {dog[0]}")
        print(f"Breed: {dog[1]}")
        print(f"Age: {dog[2]}")
        print(f"Weight: {dog[3]}")

def findDog():
    print("\nFind Dog")

    search_name = input("Enter dog name to search: ")

    found = False

    for dog in dogs:
        if dog[0].lower() == search_name.lower():
            print("\nDog Found:")
            print(f"Name: {dog[0]}")
            print(f"Breed: {dog[1]}")
            print(f"Age: {dog[2]}")
            print(f"Weight: {dog[3]}")
            found = True

    if not found:
        print("Dog not found.")


main()