#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 17:33:50 2025

@author: a
"""

class Solution(object):
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s='qwqwqqqq'):

        substring=[s[1]]
       
        for i in range(1,len(s)):
          
            if substring[-1]!=s[i]:
                substring.append(s[i])  
                print(substring)
        return len(substring)

if __name__ == "__main__":
    s=input()

    sol=Solution()
    print(sol.lengthOfLongestSubstring(s))
    