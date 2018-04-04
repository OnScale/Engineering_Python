# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 01:53:37 2014

@author: Gerry Harvey

Create a subsampled mask for plotting purposes
every nth point = FALSE
"""

#create full mask array of correct size
mask=np.zeros([300,300], dtype=bool)
mask_sub=np.copy(mask)
Nth = 2
# loop through elements and assign FALSE
for i in range(0,len(mask),Nth):
    for j in range(0,len(mask),Nth):
        mask_sub[i,j] = True
    
# shift by 1 and repeat
for i in range(1,len(mask),Nth):
    for j in range(1,len(mask),Nth):
        mask_sub[i,j] = True

