#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 16:00:25 2025

@author: a
"""

class Solution(object):
    
    def __init__(self):
        pass
    def mergeAlternately(self, word1='lu', word2='michal'):
        large=max(word1,word2,key=len)
        merged=''
        word_first=list(word1)
        word_second=list(word2)
        for i in range(len(large)):
            if word_first:
                merged=merged+word_first.pop(0)
            if word_second:
                merged=merged+word_second.pop(0)
        
        return merged
        
    
sl=Solution()
print(sl.mergeAlternately())
