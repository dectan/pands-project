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
#info for histograms
iris_s = iris[iris.type == "Iris-setosa"]
iris_vers = iris[iris.type == "Iris-versicolor"]
iris_virg = iris[iris.type == "Iris-virginica"]

#https://stackoverflow.com/questions/34926517/stop-sys-stdout-from-writing-to-a-text-file
def write_to_file():
    print("******************")
    sys.stdout = open ("summary.txt","w")
    #calculate sum/mean/median of sepal length
    print("******************")
    sum_data = iris['sepal_length'].sum()
    mean_data = iris["sepal_length"].mean()
    median_data = iris["sepal_length"].median()
    print("Sum of sepal length:",sum_data, "\nMean of sepal length:", mean_data, "\nMedian of sepal length:",median_data)
    print("******************")
    #calculate sum/mean/median of sepal width
    sum_data = iris['sepal_width'].sum()
    mean_data = iris["sepal_width"].mean()
    median_data = iris["sepal_width"].median()
    print("Sum of sepal width:",sum_data, "\nMean of sepal width:", mean_data, "\nMedian of sepal width:",median_data)
    print("******************")
    #calculate sum/mean/median of petal length
    sum_data = iris['petal_length'].sum()
    mean_data = iris["petal_length"].mean()
    median_data = iris["petal_length"].median()
    print("Sum of petal length:",sum_data, "\nMean of petal length:", mean_data, "\nMedian of petal length:",median_data)
    print("******************")
    #calculate sum/mean/median of petal width
    sum_data = iris['petal_width'].sum()
    mean_data = iris["petal_width"].mean()
    median_data = iris["petal_width"].median()
    print("Sum of petal width:",sum_data, "\nMean of petal width:", mean_data, "\nMedian of petal width:",median_data)
    print("******************")
    print("Initial 5 Rows")
    print(iris.head())
    print("******************")
    print("columns in this table are",iris.columns)
    print("******************")
    print("count of each type is\n",iris.type.value_counts())
    print("******************")
    print("shape of this table is :",iris.shape)
    print("******************")
#https://www.w3schools.com/python/pandas/ref_df_describe.asp
    print(iris.describe())
    print("******************")
    sys.stdout.close()

#https://www.bing.com/videos/search?q=histograms+iris+data+set+different+colours+python&qpvt=histograms+iris+data+set+different+colours+python&view=detail&mid=A11A51CDECB7554E9784A11A51CDECB7554E9784&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dhistograms%2Biris%2Bdata%2Bset%2Bdifferent%2Bcolours%2Bpython%26qpvt%3Dhistograms%2Biris%2Bdata%2Bset%2Bdifferent%2Bcolours%2Bpython%26FORM%3DVDRE
#https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# Histogram for Sepal Length
#fix legend issus @https://stackoverflow.com/questions/43872450/matplotlib-histogram-with-multiple-legend-entries

def hist():
    sepal_length_hist()
    sepal_width_hist()
    petal_length_hist()
    petal_width_hist()
    return

def box():
    sepal_length_box()
    sepal_width_box()
    petal_length_box()
    petal_width_box()
    return

#https://www.statology.org/matplotlib-boxplot-by-group/
def sepal_length_box():
    sns.set(style='whitegrid') # set style of the plot
# create box plot
    sns.boxplot(x='type', y='sepal_length', data=iris)
    plt.savefig("sepal_length_box.png")
    plt.show()
    return
def sepal_width_box():
    sns.set(style='whitegrid') # set style of the plot
# create box plot
    sns.boxplot(x='type', y='sepal_width', data=iris)
    plt.savefig("sepal_width_box.png")
    plt.show()
    return
def petal_length_box():
    sns.set(style='whitegrid') # set style of the plot
# create box plot
    sns.boxplot(x='type', y='petal_length', data=iris)
    plt.savefig("petal_length_box.png")
    plt.show()
    return
def petal_width_box():
    sns.set(style='whitegrid') # set style of the plot
# create box plot
    sns.boxplot(x='type', y='petal_width', data=iris)
    plt.savefig("petal_width_box.png")
    plt.show()
    return
#scatterplot Sepal Length & Sepal Width
#https://seaborn.pydata.org/generated/seaborn.scatterplot.html

