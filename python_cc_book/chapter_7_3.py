#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 12:17:50 2025

@author: a
"""

# confiremd_users.py1
unconfirmed_users=['alice','brian','candace']

confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    
    print(f'verifying user: {current_user.title()}')
    confirmed_users.append(current_user)
    
    print("\t\n The followinguser have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
        

pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# mountain_poll.py
responses={}

# set a flag to indicate that polling is active

polling_active=True

while polling_active:
    #Prompt for the person's name and reponse.
    name =input("\n what is your name ?")
    response=input("which mountain would you like to cliomb someday ?")
    #store the response in the dictonary.
    responses[name]=response
    
    # find out if anyone else is going to take poll
    repeat =input("would you like to lelt another persone respond ?(yse/no)" )
    if repeat=='no':
        polling_active=False
# dictnoary
print(f"dictnoary is {responses}")
# Polling is complete.Show the results.
print("\n Poll Result ")

for name, response in responses.items():
    print(f'{name} would like to climeb {response}')