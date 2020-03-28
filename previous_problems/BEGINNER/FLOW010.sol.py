#!usr/bin/env python
dictionary = {'B':'BattleShip', 'b':'BattleShip', 'C':'Cruiser', 'c':'Cruiser', 'D':'Destroyer', 'd':'Destroyer', 'F':'Frigate', 'f': 'Frigate'}
t = int(input())
for i in range(t):
    n = input()
    print(dictionary[(n)])    