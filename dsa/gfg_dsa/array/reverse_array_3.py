#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 11:25:30 2025

@author: a
"""

def reverseArray(arr):
        length=len(arr)
        if length==1:
            return arr
        i=0
        while i <length//2:
            arr[i],arr[length-i-1]=arr[length-i-1],arr[i]
            i+=1
        return arr

reverseArray([1, 2, 3, 4, 5])