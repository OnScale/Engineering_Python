# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:18:27 2014

@author: adminGH
"""

"""
Read in material tabl-Used to set up grid and mask non-flow fluids
"""

from numpy import *
from scipy import *

# enter filename
filename = 'model.flxtbl'       
fileIN = open(filename, "r")

# set up lists and vars
data, buff, fields, vals = [], [], [], []
idx = 0

for line in fileIN:
    if not line.startswith(' '):
        
        # clear buffer array for new input
        buff = []        
        
        # create list for data in correct place       
        data.append(line.split())
        
        # create list of names
        fields.append(data[idx][0])
        vals.append(data[idx][1])
        idx += 1
        
    else: 
        # use current tag to store info in list
        buff.extend(line.split())
        data[(idx-1)] = buff
       
fileIN.close()

# Map numerical data to types
data[2] = map(float32,data[2])
data[3] = map(float32,data[3])
data[4] = map(float32,data[4])
data[6] = map(int, data[6])

# Grid dimensions - nodes and elements
Nx = int(vals[2]); Ny = int(vals[3]); Nz = int(vals[4]) 
Ex = Nx-1; Ey = Ny-1; Ez = Nz-1

# Format elements into matrix
n=0
MatrMap = zeros([Ex,Ey,Ez], dtype=int)
for k in range(Ez):
    for j in range(Ey):
        for i in range(Ex):
            MatrMap[i,j,k] = data[6][n]
            n += 1
            
# Create arrays for Xv, Yv, Zv
Xv = float32(zeros([Nx,Ny,Ez]))
Yv = float32(zeros([Nx,Ny,Ez]))
Zv = float32(zeros([Nx,Ny,Ez]))

# all materials not 'flow material' xvel, yvel, zvel = 0.
flowmat = 'watr'
fmat_index = data[5].index(flowmat) + 1
for k in range(Ez):
    for j in range(Ey):
        for i in range(Ex):
            if (MatrMap[i,j,k] == fmat_index):
                Xv[i,j,k] = 0.     
                Yv[i,j,k] = 0.     
                Zv[i,j,k] = 1.   

# Create a 3D array for last k-index of flow
ZvLast = [Ex, Ey, 1]
ZvLast = Zv[:,:,Ez-1]

# Append to Zv array to prevent no flow at boundary
Zv = dstack((Zv, ZvLast))

# Fortran Format
XvF = Xv.T
YvF = Yv.T
ZvF = Zv.T

# Export flex binary format
Fxdata = open('xvflow.bin', 'wb') 
Fydata = open('yvflow.bin', 'wb')
Fzdata = open('zvflow.bin', 'wb')

Fxhdr = open('xvflow.hdr', 'w')
Fyhdr = open('yvflow.hdr', 'w')
Fzhdr = open('zvflow.hdr', 'w')

# Write header files
Fxhdr.write("xvflow 3 %d %d %d float32 \n" % (Nx,Ny,Nz))
Fyhdr.write("yvflow 3 %d %d %d float32 \n" % (Nx,Ny,Nz))
Fzhdr.write("zvflow 3 %d %d %d float32 \n" % (Nx,Ny,Nz))

# Write Data files
XvF.tofile(Fxdata); YvF.tofile(Fydata); ZvF.tofile(Fzdata)

# Close all open files
Fxdata.close(); Fydata.close(); Fzdata.close()
Fxhdr.close(); Fyhdr.close(); Fzhdr.close()

print 'Flow Importation Complete'