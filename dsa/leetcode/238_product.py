#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 17:50:56 2025

@author: a
"""

class Solution(object):
    def productExceptSelf(self, nums):
        array=[]
        product=1
        counter=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                product*=nums[j]
            array.append(product)
            product=1
        return array