#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 19:02:09 2025

@author: a
"""

from pathlib import Path
path=Path('pi_million_digits.txt')
contents=path.read_text()
# print(contents)

# contents=contents.rstrip()
# print(contents)

# contents=path.read_text().rstrip()

# # relative path
# # path=Path('pi_digits.txt')
# # =============================================================================
# # absolute path1
# # =============================================================================

# # path =Path('/home/a/Pictures/ate_month/python_cc_book/file\and\exception/exception/pi_digits.txt')
# contents=path.read_text()
# print(contents)

# linear
lines=contents.splitlines()
# for line in lines:
#     print(line)

pi_string=''
for line in lines:
    pi_string+=line.lstrip()

birthday=input("Enter your birthday,in the form of ddmmyy")
if birthday in pi_string:
    print("your birthady hass apper")
else:
    print("not apper")
print(len(pi_string))
print(path)