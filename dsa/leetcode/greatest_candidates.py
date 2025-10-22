#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:05:15 2025

@author: a
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        extra=[]
        for i in candies:
            if i+extraCandies>=max(candies):
                extra.append(True)
            else:
                extra.append(False)
        return extra
                
sol=Solution()
print(sol.kidsWithCandies([2,3,5,1,3], 3))