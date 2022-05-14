# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:34:43 2022

@author: Anton

"""


"""
Finger exercise: Write a program that asks the user to input 10 integers, and then
prints the largest odd number that was entered. If no odd number was entered, it
should print a message to that effect.

"""

UserInput = list(input("Please eneter 10 integers: "))

for i in range(len(UserInput)):
    UserInput[i]=int(UserInput[i])

newList=[]   
    
for item in UserInput:
    if item%2==1:
        newList.append(item)
        
print(max(newList))

"""
Finger exercise: Write a program that asks the user to enter an integer and prints two integers,
root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.
If no such pair of integers exists, it should print a message to that effect.

"""


Number=int(input("Please, enter a number: "))


root=1
pwr=1

while pwr<6 and root<=Number:
    if root**pwr==Number:
        print(root,"**",pwr,"=",root**pwr)
        root=root+1
    elif root**pwr<Number and pwr<5:
        pwr=pwr+1
    else:
        root=root+1
        pwr=1
"""
Finger exercise: Let s be a string that contains a sequence of decimal numbers
separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
sum of the numbers in s.

"""        

s="1.23,2.4,3.123"
Newlist=[]
for i in s:
    if i==",":
        Newlist.append(float(s[0:s.index(",")]))
        s=s[s.index(",")+1:]
    elif s.find(",")==-1:
        Newlist.append(float(s))
        break
print(sum(Newlist))





