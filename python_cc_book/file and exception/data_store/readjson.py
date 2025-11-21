#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 17:59:49 2025

@author: a
"""

from pathlib import Path
import json

username=input("enter your username\t: ")


path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"we'll remember you when you came back")