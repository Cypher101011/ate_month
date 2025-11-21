#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 10:19:08 2025

@author: a
"""

from pathlib import Path
path=Path('learn.txt')
contents=path.read_text()

print(contents)
lines=contents.splitlines()
print(lines)

array=[]
for line in lines:
    line=line.replace('python','C')
    array.append(line)
    
print(array)


for line in contents.splitlines():
    line=line.replace('python', 'c')
    array.append(line)
print(array)

# =============================================================================
# writing to the fiel
# =============================================================================

writepath=Path('programing.txt')

new_contents='\nthere is something new \n'
new_contents+='i also love working with data'
print(new_contents)
writepath.write_text(new_contents)