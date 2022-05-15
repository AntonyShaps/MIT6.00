# -*- coding: utf-8 -*-
"""
Created on Sun May 15 18:16:36 2022

@author: Anton
"""

"""
Finger exercise: Write a function isIn that accepts two strings as arguments and
returns True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in.
"""

x="xx"
y="ssssd"

def isIn(string1,string2):
    for i in string1:
        for t in string2:
            if i == t:
                print("True")
                return
            else:
                print("False")
                return


