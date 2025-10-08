#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:42:53 2025

@author: a
"""

# make a list of five or more usernames,include the name admin imagineyou are writing code
# that will a greeting to each user after long in to a website loop through the lsit and print a greeting to eachuser

usernames=['luci@13','admin','rohit','hr','anonymus']

for i in range(True):
    username= input('enter yousername..')
    for j in range(len(usernames)):
        if username in usernames:
            if username not in usernames:
                print('invalid username')
            
            elif username=='admin':
                print('you are admin')
                break
            else:
                print(f'hello {username}')
                break
        
current_users=['luci@13','admin','rohit','hr','anonymus']

new_users=['rohit','luci','someone','hiba']

for i in new_users:
    if i in current_users:
        print(f'this username "{i}" is currently uesed')
 