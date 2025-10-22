#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 10:43:10 2025

@author: a
"""

def show_message(messages):
    for message in messages:
        print(message)
        
messages=['hi ','how are you','very well']
show_message((messages))
    
def send_messages(messages):
    sent_messages=[]
    while messages:
        message=messages.pop()
        print(f'this message has been sent: {message}')
        sent_messages.append(message)
    return f"{sent_messages}"



print(messages,send_messages(messages[:])
)
    
    