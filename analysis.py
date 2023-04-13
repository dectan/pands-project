import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#https://www.w3schools.com/python/pandas/ref_df_describe.asp
#histograms & box plots @ https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
#adding legend https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
import seaborn as sns
import sys
#import csv
#assign column names to iris_data.csv
col=['sepal_length','sepal_width','petal_length','petal_width','type']
#read in iris.csv file
iris=pd.read_csv("iris_data.csv",names=col)

#https://stackoverflow.com/questions/34926517/stop-sys-stdout-from-writing-to-a-text-file
def write_to_file():
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

def sepal_lenght_hist():
    plt.figure(figsize = (10, 7))
    x = iris.sepal_length
    plt.hist(x, bins=20,color = "blue")
    plt.title("Sepal Length in cm")
    plt.xlabel("Sepal Length cm")
    plt.ylabel("Count")
    plt.legend(['sepal_lenght'])
    plt.savefig('sepal_lenght_histogram.png')
    #plt.show()
    return

#Histogram for Sepal Width
def sepal_width_hist():
    plt.figure(figsize = (10, 7))
    x = iris.sepal_width
    plt.hist(x,bins=20,color = "green")
    plt.title("Sepal Width in cm")
    plt.xlabel("Sepal_Width_cm")
    plt.ylabel("Count")
    plt.legend(['Sepal_Width'])
    plt.savefig('sepal_width_histogram.png')
    #plt.show()
    return

#Histogram for Petal Length
def petal_length_hist():
    plt.figure(figsize = (10, 7))
    x = iris.petal_length
    plt.hist(x,bins=20,color = "red")
    plt.title("Petal Length in cm")
    plt.xlabel("Petal_Length_cm")
    plt.ylabel("Count")
    plt.legend(['Petal_length'])
    plt.savefig('petal_length_hist.png')
    #plt.show()
    return

#Histogram for Petal Width
def petal_width_hist():
    plt.figure(figsize = (10, 7))
    x = iris.petal_width
    plt.hist(x, bins=20, color = "yellow")
    plt.title("Petal Width in cm")
    plt.xlabel("Petal_Width_cm")
    plt.ylabel("Count")
    plt.legend(['Petal_Width'])
    plt.savefig('petal_width_histogram.png')
    #plt.show()
    return
    

#scatterplot Sepal Lenght & Sepal Width
#https://seaborn.pydata.org/generated/seaborn.scatterplot.html

def scatter_sep_len_v_wid():
    sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue = "type",palette = ["green","blue","yellow"])
    plt.title('Sepal Lenght v. Sepal Width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    #plt.show()
    return

#scatterplt sepal_length & petal_length
def scatter_sep_len_v_pet_wid():
    sns.scatterplot(x='sepal_length', y='petal_length', data=iris, hue = "type",palette = ["green","blue","yellow"])
    plt.title('Sepal Lenght v. Petal Lenght')
    plt.xlabel('sepal_length')
    plt.ylabel('petal_length')
    #plt.show()
    return

#scatterplt sepal_width & petal_width
def scatter_sep_wid_v_pet_wid():
    sns.scatterplot(x='sepal_width', y='petal_width', data=iris, hue = "type",palette = ["green","blue","yellow"])
    plt.title('sepal_width v petal_width')
    plt.xlabel('sepal_width')
    plt.ylabel('petal_width')
    #plt.show()
    #print("programme running")
    return

def main():
    try:
        user_input = str(input("Run Program?"))
        if (user_input == "y" or user_input == "Y"):
            print("program running")
            write_to_file()
            sepal_lenght_hist()
            sepal_width_hist()
            petal_length_hist()
            petal_width_hist()
            scatter_sep_len_v_wid()
            scatter_sep_len_v_pet_wid()
            scatter_sep_wid_v_pet_wid()
            write_to_file()
            
        else:
            print("Program only runs when y/Y is entered")
            

    except ValueError as e:
            print(f"Error:",e)


main()
#print("programme running")
#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
#iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
#iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
#iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]
