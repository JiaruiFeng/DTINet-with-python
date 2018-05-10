# -*- coding: utf-8 -*-
"""
diffusionRWR

"""
import numpy as np
import pandas as pd

def diffusionRWR(A,maxiter,restartProb,netname):
    n=len(A)
    #normalize the adjacency matrix
    P=A/A.sum(axis=0)
    
    #Personalized PageRank
    restart=np.eye(n)
    Q=np.eye(n)
    for i in range(1,maxiter):
        Q_new=(1-restartProb)*np.dot(P,Q)+restart*restartProb
        delta=np.linalg.norm((Q-Q_new))
        print 'this is'+netname + str(i)+ 'circulation,the delta='+str(delta)
        Q=Q_new
        if delta<1e-6:
            break
    return Q
        
