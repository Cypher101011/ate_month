#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:42:37 2025

@author: a
"""

from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path = Path('programming.txt')
print(path)
path.write_text(contents)

lines=path.read_text().splitlines()
for line in lines:
    print(line)
    


# Try it yourself

name=input("enter your name :")
guest=Path('guest.txt')
guest.write_text(name)
guests=guest.read_text().splitlines()
for line in guests:
    print(line)