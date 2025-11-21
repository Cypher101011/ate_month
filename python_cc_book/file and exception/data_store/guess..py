#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 15:19:34 2025

@author: a
"""

from pathlib import Path

path=Path('value.txt')
contents=path.read_text()
print(f"your favourate number is {contents}")