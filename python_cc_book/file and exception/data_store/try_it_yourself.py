#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 15:15:19 2025

@author: a
"""
import json
from pathlib import Path
def your_number(path):
   
    contents=path.read_text()
    print(f"your favourate number is {contents}")
    
def write_number():
    
    path=Path('value.txt')
    if path.exists():
        your_number(path)
    else:
        number= input("enter number")
        contents=json.dumps(number)
        path.write_text(contents)

write_number()

person={}

def greet_user(path):
    contents = path.read_text()
    data = json.loads(contents)

    # If username exists in saved file
    if "username" in data:
        print(f"Hello Mr {data['name']}! Your username is {data['username']}.")
    else:
        # Ask user to create a username
        username = input("Enter a username to set: ")
        data["username"] = username
        # Save updated data
        path.write_text(json.dumps(data))
        print(f"Username saved! Hello Mr {data['name']}!")


    
   
    
def user_dictnoary():
    path=Path('user.txt')
    if path.exists():
        greet_user(path)
    else:
        person['name']=input("enter your name")
        person['age'] =input("\n \tenter your age : \n")
        person['gender']=input('enter your gender')
        person['date_of_birth']=input('enter your date of birth')
        print(f"we'll remember you mr {person['name']}")
        contents=json.dumps(person)
        path.write_text(contents)
        
user_dictnoary()
        