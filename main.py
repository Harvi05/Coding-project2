# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:36:41 2022

@author: hg22aal
"""
"""
This is a file of code which is used to do comparison of data from 3 different datasets
and coclude to notify at world level
"""
#import useful libraries
import pandas as pd
import matplotlib.pyplot as plt

"""
Created function that reads a file, Update NAN values with 0 and transposed matrix
This function returns converted data to dataframe and transposed dataframe data
"""
def readFile(x):
    fileData = pd.read_csv(x);
    transposedFileData = pd.read_csv(x, header=None, index_col=0).T
    transposedFileData = transposedFileData.rename(columns={"Country Name":"Year"})
    transposedFileData = transposedFileData.fillna(0.0)
    return fileData, transposedFileData

"""
lineGraph_df is a function which takes a transposed matrix and plot the line graph using pandas
"""
def lineGraph_df(transposedFileData, label):
    Countries = ["China", "United States", "India", "Canada", "United Kingdom"]
    year = ["2000", "2001" , "2002", "2003", "2004", "2005", "2006" , "2007", "2008", "2009", "2010", "2011", "2012", "2013"]
    transposedFileData.update({"Year" : year})
    transposedFileData.plot("Year", ["China", "United States", "India", "Canada", "United Kingdom"], figsize=(10,7))
    plt.legend(Countries)
    plt.ylabel(label)
    plt.savefig("line Graph")

"""
This function return the sliced data
"""    
def sliceData(trfileData):
    trfileData = pd.DataFrame(trfileData)
    trfileData['Year'] = trfileData['Year'].astype(int)
    trfileData = trfileData.iloc[30:35]
    return trfileData

"""
this function takes transposed matrix and plot the bar graph using pandas
"""
def barGraph_df(transposedFileData):
    slicedFiledata = sliceData(transposedFileData)
    Countries = [ "India", "Canada", "United Kingdom"]
    slicedFiledata.plot.bar(x="Year", y=["India", "Canada", "United Kingdom"])
    plt.ylabel("Electricity production from renewable sources")
    plt.legend(Countries)
    plt.savefig("Bar graph")


"""
This function returns total values of the world
"""
def totalList(df, year, li):
    for i in year:
        li.append(df[i].sum())
    return li

"""
this function plots the graph using matploit for the world
"""
def barplot(year, li, label):
    plt.figure()
    plt.bar(year, li)
   # xyz ="dfsdf"
    #plt.xlabel(xyz)
    plt.ylabel(label)
    plt.xlabel("Years")
    plt.legend(loc = "upper right")
    plt.show()
    
"""
 this function plots the line graph using matploit for the world
"""   
def lineplot(year, li, label):
    plt.figure()
    plt.plot(year,li)
    plt.legend(loc = "upper right")
    plt.xlabel("Year")
    plt.ylabel(label)
    plt.show()
    
"""
calculating the percentage of data for all factros
"""   
def percentageData(li):
    increaseList = [0]
    for i in range(2, len(li)):
        increaseList.append((li[i]*100.0/li[i-1])-100)
    return increaseList

"""
plotting the line graph using pandas
"""
def lineplot_df(data, countries, label):
    plt.figure()
    data.plot("Year", countries)
    plt.ylabel(label)
    plt.legend(countries)
    plt.show()
    
#read the csv file  
population_df, transposedPop_df = readFile("pop3.csv")
powerConsume_Df, transposedpoCon_df = readFile("powerConsumption.csv")
agriLand_df, transAgriLand_df = readFile("AgriLand.csv")
forestArea_df, transForestArea_df = readFile("ForestArea.csv")

#plot population line graph
lineGraph_df(transposedPop_df, "Population")

#plot powerconsumption line graph
lineGraph_df(transposedpoCon_df,"powerConsumption")

#plot the bar graph of agriculture land and forest land
barGraph_df(transAgriLand_df)
barGraph_df(transForestArea_df)

year = ["2000", "2001", "2002", "2003", "2004", "2005", "2006" , "2007", "2008", "2009", "2010", "2011"]

#calsulating the total world values
population = totalList(population_df, year, ["Total World Population"])
powerConsumption = totalList(powerConsume_Df, year, ["Total World Power Consumption"])
agriLand = totalList(agriLand_df, year, ["Total Agriculture Land"])
forestArea = totalList(forestArea_df, year, ["Total Agriculture Land"])

populationLabel = "Total World Population Data"
powerConsumptiionLabel = "Total world PowerConsumption"
agriLandLabel = "Total Agriculture land"
forestAreaLabel = "Total Forest Area"

#ploting world bar graph 
barplot(year, population[1:], populationLabel)
barplot(year, powerConsumption[1:], powerConsumptiionLabel)
lineplot(year, agriLand[1:], agriLandLabel)
lineplot(year, forestArea[1:], forestAreaLabel)

#plotting the combined graph for all factors
totalData = dict(zip([populationLabel, powerConsumptiionLabel, agriLandLabel, forestAreaLabel], [percentageData(population), percentageData(powerConsumption), percentageData(agriLand), percentageData(forestArea)]))
totalData.update({"Year" : year})
totalData = pd.DataFrame(totalData)
lineplot_df(totalData, [populationLabel, powerConsumptiionLabel, agriLandLabel, forestAreaLabel],"increase or decrease from previous")