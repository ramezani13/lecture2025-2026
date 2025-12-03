#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maryamramezaniziarani
"""
#%% Python’s OS (Operating System) module
import os
print(os.getcwd())
#%% ##reading the data from the file, saving the data to the file
import numpy as np
x = np.array([5, 4, -7, 11])
print(x)
#%%
y = np.array([[4, 5, 0], [3, 7, 9], [2, 1, 2]])
print(y)
#%%
np.savetxt("y_test.txt", y, delimiter=",", header="name,id,region", fmt="%d")
#%%
b = np.genfromtxt('/your_path/testn.txt', delimiter=';')
print(b) 
#%%
b = np.genfromtxt('/your_path/testn.txt', delimiter=';', skip_header=1)
print(b)
#%%
#Exercise1: Create a 2D array and use the np.savetxt() function to save 
#the data array to a text 
#file named "mydata.txt" with a comma delimiter and a header line 
#Col1,Col2,Col3,Col4

data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

np.savetxt("mydata.txt", data, delimiter=",", header="Col1,Col2,Col3,Col4", fmt="%d")

print("Data saved to mydata.txt file.")

#%% ## ploting an array
#%%
import matplotlib.pyplot as plt
#%%
plt.plot(y[1, :]);
#%%
plt.plot(y[:, 1]);
#%% column
plt.plot(y);
#%%
plt.plot(y, color='red');
#%%
#Exercise2: Plot each column of the array as a separat line.
#Assign the following colors to each line: ['red', 'blue', 'green'], 
#using for loop.
#add plt.legend(),plt.title("Plot with Specified Colors"), your legend 
#requires label argument in plot()...

## colors for each line
colors = ['red', 'blue', 'green']

for i in range(y.shape[1]):  ## loop over columns
    plt.plot(y[:, i], color=colors[i], label=f"Column {i}")

plt.legend(title="My Legend", loc= "upper left", frameon=False)
plt.title("Plot with Specified Colors")
plt.show()

#%%
plt.plot(y[:, 0], color='red', label='red')
plt.plot(y[:, 1], color='green', label='green')
plt.plot(y[:, 2], color='blue', label='blue')
plt.legend();
plt.title('Line Plot for Each Column in y')
plt.xlabel('X-axis (Assuming Index)')
plt.ylabel('Y-axis (Values in Each Column)')
#plt.show()
#%%
##Exercise 3:
# Given a 2D list of numbers, extract the diagonal elements and plot 
#them on a graph.

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
##Extract diagonal elements using indexing arr[i][i]
diagonal = []
for i in range(len(arr)):
    diagonal.append(arr[i][i])

print("Diagonal elements:", diagonal)

plt.plot(diagonal, marker='*')
plt.title('Diagonal Elements of the 2D Array')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

#%%
##Histograms
y = np.array([[4, 5, 0], [3, 7, 9], [2, 1, 2]])
h = y.flatten()
print(h)
plt.hist(h);
#%%
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

plt.hist(data, bins=[0,2,4,6,8,10])
plt.title('My Histogram')
plt.xlabel('Interval')
plt.ylabel('Frequency')
#plt.show()
#%%
##Line Plots, mostly for temporal variation

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)
plt.show()
#%%
##linear Regression Fit and trend line

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

##Find the best-fit polynomial of degree 1 (a straight line) for the data
coeficients = np.polyfit(x, y, 1)
print(coeficients)
##It produces the y-values of the line
trend_line = np.polyval(coeficients, x)


## plot the orignal data points
plt.plot(x, y, '*', label='Data Points')


# plot the trend line
plt.plot(x, trend_line, label='Trend Line', color='red')

## add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Trend Line')
plt.legend()

## show the plot
plt.show()
#%% detecting patterns
##Scatter Plots

x = [1, 2, 3, 4]
y = [2, 0, 6, 8]

plt.scatter(x, y)
plt.show()
#%%
##Bar Plots, categorical data

categories = ['A', 'B', 'C']
values = [4, 7, 2]

plt.bar(categories, values)
plt.show()
#%%References
#M.T. Goodrich, R. Tamassia, and M.H. Goldwasser, Data Structures and Algorithms in Python, Wiley, 2013 (“GTG”)
#R. Johansson, Numerical Python: Scientific Computing and Data Science Applications with Numpy, SciPy and Matplotlib, Apress, 2019 (“Joh”)
#J.V. Guttag, Introduction to Computation and Programming Using Python, third edition, The MIT Press, 2021
#https://docs.python.org
#For the assignments associated with this lecture (82-105-DS02, Introduction to Programming);
#M.T. Goodrich, R. Tamassia, and M.H. Goldwasser, Data Structures and Algorithms in Python, Wiley, 2013 (“GTG”)
