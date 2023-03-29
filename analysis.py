import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#https://www.w3schools.com/python/pandas/ref_df_describe.asp
import seaborn as sns
import sys
#import csv
#assign columns to iris_data.csv
col=['sepal_length','sepal_width','petal_length','petal_width','type']
#read in iris.csv file
iris=pd.read_csv("iris_data.csv",names=col)



#https://stackoverflow.com/questions/34926517/stop-sys-stdout-from-writing-to-a-text-file
sys.stdout = open ("summary.txt","w")
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
print("*********")
sys.stdout.close()
#print("summary.txt file is closed")


#https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# Histogram for Sepal Length

#def sepal_lenght_hist():

plt.figure(figsize = (10, 7))
x = iris.sepal_length
plt.hist(x, color = "blue")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal Length cm")
plt.ylabel("Count")
plt.legend("sepal_lenght")
plt.savefig('sepal_lenght_histogram.png')
#plt.show() 


#Histogram for Sepal Width

#def sepal_width_hist():

plt.figure(figsize = (10, 7))
x = iris.sepal_width
plt.hist(x,color = "green")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.legend("Sepal Width")
plt.savefig('sepal_width_histogram.png')
plt.show() 


#Histogram for Petal Length
#def petal_length_hist():

plt.figure(figsize = (10, 7))
x = iris.petal_length
plt.hist(x,color = "red")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
plt.legend("vv",prop={'size': 12})
plt.savefig('petal_length_hist.png')
#plt.show() 


#Histogram for Petal Width
#def petal_width_hist():

plt.figure(figsize = (10, 7))
#x = iris.petal_width
plt.hist(x= iris.petal_width, color = "yellow")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")
plt.legend("Petal Width")
plt.savefig('petal_width_histogram.png')
plt.show() 

#scatterplot Sepal Lenght & Sepal Width
#https://seaborn.pydata.org/generated/seaborn.scatterplot.html
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue = "type",palette = ["green","blue","yellow"])
plt.show()

#scatterplt Petal Lenght & Peal Width
sns.scatterplot(x='petal_length', y='petal_width', data=iris, hue = "type",palette = ["green","blue","yellow"])
plt.show()




'''
#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]

'''