#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 10:20:05 2025

@author: a
"""

from pathlib import Path
import json



def get_stored_username(path):
    '''get stored username if available'''
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None
def get_new_username(path):
    '''prompt for a new username'''
    
    username = input("whats your name ?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    '''greet user by name'''
    path=Path('username.json')
    username=get_stored_username(path)
    
    if username:
        print(f"welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"we'll remember you when you came back, {username}")
        
greet_user()