#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 14:58:39 2025

@author: maryamramezaniziarani
"""
#%% Boolean Indexing
import numpy as np

## students scores
scores = np.array([85, 60, 95, 45, 70])

## boolean list 
pass_fail = [True, False, True, False, True]

## boolean indexing 
passed_scores = scores[pass_fail]

print("Original scores:", scores)
print("Pass/Fail filter:", pass_fail)
print("Scores of students Who pased:", passed_scores)
#%%
# Exercise1: Given a numpy array numbers with the values 
#[10, 15, 20, 25, 30, 35, 42], 
#write a code to mask out only the elements that are divisible by 5. 
#Use list Comprehension
#or
#Use a for loop to create a boolean mask list named is_divisible_by_5, 
#and then 
#use that mask to create a new array named masked_numbers.

numbers = np.array([10, 15, 20, 25, 30, 35, 42])

## create the boolean mask using list comprehension
is_divisible_by_5 = [number % 5 == 0 for number in numbers]
print(is_divisible_by_5)

## using the boolean mask to filter the numbers
masked_numbers = numbers[is_divisible_by_5]

print("Boolean filter array:", is_divisible_by_5)
print("Filtered numbers array:", masked_numbers)
#%%
numbers = np.array([10, 15, 20, 25, 30, 35, 42])

is_divisible_by_5 = []

for number in numbers:
    ## If the number is divisible by 5, the value is True, otherwise False
    if number % 5 == 0:
        is_divisible_by_5.append(True)
    else:
        is_divisible_by_5.append(False)

masked_numbers = numbers[is_divisible_by_5]

print("Boolean filter array:", is_divisible_by_5)
print("Filtered numbers array:", masked_numbers)
#%% #complex Boolean masks using element-wise logical operators

#& (AND): both conditions are true 
#| (OR): at least a condition is true, OR results in True
#~ (NOT): negates the condition
#Rules for Using Logical Operators:
#Parentheses are required around each condition because logical 
#operators have a lower precedence than comparison operators
#The conditions are applied element-wise to the array
#%%
import numpy as np

x = np.array([5, 11, 15, 20, 25])
mask = (x > 11) & (x < 25)  ## Select elements between 11 and 25

print (mask)
print(x[mask])

mask = (x == 11) | (x == 25) ## Select elements equal to 10 or 25
print(x[mask]) 

mask = ~(x > 15)  ## Select elements less than or equal to 15
print(x[mask])
#%%
#Exercise 2: given a numpy array scores representing test scores, 
#create a new array that includes:

#Scores greater than 80 AND less than 90, OR Scores equal to 100 
#and set all other scores to 0 in the original array.

#scores = np.array([50, 85, 95, 100, 80, 89, 90])


scores = np.array([50, 85, 95, 100, 80, 89, 90])

## Logical condition: greater than 80 and less than 90, or equal to 100
mask = ~(((scores > 80) & (scores < 90)) | (scores == 100))

## Set all scores that match the mask to 0
scores[mask] = 0

print(scores) 
#%%
##Array summarizing, vectorizing (paused)
#%%References
#M.T. Goodrich, R. Tamassia, and M.H. Goldwasser, Data Structures and Algorithms in Python, Wiley, 2013 (“GTG”)
#R. Johansson, Numerical Python: Scientific Computing and Data Science Applications with Numpy, SciPy and Matplotlib, Apress, 2019 (“Joh”)
#J.V. Guttag, Introduction to Computation and Programming Using Python, third edition, The MIT Press, 2021
#https://docs.python.org