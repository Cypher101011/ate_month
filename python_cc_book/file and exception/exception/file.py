#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 10:34:28 2025

@author: a
"""

from pathlib import Path
def count_words(path):
  
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
    
        print(f"sorry , the file {path} does not exist")
    else:
    
        words=contents.split()
        num_words=len(words)
        print(f"the file {path} has about {num_words} words.")


path=Path('shekspier.txt')
count_words(path)


filenames=['exceptions.py','shekspier.py',
           'exceptions2.py','shekspier.txt','file.py']
for filename in filenames:
    path=Path(filename)
    count_words(path)