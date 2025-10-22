#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 17:34:14 2025

@author: a
"""

def minion_game(string):
    stewe=[]
    kevi=[]
    kev=''
    st_word=''
    for i in range(len(string)):
        if string[i] in 'aeiouAEIOU':
            for j in range(i,len(string)):
                st_word+=string[j]     
                stewe.append(st_word)
            st_word=''
        if string[i] not in 'aeiouAEIOU':
            for j in range(i,len(string)):
                kev+=string[j]
                kevi.append(kev)
            kev=''
    kevi=set(kevi)            
    stewe=set(stewe)
    kevin(kevi,stewe,string)
def kevin(kevin,stev,string):
    kevi=list(kevin)
    stuart=list(stev)
    score_k=0
    score_s=0
    score_kevin=[]
    score_stv=[]
    for i in kevi:
        score_k=string.count(i)
        score_kevin.append(score_k)
        score_k=0
    
    for i in stuart:
        score_s=string.count(i)
        score_stv.append(score_s)
        score_s=0
    sum_kev=sum(score_kevin)
    sum_stv=sum(score_stv)
    if sum_kev>sum_stv:
        print(score_kevin)
        print(kevi)
        print(f"Kevin {sum_kev}")
    else:
        print(f"Stuart {sum_stv}")

if __name__ == '__main__':
    s = 'banana'

    minion_game(s)