# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:58:01 2014

@author: Gerry Harvey

Script to interpolate XY Velocities
into new PZFlex binary format

Improvements:
    - Write direct into out1 format
    - be callable from flxinp file - DONE
    - need to have pylibs pathed for that - DONE
    
Notes:
    - Better interpolation implemented
    - Writing to binary format implemented
"""

# Import necessary libraries
import scipy.interpolate as scpint

""" 
Libraries required if calling direct from Flex
"""
import sys
# sys.path.append("C:\Users\adminGH\Anaconda\Lib\site-packages")
from numpy import *
from scipy import *
from matplotlib.mlab import *

"""
Read in material tabl-Used to set up grid and mask non-flow fluids
"""

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
data[5] = map(int, data[5])

# Grid dimensions - nodes and elements
Nx = int(vals[2]); Ny = int(vals[3]) 
Ex = int(vals[2]) - 1; Ey = int(vals[3]) - 1

# Format elements into matrix
n=0
MatrMap=zeros([Ex,Ey], dtype=int)
for j in range(Ey):
    for i in range(Ex):
            MatrMap[i,j] = data[5][n]
            n += 1

""" 
Flow interpolation
- read in scatter data
- interpolate on to regular based on model
- create arrays and write binary files
"""

print 'Processing in Python....\n'

# Read Velocity files 
FlowData = loadtxt('PZFlex2d.csv', delimiter=',', dtype='float32')

# Read positional data
X = FlowData[:,0]; Y = FlowData[:,1]

# Read velocity data
Xv = FlowData[:,2]; Yv = FlowData[:,3]

# set up grid to accomodate Symmetry
Nx_sym = Nx; Nx =  Nx_sym*2

# Get max and min X & Y from table file
XMax = max(data[2]); XMin = -XMax; YMax = max(data[3]); YMin = min(data[3])

# Create interp grid based on Flex Grid
Xi = linspace(XMin,XMax,Nx)
Yi = linspace(YMin,YMax,Ny)
[XGrid, YGrid] = meshgrid(Xi,Yi)

# interpolate to Flex Grid
XvInt = scpint.griddata((X,Y), Xv, (XGrid,YGrid), method='linear', fill_value=0.)
YvInt = scpint.griddata((X,Y), Yv, (XGrid,YGrid), method='linear', fill_value=0.)

# Half Arrays along X-axis for symm conditions in Flex
XvInt = XvInt[:,Nx_sym:]
YvInt = YvInt[:,Nx_sym:]

# Convert arrays to Single Precision
XvF = float32(XvInt)
YvF = float32(YvInt)

# all materials not 'flow material' xvel, yvel = 0.
fmat_index = data[4].index('dflm24') + 1
i, j = 0, 0
for j in range(Ey):
    for i in range(Ex):
        if not (MatrMap[i,j] == fmat_index):
            XvF.T[i,j] = 0.     # Fortran format
            YvF.T[i,j] = 0.     # Fortran format

# Export XvInt and YvInt to flex binary format
Fxdata = open('xvflow.bin', 'wb'); Fydata = open('yvflow.bin', 'wb')
Fxhdr = open('xvflow.hdr', 'w'); Fyhdr = open('yvflow.hdr', 'w')

# Write header files
Fxhdr.write("xvflow 3 %d %d %d float32 \n" % (Nx_sym,Ny, 1))
Fyhdr.write("yvflow 3 %d %d %d float32 \n" % (Nx_sym,Ny, 1))

# Write Data files
XvF.tofile(Fxdata); YvF.tofile(Fydata)

# Close all open files
Fxdata.close(); Fydata.close(); Fxhdr.close(); Fyhdr.close()

print 'Complete'



