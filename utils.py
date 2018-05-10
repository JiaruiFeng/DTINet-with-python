# -*- coding: utf-8 -*-
"""
utils
"""
import csv
import pandas as pd
def outputCSVfile(filename,data):
    csvfile=open(filename,'wb')
    writer=csv.writer(csvfile)
    writer.writerows(data)
    csvfile.close()
    
def txtToCSV(inputname,sep,header,outputname):
    txtfile=pd.read_table(inputname,sep=sep,header=header)
    txtfile=txtfile.as_matrix(columns=None)
    outputCSVfile(outputname,txtfile)
