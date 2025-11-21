#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:17:22 2025

@author: a
"""

def getSecondLargest(arr):
    n = len(arr)
    largest=-1
    secondLargest=-1
    
    for i in range(n):
        if arr[i]>largest:
            largest,secondLargest=arr[i],largest
        elif arr[i]<largest and arr[i]>secondLargest:
            arr[i]=secondLargest
    return secondLargest

# =============================================================================
# with few python tricks without fol llp
# =============================================================================

    arr=list(set(arr))
    arr.sort()
    if arr:
        arr.pop()
        if arr:
            return arr[-1]
        else:return -1
    else:return -1