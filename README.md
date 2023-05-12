<p>This repository is used for the project given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.</p>
<p>I have created files in Visual Studio Code, & I have added added comments to explain work, along with references<br>
For this markup sheet, I used the following websites as guides.<br>
#https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
<ol>
<li><a href="#">https://www.markdownguide.org/basic-syntax</a></li>
<li><a href="#">https://www.w3schools.io/file/markdown-cheatsheet/</a></li></p>
</ol>

# **Table of contents**
* [Iris Dataset](Iris-Dataset)
    1. [Introduction](#Introduction)
    2. [About the Dateset](#About-the-Dateset)
    3. [Analysis](#Analysis)
    4. [Histogram](#Histogram)
    5. [Histogram Conclusion](#Histogram-Conclusion)
    6. [Scatter](#Scatter) 
    7. [Scatter plot Conclusion](#Scatter-Plot-Conclusion)
    8. [Box Plots](#BoxPlots)
    9. [Box Plot Conclusion](#Box-Plot-Conclusion)
    10. [Pair Plot ](#PairPlot)
    11. [PairPlotConclusion](#Pair-Plot-Conclusion)
    12. [How to run program](#How-to-run-program)
    13. [Conclusion](#Conclusion)
    14. [Imported Libraries](#Imported-Libraries)

# Introduction #
</p>This project is using the Iris datset and is widely used as an introductory dataset, similar to the "Hello World" program. The dataset has measurements in centimetres for 50 flowers from 3 species. The Species are:</p>
<p>
<li>Iris-setosa</li>
<li>Iris-versicolor</li>
<li>Iris-virginica</li>
<p> <img src = "https://machinelearninghd.com/wp-content/uploads/2021/03/iris-dataset.png"> </p>

<p>The Iris Dataset or Fisher's Iris dataset was introduced in 1936 by Ronald Fisher. It is also known as Anderson's Iris dataset as Edgar Anderson collected the data. From researching this dataset, I found that two out of three species were collected in same Peninsula, and picked on the same day, and also measured at the same time using the same apparatus.</p> 

Ronald Fisher
<p> <img src = "https://www.bing.com/images/search?view=detailV2&ccid=AoMa3Tv3&id=CF9DB76D51C1BBE29AC09AC21A10B2A3C0CC902A&thid=OIP.AoMa3Tv3dAmF5lKNK4XjTQAAAA&mediaurl=https%3a%2f%2fi2.wp.com%2fi.dailymail.co.uk%2f1s%2f2020%2f06%2f10%2f08%2f29411882-8401935-Ronald_Fisher_1890_1962_was_a_mathematician_and_geneticist_who_i-a-45_1591772973607.jpg%3fresize%3d470%252C988%26ssl%3d1&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.02831add3bf7740985e6528d2b85e34d%3frik%3dKpDMwKOyEBrCmg%26pid%3dImgRaw%26r%3d0&exph=988&expw=470&q=ronald+fisher&simid=608036063852193016&FORM=IRPRST&ck=41D972340C5890E2C745214E09AF77D2&selectedIndex=4&ajaxhist=0&ajaxserp=0"> </p>

# About the Dateset # 
<p>I have saved the Iris dataset in this ripository, and and can be viewed in the file called <em>iris_data.csv</em>. This file is read using the following code;</p>
<p>iris=pd.read_csv("iris_data.csv",names=col)</p>
<p>As there are no column names in this dataset, I have asssigned column names using the following;</p>
<p>col=['sepal_length','sepal_width','petal_length','petal_width','type']</p>
<p>The columns in this dataset are as follows</p>
<p>
<li>Petal Lenght</li>
<li>Petal Width</li>
<li>Sepal Length</li>
<li>Sepal Width</li>
<li>Type</li>
</p>
<p>There are 150 samples, with 50 each per flower type. This means that the dataset is balanced.

# Analysis #
<p>The following analysis is performed when program is run, and the output is saved to the following file <em>summary.txt</em>
<li>Sum, Mean & Median of each column</li>
<li>Initial 5 rows using .head() function</li>
<li>Count of each type using .value_counts() function</li>
<li>quantity of columns & rows using .shape() function</li>
</p>
<p>The .describe() function also displays the following information:
<ol>
<li>Count of each column</li>
<li>Mean of each column</li>
<li>Standard Deviation of each colum</li>
<li>min of each colum</li>
<li>25% Percentile</li>
<li>50% Percentile</li>
<li>75% Percentile</li>
<li>max</li>
</ol>
</p>

# Histogram #
<p>The program generates 4 Histograms, for Sepal Lenght, Sepal Width, Petal Lenght & Petal Width. The histograms are displayed and output is saved to individual .png files. These files are as follows:
<li>Sepal_Lenght_histogram.png</li>
<li>Sepal_Width_histogram.png</li>
<li>Petal_Lenght_histogram.png</li>
<li>Petal_Width_histogram.png</li>

# Histogram Conclusion #
<p>Some useful information that can be visualised from these histograms</p>
<li>Petal width of setosa is usually below .5</li>
<li>Petal width of virginica is typically largest of 3 types</li>
<li>Petal Lenght of setosa is between 1 & 2</li>
<li>Sepal width indicates roughly normal distribution between 3.0 & 3.5</li>

# Scatter #
<p>The program generates 4 Scatter plots and the output is saved to individual .png files. These compare the following values
<li>Sepal_Lenght v Sepal Width</li>
<li>Sepal_Lenght v Petal Length</li>>
<li>Sepal_Lenght v Petal Width</li>
<li>Sepal_Lenght v Petal Width</li>

</p>

# Scatter plot Conclusion #
<p>The following information can be gleaned from these scatter plots</p>

<li>No strong relationship between Sepal lenght and Sepal Width</li>
<li>As Sepal lenght increases, petal lenght also tends to increase</li>
<li>As Petal lenght increases, petal width also tends to increase</li>
<li>As Petal lenght increases, sepal width tends to derease</li>

# Box Plots #
<p>The program generates 4 Box plots, for Sepal Lenght,Seapl Width,Petal Lenght & Petal Width. The box plots are displayed and output is saved to individual .png files. These files are as follows:
<li>Sepal_Lenght_box.png</li>
<li>Sepal_Width_box.png</li>
<li>Petal_Lenght_box.png</li>
<li>Petal_Width_box.png</li>

 # Box Plot Conclusion</H1>
<p>The following information can be gleaned from these box plots</p>
<p>
<li>The range of sepal lenghts is widest for iris Virginica & smallest for iris Setosa</li>
<li>The range of sepal widths is widest for iris Setosa & smallest for iris Virginica</li>
<li>The range of petal lenghts is widest for iris Virginica & smallest for iris Setosa </li>
<li>The range of petal widths is widest for iris Virginica & smallest for iris Setosa </li></p>
<p>Iris Setosa generally has the smallest measurements compared to other two species.</p>

# Pair Plot #

<p>The program generates a Pair plot, for Sepal Lenght,Seapl Width,Petal Lenght & Petal Width. The pair plot allows easy visualisation of the relationships between pairs of variables. The output of the pairplot is saved in a .png file called pairplot.png</p>

# Pair Plot Conclusion #
<li>Setosa normally has shorter Sepal Lenght and wider Sepal width compared to other species</li>
<li>As Sepal lenght increases, the Petal lenght tends to increase also</li>
<li>As Sepal lenght increases, petal widths tends to increase also </li>
<li>As Petal lenght increases, petal width tends to increase</li>

# Conclusion #
<p>The Iris dataset is well documented and consists of measurements of Sepal Lenght,Seapl Width,Petal Lenght & Petal Width for three different species;</p>
<p>
<li>Iris-setosa</li>
<li>Iris-versicolor</li>
<li>Iris-virginica</li>
</p> 
<p>The following conlusions are the most interesting I have found over the course of this prohect</p>
<p>
<ol>
<li>The Petal measurements are typically more useful in identifying species compared to sepal measurements</li>
<li>The Setosa species is easiest to identify due to smaller size</li>
<li>The Versicolr & Virginica species are hardest to identify</li> 
</ol>
</p>


# How to run program #
<ol>
<li>$ python analysis</li>
<li>individual images open. Close each image after viewing by clicking "x" on image</li> 
<li>.png & .txt files have been updated</li> 
</ol>


# Imported Libraries #

<ol>
<li>import numpy as np</li>
<p> NumPy is short for "Numerical Python". It allows for matematical and logical operations on arrays efficiently. NumPy also enables user to reshape,slice ,stack and join arrays. Broadcasting is a powerful NumPy feature that that allows arithmetic operations between arrays with different sizes.</p>
<li>import pandas as pd</li>
<p>Pandas is an open source Python library that provides high performance data manipulation tools and analysis tools. It also allows for reading and writing from various file formats, such as .csv. Pandas has functions for analyzing, cleaning , exploring and manipulating data</p>
<li>import matplotlib.pyplot as plt</li>
<p>Matplotlib is a low level graph plotting library in python. It is open source. Using Mathplotlib, different types of plots can be created, such as scatter plots, histograms,box plots etc.</p>
<li>import seaborn as sns</li>
<p>Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.It is designed to work well with dataframes from Pandas
<li>import sys</li>
<p>sys is a built in module in Python that allows access to common functions and variables that are used to manipulate different parts of the Python runtime environment. A common use are is sys.argv which takes input from user and this input is then used in program</p>
</ol>

# References # 
<ol>
<li><a href="#">https://www.kaggle.com/datasets/vikrishnan/iris-dataset</a></li>
<li><a href="#">https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data</a></li>
<li><a hef ="#">https://medium.com/@naidubhavya06/detailed-explanation-of-exploratory-data-analysis-using-iris-dataset-fa8082a4ce0f</a></li>
<li><a hef ="#">https://www.markdownguide.org/basic-syntax</a></li>
<li><a hef ="#">https://stackoverflow.com/questions/34926517/stop-sys-stdout-from-writing-to-a-text-file</a></li>
<li><a hef ="#">https://www.w3schools.com/python/pandas/ref_df_describe.asp</a></li>
<li><a hef ="#"></a>https://www.bing.com/videos/search?q=histograms+iris+data+set+different+colours+python&qpvt=histograms+iris+data+set+different+colours+python&view=detail&mid=A11A51CDECB7554E9784A11A51CDECB7554E9784&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dhistograms%2Biris%2Bdata%2Bset%2Bdifferent%2Bcolours%2Bpython%26qpvt%3Dhistograms%2Biris%2Bdata%2Bset%2Bdifferent%2Bcolours%2Bpython%26FORM%3DVDRE</li>
<li><a hef ="#">https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/</a></li>
<li><a hef ="#">https://stackoverflow.com/questions/43872450/matplotlib-histogram-with-multiple-legend-entries</a></li>
<li><a hef ="#">https://www.statology.org/matplotlib-boxplot-by-group/</a></li>
<li><a hef ="#">https://seaborn.pydata.org/generated/seaborn.scatterplot.html</a></li>
<li><a hef ="#">https://www.youtube.com/watch?v=b7JuBsswDlo</a></li>
<li><a hef ="#">https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d</a></li>
<li><a hef ="#"></a>https://www.w3schools.com/python/pandas/ref_df_describe.asp</li>
<li><a hef ="#"></a>histograms & box plots @ https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/</li>
<li><a hef ="#"></a>adding legend https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/</li>
<li><a hef ="#"></a>https://numpy.org/doc/stable/user/whatisnumpy.html</li>
<li><a hef ="#"></a>https://www.w3schools.com/python/pandas/pandas_intro.asp</li>
<li><a hef ="#"></a>https://www.w3schools.com/python/seaborn_intro.asp</li>
<li><a hef ="#"></a>https://seaborn.pydata.org/</li>
<li><a hef ="#"></a>https://www.geeksforgeeks.org/python-sys-module/</li>
<li><a hef ="#"></a>https://www.geeksforgeeks.org/python-sys-module/</li>
<li><a hef ="#"></a></li>
</ol>
