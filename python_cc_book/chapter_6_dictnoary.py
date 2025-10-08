#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 11:41:14 2025

@author: a
"""
# alian.py

alien_0={'color':'green',
         'points':5}
print(alien_0['color'])
print(alien_0['points'])


new_points=alien_0['points']
print(f'you just earned {new_points} points !')
# print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25

alien_0={
    
    'x_position':0,
    'y_position':22,
    'speed':'medium'}

print(f'Orignal position:{alien_0["x_position"]}')
if alien_0['speed']=='slow':
    x_increment =1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
    
alien_0['x_position']=alien_0['x_position']+x_increment

print(f"New Position:{alien_0['x_position']}")

alien_0['speed'] = 'fast'
print(alien_0)
# del alien_0['']
print('\n after \n',alien_0)
print(alien_0['x_position'])

# favorite_languages.py

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'}
print(len(favorite_languages))

lucifer={
    'name':'lucifer',
    'last name':'morningstar',
    'age':666666,
    'city':'los angelos'
    
    
    
    }
print(lucifer)
lucifer['favoriet number']=6
print(lucifer)



glossary ={
    'if':'conditional',
    'else':'also conditional',
    'for' :'loop',
    'while':'loop',
    'list':[1,2,3,4,5]
    
    
    
    
    }
print(glossary)
print(glossary['if'])

# looping through dict1



for key,value in glossary.items():
   
    print(f'{key} ={value}')
    
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print (name.title())

friends=['phil','sarah','edward','luci']

for name in favorite_languages.keys():
    if name not in friends:
        print(f"HI {name.title()}.")
    
    if name in friends:
        language=favorite_languages[name].title()
        print(f'\t{name.title()},i see you love {language}')




for language in set( favorite_languages.values()):
    print(language.title())








rivers={
        'nile':'egypt',
        'gagna':'himalayan',
        'bramhaputra':'meghalay',
        'jordan':'israil'}

for i ,j in rivers.items():
    print(f"{i.title()} run through ,{j}")
    
for key,value in rivers.items():
    print('rivers are ',key)
for river in rivers.keys():
    print(river)









shuld_take_pole=['ron','harry','harmoiney','luci','smith','greg']

for person,lang in favorite_languages.items():
    for i in shuld_take_pole:
        
        if i == person:
            print('you shuld take pooll')

# pizza.py
pizza={
       'crust':'thick',
       'topping':['mushrooms','extre cheese']
       }
print(f"you ordered a {pizza['crust']} -crust pizza"
      "with the following topping:")
for topping in pizza['topping']:
    print(f"\t{topping}")


# favorite_languages.py1


favorite_languages={
    'jen':['python','rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phil':['python','haskell'],
    
    
    }

for name,languages in favorite_languages.items():
    print(f"{name.title()}'s favourate languages are :")
    for language in languages:
        print(f"{language.title()}")



users={
       'aeinstein':{
           'first':'albert',
           'last':'einstein',
           'location':'princeton'
           },
       'mcurie':{
           'first':'marie',
           'last':'curie',
           'location':'paris',
           }
           }
for username,user_info in users.items():
    print(f"\t username: {username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']
    
    print(f"\tFull name :{full_name.title()}")
    print(f"\t location: {location.title()}")





# TRY IT YOURSELF

'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionar-
ies in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.



'''
people = {
    'person1': {
        'name': 'lucifer',
        'series': 'lucifer',
        'age': '666',
        'favorite_number': '6',
        'spouse': 'chloe decker',
        'siblings': ['michel', 'amanadile', 'rere'],
        'offspring': ['rory']
    },
    'person2': {
        'name': 'amanadile',
        'series': 'lucifer',
        'age': '544',
        'favorite_number': 'everything',
        'spouse': 'Dr linda',
        'siblings': ['lucifer', 'rere', 'michel'],
        'offspring': ['charlie']
    },
    'person3': {
        'name': 'michel',
        'series': 'lucifer',
        'age': '666',
        'favorite_number': '999',
        'spouse': 'single',
        'siblings': ['lucifer', 'rere', 'amanadile'],
        'offspring': [None]
    }
}

for person, info in people.items():
    print(f"{person}:")
    for key, value in info.items():
        # if value is a list, join elements with commas
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value if v is not None)
        print(f"  {key}: {value}")
    print()  # blank line after each person





pet1={'kind':'dog','owner':'alice'}
pet2={'kind':'snake','owner':'obonai'}
pet3={'kind':'fish','owner':'kanao'}

pets=[pet1,pet2,pet3]


for pet in pets:
    for key,value in pet.items():
            print(f"{key},{value}")
        




