def scatter_sep_len_v_wid():
    sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue = "type",palette = ["green","blue","yellow"])
    plt.title('Sepal Length v. Sepal Width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    plt.savefig("sepal_length_v_sepal_width_scatter.png")
    plt.show()

def scatter_sep_len_v_pet_len():
    sns.scatterplot(x='sepal_length', y='petal_length', data=iris, hue = "type",palette = ["green","blue","yellow"])
    plt.title('Sepal Length v. Petal_Length')
    plt.xlabel('sepal_length')
    plt.ylabel('petal_length')
    plt.savefig("Sepal Length v. Petal_Length_scatter.png")
    plt.show()

#scatterplt sepal_length & petal_length
def scatter_sep_len_v_pet_wid():
    sns.scatterplot(x='sepal_length', y='petal_width', data=iris, hue = "type",palette = ["green","blue","yellow"])
    plt.title('Sepal Length v. Petal width')
    plt.xlabel('sepal_length')
    plt.ylabel('petal_width')
    plt.savefig("sepal_length_v_petal_width_scatter.png")
    plt.show()

#scatterplt sepal_width & petal_width
def scatter_sep_wid_v_pet_length():
    sns.scatterplot(x='sepal_width', y='petal_length', data=iris, hue = "type",palette = ["green","blue","yellow"])
    plt.title('sepal_width v petal_length')
    plt.xlabel('sepal_width')
    plt.ylabel('petal_length')
    plt.savefig("sepal_width_v_petal_length_scatter.png")
    plt.show()
    #print("programme running")

def scatter():
    scatter_sep_len_v_wid() 
    scatter_sep_len_v_pet_len() 
    scatter_sep_len_v_pet_wid() 
    scatter_sep_wid_v_pet_length()

def sepal_length_hist():
    plt.figure(figsize = (10,10))
    iris_s = iris[iris.type == "Iris-setosa"]
    iris_vers = iris[iris.type == "Iris-versicolor"]
    iris_virg = iris[iris.type == "Iris-virginica"]  
    plt.hist(iris_s["sepal_length"],  label = "Iris setosa", color = "black",alpha=1)
    plt.hist(iris_vers["sepal_length"],  label = "Iris versicolor", color = "blue",alpha=.5)
    plt.hist(iris_virg["sepal_length"],  label = "Iris virginica", color = "yellow",alpha=.6)
    plt.title("Sepal Length in cm")
    plt.xlabel("Sepal Length cm")
    plt.ylabel("Count")
    plt.legend(["Iris setosa","Iris versicolor","Iris virginica"])
    plt.savefig("sepal_length_histogram.png")
    plt.show()
    
#Histogram for Sepal Width
def sepal_width_hist():
    plt.figure(figsize = (10,10))
    plt.hist(iris_s["sepal_width"],label = "Iris setosa", color = "black",alpha=1)
    plt.hist(iris_vers["sepal_width"],label = "Iris versicolor", color = "blue",alpha=.5)
    plt.hist(iris_virg["sepal_width"],label = "Iris virginica", color = "yellow",alpha=.6)
    plt.title("Sepal Width in cm")
    plt.xlabel("Sepal_Width_cm")
    plt.ylabel("Count")
    plt.legend(["Iris setosa","Iris versicolor","Iris virginica"])
    plt.savefig('sepal_width_histogram.png')
    plt.show()
    
#Histogram for Petal Length
def petal_length_hist():
    plt.figure(figsize = (10,10))
    plt.hist(iris_s["petal_length"],  label = "Iris setosa", color = "black",alpha=1)
    plt.hist(iris_vers["petal_length"],  label = "Iris versicolor", color = "blue",alpha =.5)
    plt.hist(iris_virg["petal_length"],  label = "Iris virginica", color = "yellow",alpha=.6)
    plt.title("Petal Length in cm")
    plt.xlabel("Petal_Length_cm")
    plt.ylabel("Count")
    plt.legend(["Iris setosa","Iris versicolor","Iris virginica"])
    plt.savefig("petal_length_histogram.png")
    plt.show()  
    
#Histogram for Petal Width
def petal_width_hist():  
    plt.figure(figsize = (9,9))  
    plt.hist(iris_s["petal_width"],  label = "Iris setosa", color = "black",alpha=1)
    plt.hist(iris_vers["petal_width"],  label = "Iris versicolor", color = "blue",alpha=.5)
    plt.hist(iris_virg["petal_width"],  label = "Iris virginica", color = "yellow",alpha=.6)
    plt.title("Petal Width in cm")
    plt.xlabel("Petal_Width_cm")
    plt.ylabel("Count")
    plt.legend(["Iris setosa","Iris versicolor","Iris virginica"])
    plt.savefig('petal_width_histogram.png')
    plt.show()

#https://www.youtube.com/watch?v=b7JuBsswDlo
def pair_plot():
    plt.figure(figsize = (9,9)) 
    sns.set(style="whitegrid")
    sns.pairplot(iris, hue="type",height = 3)
    plt.savefig("pairplot.png")
    plt.show()
def main():                    
            hist()
            scatter()
            box()
            pair_plot()
            write_to_file()            

if __name__ == "__main__":
    main()
#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
