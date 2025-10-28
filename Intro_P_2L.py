#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 28 15:18:13 2025

@author: Maryam Ramezani Ziarani
"""
#%%    
# Arithmetic operators
#%%
a = 5
b = 2
addition = a + b
print(a+b)
subtraction = a - b
print(a-b)
multiplication = a * b
print(a*b)
division = a / b 
print(a/b)
remainder = a % b
print(a%b)
exponentiation = a ** b
print(a**b)
#%%
# Comparison operators
#%%
x = 5
y = 10
equals = x == y
not_equals = x != y
greater_than = x > y
less_than = x < y
print(x > y)
#%%
#Conditional Statements
#the code inside runs only if the condition is True
#%%
grade=60
if grade>50:
   print("you pass the test")
#%% else gives an alternative when the condition fail
a=34
if a<20:
    print("you are a winner")
else:
    print("you are a loser")
#%% #IndentationError
grade=60

if grade>50:
print("you pass the test") #this is wrong!!!
#%%
#Excercise1: Given two numbers a and b, write a Python code
#to check if a is divisible by b or not.
#%%
a=10
b=5
if (a % b == 0): 
    print("a is divisible by b") 
else: 
    print("a is not divisible by b")    
#%%
# for and while loops
#%% 
animals = ["dog", "cat", "bird"]
for x in animals:
    print(x)
#%% break
animals = ["dog", "cat", "bird"]
for x in animals:
    print(x)
    if x == "cat":
        break
#%%range(start, stop, step) generates a sequence of numbers
x = range(10, 20)
for n in x:
    print(n)
#%%
x = range(10, 20,2)
for n in x:
    print(n)
#%%
#Exercise2: What numbers between 2 and 30 are even and odd?
#%%
for x in range(2, 30):  
    if x % 2 == 0: 
        print(x, "is a Even Number")
    else: 
        print(x, "is a Odd Number")
#%%
#Exercise3: Write a Python program to find the largest number 
#in a given list of numbers
#%%
arr = [2, 4, 6, 8]
max_num = arr[0]

for num in arr:
    if num > max_num:
        max_num = num
print(max_num)
#%%
#while loop
#%%
i = 1
while i < 11:
    print(i)
    i += 1
#%%
#Exercise4: print out the numbers from 100 to 0 in steps of 10, 
#using while loop
#%%
i = 100
while i >= 0:
    print(i)
    i -= 10
#%%References
#M.T. Goodrich, R. Tamassia, and M.H. Goldwasser, Data Structures and Algorithms in Python, Wiley, 2013 (“GTG”)
#R. Johansson, Numerical Python: Scientific Computing and Data Science Applications with Numpy, SciPy and Matplotlib, Apress, 2019 (“Joh”)
#J.V. Guttag, Introduction to Computation and Programming Using Python, third edition, The MIT Press, 2021
#https://docs.python.org