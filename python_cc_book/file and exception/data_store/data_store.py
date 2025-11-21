#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:39:52 2025

@author: a
"""

# =============================================================================
# storing the data in the file
# =============================================================================

# number_writer.py
from pathlib import Path
import json

numbers=[1,1,1,2,5,4,5,5,47,7,8]
path=Path('numbers.json')
contents=json.dumps(numbers)
path.write_text(contents)
print(contents)