# DIS---Walmart-Store---P07

Team Number:P07

Team Members: Manoj Kumar Kotte
              Mani Nomula

Summary: We will be using Walmart Store transactions as our data set. This dataset contains huge amount of information related to various stores. We are calculating what is the maximum and minimum fuel price encountered at each store.

Describe your Data Source: Our data source is features.txt, which is structured data. We have converted csv file to text file so that it is easy to handle. This file contains 12 fields and size of the file is around 580KB and the data is structured.

Link to Data Source: https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data(Links to an external site.) (Links to an external site.)

What makes it a big data problem?
Volume: Even though the size of the file is 580 KB, it has 8191 records which is hard to handle using traditional methods.
Variety: The data is a structured. Data is stored in text file.
Velocity: The data in the dataset is generated weekly and 4 years of data is stored for each store.
Veracity: There is no noise in the data. It is cleaned and formatted.
Value: For each store we are finding the max and min fuel price which helps the store managers to make a good decision.

Describe your two Map Reduce problems in the format "for each _(key)_ , we will find the _(value)__". 
For each store, calculate the maximum fuel price.
For each store, calculate the minimum fuel price.

Mapper input:  show one line of data that your mapper will read.
1 2/5/2010  42.31 2.572

Mapper output/ Reducer input:
1      2.572
1      2.548
1      2.514
1      2.561
1      2.625

Reducer Output (max):
1          3.717
2          3.907
3          3.907
4          3.866

Language: We are using Python as our programming language.

Process: We are processing numeric data. No data cleaning is required for the data set.
