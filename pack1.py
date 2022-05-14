# -*- coding: utf-8 -*-
"""
Created on Thu May 12 21:30:23 2022

@author: Anton
"""

x,y,z=2,4,68

if x>y and x>z and x%2==1:
    print("X is the largest Odd")
elif y>x and y>z and y%2==1:
    print("Y is the largest Odd")
elif z>x and z>y and z%2==1:
    print("Z is the largest Odd")
else:
    print("No odds here")
    
    
x=int(input("Enter X: "))  
y=int(input("Enter Y: "))
z=list(range(y))
i=0
ans=1
for i in z:
    ans=ans*x
    i=i+1
    print(ans)
    