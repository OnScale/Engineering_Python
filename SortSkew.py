# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:50:45 2013

@author: adminGH
"""
# load node and copy to test array
data=loadtxt("nodes.txt"); A = data 
                            
# Can split into individual vectors if needed
X = A[:,0]; Y = A[:,1]; Z = A[:,2]

# get max and minimum XYZ
Xmax=max(X); Xmin=min(X); Ymax=max(Y); Ymin=min(Y); Zmax=max(Z); Zmin=min(Z)

#    test a sorting algorithm on X
for passnum in range(len(A)-1,0,-1):    # set passes through A
    for i in range(passnum):            # each pass, cycle through nodes        
        if A[i,0] > A[i+1,0]:           # check X-value
            
            temp = A[i,:]
            A[i,:] = A[i+1,:]
            A[i+1,:]= temp
                    
