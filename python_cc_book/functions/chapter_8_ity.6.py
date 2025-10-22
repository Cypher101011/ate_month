#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 11:55:20 2025

@author: a
"""

# try it yourself

def city_country(city,country):
    formated=f'{city.title()} is located in {country.title()}'
    return formated

city_country('chennai', 'india')

def make_album(artist_name,album_title,optional=None):
    album={'artist':artist_name,'title':album_title,'optional':optional}
    return album
print(make_album('mazekine','rock','top of demons'))
    

while True:
    
    x=input("enter q for quit")=='q'
    if x =='q':break 
    artist=input("e\nter artis name")
    title=input('enter album title')
    
    print(make_album(artist,title))

    
