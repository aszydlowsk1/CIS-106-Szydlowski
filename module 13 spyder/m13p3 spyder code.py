# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:59:39 2026

@author: ski
"""

def load_players(filename):
    players = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, avg = line.split()  
            players[name] = float(avg)
    return players

def print_players(players_dict):
    print(f"{'Player Name':<15} {'Batting Avg':<10}")
    print("-" * 25)
    for name, avg in players_dict.items():
        print(f"{name:<15} {avg:<10.3f}")

filename = 'm12p4.txt'
players = load_players(filename)
print_players(players)