#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 11:15:39 2025

@author: a
"""

numDays=int(input("how many days's tempreturne"))
total=0
days=[]
for i in range(1,numDays+1):
    nextDay=int(input(f'day {i} high temp : '))
    days.append(nextDay)
    
avgg=round(sum(days)/numDays,2)
print(days)
print('\n Average ='+str(avgg))

for i in days:
    if i >avgg:
        total+=1

print(f"{total} days more than average")