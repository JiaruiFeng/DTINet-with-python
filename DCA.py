# -*- coding: utf-8 -*-
"""
DCA
"""
from __future__ import division
import numpy as np
import pandas as pd
import diffusionRWR as RWR
import math
import scipy.linalg as la
import utils
def DCA(networks,dim,rsp,maxiter):
    i=1
    P=np.array([])
    for network in networks:
        fileID='./data/'+network+'.csv'
        net=pd.read_csv(fileID,header=None)
        net=net.as_matrix(columns=None)
        tQ=RWR.diffusionRWR(net,maxiter,rsp,network)
        if i==1:
            P=tQ
        else:
            #concatenate network
            P=np.hstack((P,tQ))
        i+=1
    print P.shape
    nnode=len(P)
    alpha=1/nnode
    P=np.log(P+alpha)-math.log(alpha)
    P=np.dot(P,P.T)
    
    #use SVD to decompose matrix
    U,Sigma,VT=la.svd(P,lapack_driver='gesvd',full_matrices=True)
    sigd=np.dot(np.eye(dim),np.diag(Sigma[:dim]))
    Ud=U[:,:dim]
    #get context-feature matrix, since we use P*PT to get square matrix, we need to sqrt twice
    X=np.dot(Ud,np.sqrt(np.sqrt(sigd)))
    return X,P,U,np.sqrt(np.sqrt(sigd))


maxiter = 20
restartProb = 0.50
dim_drug = 100
dim_prot = 400
drugNets = ['Sim_mat_drug_drug', 'Sim_mat_drug_disease', 'Sim_mat_drug_se', 'Sim_mat_Drugs']
proteinNets = ['Sim_mat_protein_protein', 'Sim_mat_protein_disease', 'Sim_mat_Proteins']
Y,P2,U2,s2=DCA(proteinNets,dim_prot,restartProb,maxiter)
X,P1,U1,s1=DCA(drugNets,dim_drug,restartProb,maxiter)
X=np.array(X)
Y=np.array(Y)
utils.outputCSVfile('./data/drug_vector_d.csv',X)
utils.outputCSVfile('./data/protein_vector_d.csv',Y)

