# -*- coding: utf-8 -*-
"""
convert data into similarity between drug or protein network
using jaccard distance 

"""
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import utils

Nets = ['mat_drug_drug', 'mat_drug_disease', 'mat_drug_se','mat_protein_protein', 'mat_protein_disease']

for net in Nets:
    inputID='./data/'+net+'.txt'
    M=pd.read_table(inputID,sep=' ', header=None)
    # jaccard distance
    Sim=1-pdist(M,'jaccard')
    Sim=squareform(Sim)
    Sim=Sim+np.eye(len(Sim))
    Sim=np.nan_to_num(Sim)
    
    #output csv file
    outputID='./data/Sim_'+net+'.csv'
    utils.outputCSVfile(outputID,Sim)
    
#write chemical similarity to networks
M=pd.read_table('./data/Similarity_Matrix_Drugs.txt',sep='    ',header=None)
M=M.as_matrix(columns=None)
utils.outputCSVfile('./data/Sim_mat_drugs.csv',M)
#write sequence similarity to networks
M=pd.read_table('./data/Similarity_Matrix_Proteins.txt',sep=' ',header=None)
M=M.as_matrix(columns=None)
M=M/100
utils.outputCSVfile('./data/Sim_mat_proteins.csv',M)