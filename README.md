# DIS---Walmart-Store---P07

Team Number:P07

Team Members: Manoj Kumar Kotte &
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


We have used the Modern Version Controlling System -GIT. The repository is made public and the code is available in an accessible location. Yes, each team member designed, implemented, and executed one of the MapReduce processes. We have divided the work equally and worked collectively which made us to complete the project successfully.




## Getting Started

- Import this repo to your Github.
- Clone from your Github down to your local computer, e.g. C:\44564\P07.

## Steps to run:

- Right click on folder (P07) and click open-command-window-here-administrator.
- Enter the following commands in the window.
	- python mapper.py
	
	
	![1](https://cloud.githubusercontent.com/assets/22262884/25057522/4ad6d348-2136-11e7-8e74-0902b78adc64.PNG)

	The output of mapper.py is stored in map_out.txt and it looks like this
	
	![3](https://cloud.githubusercontent.com/assets/22262884/25057552/9f109a5c-2136-11e7-910f-efe7e81c9d50.PNG)

	
  - This  map_out.txt acts as input to reducer file.
  
	- python reducer.py
	
	![2](https://cloud.githubusercontent.com/assets/22262884/25057525/5429d67a-2136-11e7-9af6-7f11d20761cb.PNG)

	
  - After executing this command we will get two output files. One is for maximum and another is minimum.


![4](https://cloud.githubusercontent.com/assets/22262884/25057553/a04779f4-2136-11e7-9cd6-676e6a049211.PNG)


Graphical representation of maximum function:

![10](https://cloud.githubusercontent.com/assets/22262884/25250052/bf9f2e62-25d9-11e7-860c-9ad72632f914.PNG)

