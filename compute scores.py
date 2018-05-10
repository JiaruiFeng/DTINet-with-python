# -*- coding: utf-8 -*-
"""
score
"""

import pandas as pd
import numpy as np
import utils
import seaborn as sns
drugFeature=pd.read_csv('./data/drug_vector_d.csv',header=None)
proteinFeature=pd.read_csv('./data/protein_vector_d.csv',header=None)
knownInteraction=pd.read_table('./data/mat_drug_protein.txt',sep=' ',header=None)

#computing similarity
drugSimilarity=drugFeature.T.corr()
proteinSimilarity=proteinFeature.T.corr()

drugSimilarity=drugSimilarity.as_matrix(columns=None)
proteinSimilarity=proteinSimilarity.as_matrix(columns=None)
knownInteraction=knownInteraction.as_matrix(columns=None)



scores=np.dot(np.dot(drugSimilarity,knownInteraction),proteinSimilarity)

utils.outputCSVfile('./data/scores.csv',scores)


#sns.heatmap(scores,cmap='Blues')

'''
def findInteraction(interaction):
    drugList=[]
    proteinList=[]
    for i in range(len(interaction)):
        for j in range(len(interaction.T)):
            if interaction[i][j]==1:
                drugList.append(i)
                proteinList.append(j)
    return drugList,proteinList

X,Y=findInteraction(knownInteraction)

scores=[[0 for i in range(len(proteinSimilarity))] for j in range(len(drugSimilarity))]
for i in range(len(drugSimilarity)):
    for j in range(len(proteinSimilarity)):
        score=0
        for n in range(len(X)):
            if X[n]==i and Y[n]!=j:
                score+=proteinSimilarity[j][Y[n]]
        for m in range(len(Y)):
            if Y[n]==j and X[m]!=i:
                score+=drugSimilarity[i][X[m]]
        scores[i][j]=score
    print i
    '''








'''
#defining the findInteraction function to find intercation in interaction matrix,  in order to reduce the computational cost 
def findInteraction(interaction):
    interactionList=[]
    for i in range(len(interaction.T)):
        for j in range(len(interaction)):
            if interaction[i][j]==1:
                interactionList.append((i,j))
    return interactionList

interactionList=findInteraction(knownInteraction)

"""
count score and build the scores matrix
"""
        
scores=[[0 for i in range(len(proteinSimilarity))] for j in range(len(drugSimilarity))]
for i in range(len(drugSimilarity)):
    for j in range(len(proteinSimilarity)):
        score=0
        for interaction in interactionList:
            score+=drugSimilarity[i][interaction[1]]*proteinSimilarity[j][interaction[0]]
        scores[i][j]=score
    print '------------'+str(i)+'---------------'
scores=pd.DataFrame(scores,index=None,columns=None)
print scores.shape



'''





















'''
def haveone(df):
    for i in range(len(df)):
        if df[i]!=0:
            return True
    return False

scores=[[0 for i in range(len(proteinSimilarity))] for j in range(len(drugSimilarity))]
for i in range(len(drugSimilarity)):
    o=0
    for n in range(len(proteinSimilarity)):
        score=0
        for m in range(len(proteinSimilarity)):
            if haveone(KnownInteraction[j]):         
                for j in range(len(drugSimilarity)):
                    if KnownInteraction[m][j]==1:
                        score+=drugSimilarity[j][i]*proteinSimilarity[m][n]
        print str(n)+"+++++++++++++++++++++++++++++++++++++++++++++"
        scores[n][i]=score

scores=pd.DataFrame(scores,columns=None,index=None)
'''