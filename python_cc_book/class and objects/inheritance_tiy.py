#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 10:06:32 2025

@author: a
"""

# try it yourself 9.69
from class_objects import Restaurant as RS
from class_objects import User as User

class IceCreamStand(RS):
    def __init__(self,flavors_list):
     
         self.flavors_list=flavors_list
    def display_flavours(self):
        for flavour in self.flavors_list:
            print(flavour)

icecream1 = IceCreamStand(['vanilla', 'chocolate', 'strawberry'])
icecream1.display_flavours()


class Privileaes:
    def __init__(self,prv):
        self.prv=prv
    def show_privelages(self):
        for privelage in self.prv:
                print(f"this is user who {privelage}")
    

# try it yourself 9.7 Admin
class Admin(User):
    def __init__(self,privileages):
        super().__init__()
        self.privelages=Privileaes(privileages)
admin=Admin(['can add post','can delete post','can ban user'])
admin.privelages.show_privelages()
