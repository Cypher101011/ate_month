#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 11:18:52 2025

@author: a
"""

myDict={'name':'Edy','age':26}
myDict['age']=27
myDict['address']='london'
print(myDict)

def traverseDict(dict):
    for key,value in dict.items():
        print(key,value)
traverseDict(myDict)

def searchVal(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return 'value dosent exist '

searchVal(myDict, 27)