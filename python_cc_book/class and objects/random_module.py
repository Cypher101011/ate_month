#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 12:07:27 2025

@author: a
"""
import random
class Die:
    def __init__(self,sides):
        self.side=random.randint(1, sides)
    def roll_die(self):
        return self.side

roll_1=Die(6)
roll_2=Die(15)
print(roll_2.roll_die())

class Lottery:
    def __init__(self,tickets):
        self.tickets=tickets
    def show_lottery(self):
        win=random.sample(self.tickets,5)
        return ''.join(win)
winner=Lottery(['a','b','c','d,','f','e','1','4','6','4',])

print(winner.show_lottery())