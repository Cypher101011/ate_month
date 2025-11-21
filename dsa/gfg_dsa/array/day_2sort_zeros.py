#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:36:33 2025

@author: a
"""

# =============================================================================
# # sort zero at last
# =============================================================================
class Solution:
    def pushZerosToEnd(self, arr):
        if 0 not in arr:
            return arr
        
        counter = 0  # position for the next non-zero
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[counter] = arr[counter], arr[i]
                counter += 1   # move only when a non-zero is placed
        
        return arr
