import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#https://www.w3schools.com/python/pandas/ref_df_describe.asp
#import seaborn as sns
import sys
#import csv
#assign columns to iris_data.csv
col=['sepal_length','sepal_width','petal_length','petal_width','type']
#read in iris.csv file
iris=pd.read_csv("iris_data.csv",names=col)


#print initial 5 colums
print(iris.head())
print("*********")
#print column titles
print("columns",iris.columns)
print("*********")
#print count of each type
print("count",iris.type.value_counts())
print("*********")

#print qty rows,columns
print("shape:",iris.shape)
print("*********")
#https://www.w3schools.com/python/pandas/ref_df_describe.asp
print(iris.describe())



#https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# Histogram for Sepal Length

def sepal_lenght():

    plt.figure(figsize = (10, 7))
x = iris.sepal_length
plt.hist(x, color = "blue")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")
#plt.legend()
#plt.savefig('Histogram File')
plt.show() 


#Histogram for Sepal Width
plt.figure(figsize = (10, 7))
x = iris.sepal_width
plt.hist(x,color = "green")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
#plt.legend()
#plt.savefig('Histogram File')
plt.show() 


#Histogram for Petal Length
plt.figure(figsize = (10, 7))
x = iris.petal_length
plt.hist(x,  color = "red")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
#plt.legend()
#plt.savefig('Histogram File')
plt.show() 


#Histogram for Petal Width
plt.figure(figsize = (10, 7))
x = iris.petal_width
plt.hist(x, color = "yellow")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")
#plt.legend()
plt.savefig('Histogram File')
plt.show() 





