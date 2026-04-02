# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:53:04 2026

@author: ski
"""

def calctotalavg(score1, score2, score3):
    total = score1 + score2 + score3
    avg = total / 3
    return total, avg

name = input("Student last name: ")
score1 = float(input("Score 1: "))
score2 = float(input("Score 2: "))
score3 = float(input("Score 3: "))

total, avg = calctotalavg(score1, score2, score3)

print(f"{name} total:{total:.2f} avg:{avg:.2f}")