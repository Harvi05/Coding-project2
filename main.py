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
import numpy as np

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
    trfileData = trfileData.iloc[28:37]
    return trfileData

"""
this function takes transposed matrix and plot the bar graph using pandas
"""
def barGraph_df(transposedFileData):
    slicedFiledata = sliceData(transposedFileData)
    Countries = ["China", "United States", "India", "Canada", "United Kingdom"]
    year = ["2003", "2004", "2005", "2006", "2007", "2008", "2009",  "2009", "2010", "2011"]
    slicedFiledata.plot.bar(x="Year", y=["India", "Canada", "United Kingdom", "United States", "China"])
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
def barplot(years, li, label):
    plt.figure()
    plt.bar(years, li)
    plt.ylabel(label)
    plt.xlabel("Years")
    plt.show()
    
population_df, transposedPop_df = readFile("pop3.csv")
powerConsume_Df, transposedpoCon_df = readFile("powerConsumption.csv")
proFRenew_df, transProFRenew_df = readFile("productionFromRenew.csv")

#plot population line graph
lineGraph_df(transposedPop_df, "Population")

#plot powerconsumption line graph
plotGraph3 = lineGraph_df(transposedpoCon_df,"powerConsumption")

#plot the bar graph of production of electricity from renewable sources
p3 = barGraph_df(transProFRenew_df)

year = ["2000", "2001", "2002", "2003", "2004", "2005", "2006" , "2007", "2008", "2009", "2010", "2011"]

#calsulating the total world values
population = totalList(population_df, year, ["Total World Population"])
powerConsumption = totalList(powerConsume_Df, year, ["Total World Power Consumption"])
productionFRen = totalList(proFRenew_df, year, ["Total eelectricity production"])

populationLabel = "Total World Population Data"
powerConsumptiionLabel = "Total world PowerConsumption"
productionFRenLabel = "world production of electricity from renewable source"

#ploting world bar graph 
barplot(year, population[1:], populationLabel)
barplot(year, powerConsumption[1:], powerConsumptiionLabel)
barplot(year, productionFRen[1:], productionFRenLabel)
