<p>This repository is used for the project given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.</p>
<p>I have created files in Visual Studio Code, & I have added added comments to explain work, along with references<br>
For this markup sheet, I used the following websites as guides.<br>
#https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
<ol>
<li><a href="#">https://www.markdownguide.org/basic-syntax</a></li>
<li><a href="#">https://www.w3schools.io/file/markdown-cheatsheet/</a></li></p>
</ol>

# **Table of contents**
* [Iris Dataset](Iris Dataset)
    1. [Introduction](#Introduction)
    2. [Analysis](#Analysis)
    3. [Histogram](#Histogram)
    4. [Histogram Conclusion](#Histogram Conclusion)
    5. [Scatter](#Scatter) 
    6. [Scatter plot Conclusion](#ScatterplotConclusion)
    7. [Box Plots](#BoxPlots)
    8. [Box Plot Conclusion](#BoxPlotConclusion)
    9. [Pair Plot ](#PairPlot)
    10. [PairPlotConclusion](#PairPlotConclusion)
    11. [How to run program](#How to run program)
    11. [Conclusion](#Conclusion)

# Introduction #
</p>This project is using the Iris datset and is widely used as introductory dataset, similar to the "Hello World" program. The dataset has measurements in centimetres for 50 flowers from 3 species. The Species are:</p>
<p>
<li>Iris-setosa</li>
<li>Iris-versicolor</li>
<li>Iris-virginica</li>
<p> <img src = "https://machinelearninghd.com/wp-content/uploads/2021/03/iris-dataset.png"></p>

</p>
<p>I have imported this dataset, and is saved in a file called <em>iris_data.csv</em>The columns in this dataset are as follows</p>
<p>
<li>Petal Lenght</li>
<li>Petal Width</li>
<li>Sepal Length</li>
<li>Sepal Width</li>
<li>Type</li>
</p>

# Analysis #

<p>The following analysis is performed when program is run, and the output is saved to the following file <em>summary.txt</em>
<li>Sum, Mean & Median of each column</li>
<li>Initial 5 rows using .head()</li>
<li>Count of each type using .value_counts()</li>
<li>quantity of columns & rows using .shape()</li>
</p>
<p>The .describe() also displays the following information:
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
<p>The program generates 4 Histograms, for Sepal Lenght,Seapl Width,Petal Lenght & Petal Width. The histograms are displayed and output is saved to individual .png files. These files are as follows:
<li>Sepal_Lenght_histogram.png</li>
<li>Sepal_Width_histogram.png</li>
<li>Petal_Lenght_histogram.png</li>
<li>Petal_Width_histogram.png</li>

# Histogram Conclusion #
<p>Some useful information that can be visualised from these histograms</p>
<li>Petal width of setosa is below .5</li>
<li>Petal width of virginica is typically largest of 3 types</li>
<li>Petal Lenght of setosa is between 1 & 2</li>
<li>Sepal width has wider range of values than sepal lenght</li>

# Scatter #
<p>The program generates 3 Scatter plots and the output is saved to individual .png files. These compare the following values
<li>Sepal_Lenght v Sepal Width</li>
<li>Sepal_Lenght v Petal Lenght</li>
<li>Sepal_Lenght v Petal Width</li>
</p>

# Scatter plot Conclusion #
<p>The following information can be gleaned from these scatter plots</p>

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

<li>The range of sepal lenghts is widest for iris Virginica & smallest for iris Setosa</li>
<li>The range of sepal widths is widest for iris Setosa & smallest for iris Virginica</li>
<li>The range of petal lenghts is widest for iris Virginica & smallest for iris Setosa </li>
<li>The range of petal widths is widest for iris Virginica & smallest for iris Setosa </li>

<p>Iris Setosa generally has the smallest measurements compared to other two species.</p>

# Pair Plot #

<p>The program generates a Pair plot, for Sepal Lenght,Seapl Width,Petal Lenght & Petal Width. Thepair plot allows easy visualisation of the relationships between pairs of variables. The output of the pairplot is saved in a .png file called pairplot.png</p>

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
<p>The following conlusions are the most interest i have found over the course of this prohect</p>
<ol>
<li>The Petal measurements are typically more useful in identifying species compared to sepal measurements</li>
<li>The Setosa species is easiest to identify due to smaller size</li>
<li>The Versicolr & Virginica species are hardest to identify</li> 



# How to run program #
<ol>
<li>$ python analysis</li>
<li>individual images open. close each image after viewing by clicking "x" on image</li> 
<li>.png & .txt files have been updated</li> 


# References # 
<ol>
<li><a href="#">https://www.kaggle.com/datasets/vikrishnan/iris-dataset</a></li>
<li><a href="#">https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data</a></li>
<li>https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-dat</a></li>
<li>https://medium.com/@naidubhavya06/detailed-explanation-of-exploratory-data-analysis-using-iris-dataset-fa8082a4ce0f</li>
<li> <li><a href="#">https://www.markdownguide.org/basic-syntax</a></li> </li>
<li>  </li>
<li>  </li>
<li>  </li>
<li>  </li>