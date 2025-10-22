#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 22 15:12:49 2025

@author: Maryam Ramezani Ziarani
"""

##Variables and data types
#%%
# Numeric int, float
#%%
a=1
type(a)
#%%
b= 2.8
type(2.8)
#%%
# Sequence list, tuple
#%%
type([4, 6, 7])
#%%
type((1, 5))
#%%
# String str
#%%
type("I like Math")
#%%
# Mapping dict
#%%
type({"number of student": 8, "p": 5})
#%%
#set
#%%
type({"number of student", "p"})
#%%
#Boolean 
#%%
print(type(1 == 2))
#%%
c=("I like Math!")
print(c[2])
#%%
#Excercise1: Assign a list to a variable and check the type and 
#print an element using index!
#%%
b=[4,5,8]
type(b)
print(b[2])
#%%
#Excercise2: Assign a float to a variable and use the print() function
#to print out the following sentence "the type of 2.8 is <class 'float'>"
#%%
b= 2.8
print ("the type of", b ,"is", type(b))
#%%
# Identity and Equality
#%%

a = [1, 2, 3]
b = a               ## b is a reference to the same list as a
c = [1, 2, 3]       ## c is a different list with the same values as a

identity_check = print(a is b)    ## true, they reference the same object
equality_check = print(a == c)    ## true, they have the same values

#%%
# Mutable (list, dict, set) vs. Immutable (string, numbers, tuple)
#%%
## Lists are mutable
my_list = [1, 2, 3]
my_list[0] = 4
print(my_list)

## Strings are immutable
my_string = "Hello"
# my_string[0] = 'h'  ## This will raise an error


#%%
#Excercise3: Check this for (dict, set, tuple)
#%%
## Dictionaries are mutable
my_dict = {'name': 'Alice', 'age': 25}
my_dict['age'] = 26
print(my_dict)  

## Sets are mutable
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  

## Tuples are immutable
my_tuple = (1, 2, 3)
my_tuple[0] = 4  
print(my_tuple)
#%%    
#%%References
#M.T. Goodrich, R. Tamassia, and M.H. Goldwasser, Data Structures and Algorithms in Python, Wiley, 2013 (“GTG”)
#R. Johansson, Numerical Python: Scientific Computing and Data Science Applications with Numpy, SciPy and Matplotlib, Apress, 2019 (“Joh”)
#J.V. Guttag, Introduction to Computation and Programming Using Python, third edition, The MIT Press, 2021
#https://docs.python.org