#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 11:21:28 2025

@author: a
"""

class Solution:
    def getSecondLargest(self, arr):
        if len(arr)<2:
            return -1
        largest=second=float('-inf')
    
        for num in arr:
            if largest<num: 
                second=largest
                largest=num
            elif largest>num and num>second:
                second=num
        return second if second!=float('-inf') else -1
        
sol=Solution()
sol.getSecondLargest([12, 35, 1, 10, 34, 1])