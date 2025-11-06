#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 13:34:11 2025

@author: maryamramezaniziarani
"""
#%%
## Def function
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_numbers(3, 5))
#%%
#Exercise1: what is the area of a rectangle with a length of 2 and a 
#width of 4? (use def function)
#%%
def area_of_rectangle(length, width):
    area = length * width
    return area
print(area_of_rectangle(2, 4))
#%%This function checks a condition (n > 0) and then returns either
#True or False based on that condition
def is_positive(n):
    if n > 0:
        return True
    else:
        return False
#%% ###lecture on 4th and 5th of November (lecture3)
#Data structures in Python; Lists, Tuples, Dictionaries
#goal; work with collections in depth (building on Lectures 1 and 2)
#%%
##LISTS
#   - Indexing and slicing
#   - insert,append,extend,remove,pop
#   - sort,reverse
#   - copy vs reference
#   - enumerate for indexed loops
#   - nested lists
#   - list comprehension
#%%
nums = [10, 20, 30, 40, 50]
print("nums:", nums)

##Indexing and slicing
print("first/last:", nums[0], nums[-1])
print("slice 1..3:", nums[1:4])
print("prefix:", nums[:3], "| suffix:", nums[3:])
#%%
#Exercise 2: Indexing and Slicing
##given the list:
nums = [10, 20, 30, 40, 50]

##1)Print the second and fourt elements
##2)Print a slice containing the middle three numbers
##3)Print the first two numbers using slicing
##4)Print the last two numbers using slicing

print(nums[1], nums[3])        # second and fourth
print(nums[1:4])               # middle three
print(nums[:2])                # first two
print(nums[-2:])               # last two
#%% append/insert/extend
nums.append(60)
nums.insert(1, 15)               
nums.extend([70, 80])            
print("after append/insert/extend:", nums)
#%%
#Exercise 3: append(),insert(),extend()
#given the list:
numbers = [5, 10, 15]

##1) Append the number 20 to the end of the list
##2) Insert the number 0 at the beginning of the list
##3) Extend the list by adding [25, 30] at the end
##4) Print the final list

numbers.append(20)
numbers.insert(0, 0)
numbers.extend([25, 30])
print("Final list:", numbers)
#%% remove/pop(by value vs by index)
nums.remove(30)                  ##remove first occurrence of 30
popped_last = nums.pop()         ##remove the last item
popped_idx2 = nums.pop(2)        ##remove the item at index 2
print("after remove/pop:", nums)
print("popped (last, idx2):", popped_last, popped_idx2)
#%%
#Exercise 4:remove() and pop()
##given the list:
values = [100, 200, 300, 400, 500, 300]

##1) Remove all the 300s
##2) Pop the last element and store it in a variable called 
#last_item
##3) Pop the element at index 1 and store it in a variable 
#called second_item
##4) Print the modified list and both popped item

while 300 in values:      
    values.remove(300)    

last_item = values.pop()
second_item = values.pop(1)
print("Updated list:", values)
print("Popped items -> last:", last_item, "| index 1:", second_item)
#%%sort/reverse
scores = [42, 5, 17, 17, 100, 3, 4]
scores.sort()                    # ascending
print("sorted asc:", scores)
scores.sort(reverse=True)        # descending
print("sorted desc:", scores)
scores.reverse()                 # simple reversal
print("reversed:", scores)
#%%
# copy vs reference
a = [1, 2, 3]
b = a                 # reference (same object)
c = a.copy()          # shallow copy (new object)
a[0] = 99
print("a:", a, "| b (same object):", b, "| c (copy):", c)
#%% enumerate for indexed loop
##enumerate()lets you get both the index number(i) and the value (color) at the same time
colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print("index", i, "->", color)
#%%
#Exercise 5: using enumerate()
##given the list:
animals = ["dog", "cat", "bird", "fish"]

##Use a for loop with enumerate() to print both the index and the 
#animal name
##Print only the animals at even index positions (0,2, ...)

for i, animal in enumerate(animals):
    if i % 2 == 0:
        print(f"Even index {i}: {animal}")
        #print("Even index", i, ":", animal)       
#%%
##nested lists
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print("grid[2][1]:", grid[2][1])
print(f"grid[2][1]: {grid[2][1]}")
#%%list comprehension# A list comprehension is a short, Pythonic way to 
#create a new list by looping over an iterable 
#and optionally filtering items,all in a single line
squares = [n*n for n in range(1, 6)]
evens = [n for n in range(1, 11) if n % 2 == 0]
print("squares:", squares)
print("evens:", evens)

#short exercise:Use a for loop and an if statement to check if a number 
#is even in range (1,11)
    
even = []                 
for n in range(1, 11):
    if n % 2 == 0:      
        even.append(n)   
print(even)
#%%
##Exercise 6: 
##Using list comprehension, make a list of all numbers from 1 to 20 that 
#are divisible by 3.
##Create another list with the squares of numbers from 1 to 10.

div_by_3 = [n for n in range(1, 21) if n % 3 == 0]
print("Numbers divisible by 3:", div_by_3)

squares = [n**2 for n in range(1, 11)]
print("Squares from 1–10:", squares)
#%%TUPLES
##   - packing/unpacking “Packing puts many values into one variable (a tuple).
#                        Unpacking splits them back out into separate variables.”
##   - tuples as dict keys

## Packing
student = "Ali", 20, "AS"     # pack values into a tuple
print(student)

## Unpacking
name, age, major = student
print("Name:", name)
print("Age:", age)
print("Major:", major)
#%%
## tuples can be dict keys (lists cannot)
distances = {
    ("Paris", "London"): 343,
    ("Rome", "Milan"): 572
}
print("distance Paris->London:", distances[("Paris", "London")])
#%%
# Exercise 7: Tuples as Dictionary Keys
## 1) Create a dictionary named 'temperatures' where:
## - The key is a tuple representing a city and month, 
#e.g.("Paris", "July")
## - The value is the average temperature in Celsius.
## 2) Add at least two entries, then print one value using 
#its tuple key.


temperatures = {
    ("Paris", "July"): 25,
    ("London", "March"): 10
}
print("Paris in July:", temperatures[("Paris", "July")])
#%%DICTIONARIES
##  - create,add/update
##  - get() with default
##  - keys(), values(), items()
##  - looping over items
##  - nested dictionaries
##  - dict comprehension

student = {"name": "Ali", "age": 20, "grade": 90}
print("student:", student)
print("student['name']:", student["name"])
#%%
##add/update 
student["major"] = "AS"          # add
student["grade"] = 95            # update
print("updated student:", student)
#%%
#get() with default, Returns value for key
print("student.get('gpa'):", student.get("gpa"))              ## None
#print("student.get('gpa'):", student["gpa"])
print("student.get('gpa', 0.0):", student.get("gpa", 0.0))    ## default 0.0
#%%
# keys/values/items
print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:", list(student.items()))
#%%
##loop over items
for key, value in student.items():
    print(key, "->", value)
#%%
## nested dictionaries
classroom = {
    "A001": {"name": "Sara", "scores": [18, 19, 17]},
    "A002": {"name": "Reza", "scores": [15, 16, 14]},
}
print("classroom['A001']['scores']:", classroom["A001"]["scores"])
#%%
# dict comprehension, creating a dictionary
names2 = ["ali", "sara", "john"]
length_map = {name: len(name) for name in names2}
print("length_map:", length_map)
#%%
# EXERCISE 8:
##1) Build a dict for a book with keys: 'title', 'author', 'year'.
##    Add a new key 'pages', then update 'year'. Print the dict.
## 2) Given prices = {"apple": 2, "banana": 1, "cherry": 3},
##    print each item as "apple -> 2$" using a loop.
## 3) Create a dict 'grades' mapping student names to lists of 
#scores.
##    Print each student's average with two decimals. you can use
#sum(), 
#len() functions

book = {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008}
book["pages"] = 464
book["year"] = 2009
print("book:", book)

prices = {"apple": 2, "banana": 1, "cherry": 3}
for key, price in prices.items():
    print(key, "->", f"{price}$")
    print(f"{key} -> {price}$")

grades = {
    "Ali": [18, 17, 19],
    "Sara": [20, 19, 18],
    "John": [14, 15, 16],
}
for name, scores in grades.items():
    avg = sum(scores) / len(scores)
    print(name, "average:", f"{avg:.2f}")
#%%References
#M.T. Goodrich, R. Tamassia, and M.H. Goldwasser, Data Structures and Algorithms in Python, Wiley, 2013 (“GTG”)
#R. Johansson, Numerical Python: Scientific Computing and Data Science Applications with Numpy, SciPy and Matplotlib, Apress, 2019 (“Joh”)
#J.V. Guttag, Introduction to Computation and Programming Using Python, third edition, The MIT Press, 2021
#https://docs.python.org