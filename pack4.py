# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:07:35 2022

@author: Anton

"""
"""
Finger exercise: Implement a function that meets the specification below. Use a
try-except block.
def sumDigits(s):
Assumes s is a string
Returns the sum of the decimal digits in s
For example, if s is 'a2b3c' it returns 5
"""



s="as2dd2"


def sumDigits(s):
    newlist=[]
    for i in s:
        try:
            newlist.append(int(i))
        except ValueError:
            None
    return sum(newlist)

"""

Finger Exercise: Implement a function that satisfies the specification
def findAnEven(L):
Assumes L is a list of integers
Returns the first even number in L
Raises ValueError if L does not contain an even number
"""


f=[1,3,1,3,5,7]

def findAnEven (l):
    for i in l:
        if i%2==0:
            print(i)
            break
        else:
            raise ValueError("No even number")

































