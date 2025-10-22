#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 18:52:55 2025

@author: a
"""

def getAlternative(arr):
    for i in range(0,len(arr),2):
        print(arr[i])

getAlternative([1,3,4,5,5])