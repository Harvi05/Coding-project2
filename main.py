# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:36:41 2022

@author: hg22aal
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def readFile(x):
    fileData = pd.read_csv(x);
    
    transposedFileData = pd.read_csv(x, header=None,index_col=0).T
    #print(transposedFileData)
    transposedFileData = transposedFileData.rename(columns={"Country Name":"Year"})
    print(transposedFileData)
    print("hete")
    
    return fileData, transposedFileData

def lineGraph(transposedFileData):
    Countries = ["China", "United States", "India", "Canada", "United Kingdom"]
    year = ["2000","2001" ,"2002","2003","2004","2005","2006" ,"2007","2008" ,"2009", "2010", "2011", "2012", "2013"]
    transposedFileData.update({"Year" : year})
    transposedFileData.plot("Year",["China", "United States", "India", "Canada", "United Kingdom"],figsize=(15,10))
    plt.legend(Countries)
    plt.savefig("line Graph")

def barGraph(transposedFileData):
    Countries = ["China", "United States", "India", "Canada", "United Kingdom"]
    year = ["2009", "2009","2010", "2011", "2012", "2013"]
    transposedFileData.update({"Year" : year})
    
    transposedFileData.plot(x="Year", y=["India", "Canada","United Kingdom","United States"], kind="bar")
    plt.legend(Countries)
    plt.savefig("Bar graph")
"""
def pieChart(x):
    fileData = pd.read_csv(x)
    print(fileData)
    fileData[["2010"]] = fileData[["2010"]].apply(pd.to_numeric)
    total= [fileData["2010"].sum()]
    print(total)
    plt.figure()
    plt.pie([fileData['Canada'],total-fileData['Canada']],labels = ["Canada","Rst world"],autopct = "%1.1f%%")
    plt.show()
    
   
    population = readFile(x)
    print("Fdfdf")
    print(population)
    plt.figure()
    label = ["2004", "2005", "2006", "2007","2008"]
    plt.pie(population['Australia'], labels = label, autopct = "%1.1f%%")
    plt.title("United Kingdom agricultural land")
    plt.legend()
    plt.show()
   
def total(x):
    data = readFile(x)
    print(data['2004'])
    data['2004'] = pd.to_numeric(data['2004'])
    data['2005'] = pd.to_numeric(data['2005'])
    data['2006'] = pd.to_numeric(data['2006'])
    data['2007'] = pd.to_numeric(data['2007'])
    tot = [data['2004'].sum(),data['2005'].sum(),data['2006'].sum(),data['2007'].sum()]
    print(tot)
"""
fileData1, TransposedFileData1 = readFile("powerConsumption.csv")
fileData2, TransposedFileData2 = readFile("e3.csv")


plotGraph2 = lineGraph(TransposedFileData1)
plotGraph3 = lineGraph(TransposedFileData2)

p3 = barGraph(TransposedFileData2)
#p4 = pieChart("agri.csv")
#tt = total("poverty.csv")