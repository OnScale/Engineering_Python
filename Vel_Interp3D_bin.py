# -*- coding: utf-8 -*-
"""
Script to interpolate XYZ Velocities
into new PZFlex binary format

    
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
from scipy import ndimage
""" 
Flow interpolation
- read in scatter data
- interpolate on to regular based on model
- create arrays and write binary files
"""

print 'Processing in Python....\n'

# Read point cloud data from FLOW
filename = 'GT_3d_full.csv'
cols = [0,1,2,3,4,5]
Flow = loadtxt(filename, delimiter=',', usecols=cols)

# Read positional grid information from Flex
filename = 'flexinfo.txt'
info = loadtxt(filename, delimiter=',')

# Set bounding box for data to work with
Xmin, Xmax = info[0], info[1] ; Xd = Xmax - Xmin
Ymin, Ymax = info[2], info[3] ; Yd = Ymax - Ymin
Zmin, Zmax = info[4], info[5] ; Zd = Zmax - Zmin
Nx, Ny, Nz, box = info[6], info[7], info[8], info[9]

# Subsample Flex Grid to keep interpolation time down
nsamp = info[10]
Nxs = int(Nx/nsamp)
Nys = int(Ny/nsamp)
Nzs = int(Nz/nsamp)

(Xzoom, Yzoom, Zzoom) = round((Nx/Nxs),3), round((Ny/Nys),3), round((Nz/Nzs),3)

# Only use data in the bounding box region
dims = np.shape(Flow)
FlowBB = zeros(dims)
i=0
for row in Flow:
    if (row[0]>Xmin and row[0]<Xmax):
        if (row[1]>Ymin and row[1]<Ymax):
            if (row[2]>Zmin and row[2]<Zmax):
                FlowBB[i]=np.hstack(row)                
                i+=1
dataFlow=FlowBB[0:i-1,:]

# Extract positional and Flow values
X = dataFlow[:,0] ; Xv = dataFlow[:,3]
Y = dataFlow[:,1] ; Yv = dataFlow[:,4]
Z = dataFlow[:,2] ; Zv = dataFlow[:,5]

# Create interp grid based on Flex Grid
Xi = linspace(Xmin,Xmax,Nxs)
Yi = linspace(Ymin,Ymax,Nys)
Zi = linspace(Zmin,Zmax,Nzs)
[XGrid, YGrid, ZGrid] = meshgrid(Xi,Yi,Zi)

# interpolate to Flex Grid
XvInt = scpint.griddata((X,Y,Z), Xv, (XGrid,YGrid,ZGrid), method='nearest')
YvInt = scpint.griddata((X,Y,Z), Yv, (XGrid,YGrid,ZGrid), method='nearest')
ZvInt = scpint.griddata((X,Y,Z), Zv, (XGrid,YGrid,ZGrid), method='nearest')

# Option to smooth the interpolated data
XvInt = ndimage.gaussian_filter(XvInt, sigma=2)
YvInt = ndimage.gaussian_filter(YvInt, sigma=2)
ZvInt = ndimage.gaussian_filter(ZvInt, sigma=2)

# Convert arrays to Single Precision & transpose
XvF = float32(np.transpose(XvInt, (1,0,2)))
YvF = float32(np.transpose(YvInt, (1,0,2)))
ZvF = float32(np.transpose(ZvInt, (1,0,2)))

XvF = ndimage.zoom(XvF, (Xzoom, Yzoom, Zzoom))
YvF = ndimage.zoom(YvF, (Xzoom, Yzoom, Zzoom))
ZvF = ndimage.zoom(ZvF, (Xzoom, Yzoom, Zzoom))

# Export XvInt and YvInt to flex binary format
dim=shape(ZvF)
rX = ravel(XvF, order='F')
rY = ravel(YvF, order='F')
rZ = ravel(ZvF, order='F')
XvF = rX.reshape(dim,order='C')
YvF = rY.reshape(dim,order='C')
ZvF = rZ.reshape(dim,order='C')

# Write header files
Fxdata = open('xvflow.bin', 'wb') 
Fydata = open('yvflow.bin', 'wb') 
Fzdata = open('zvflow.bin', 'wb')
Fxhdr = open('xvflow.hdr', 'w') 
Fyhdr = open('yvflow.hdr', 'w') 
Fzhdr = open('zvflow.hdr', 'w')

Fxhdr.write("xvflow 3 %d %d %d float32 \n" % (Nx,Ny,Nz))
Fyhdr.write("yvflow 3 %d %d %d float32 \n" % (Nx,Ny,Nz))
Fzhdr.write("zvflow 3 %d %d %d float32 \n" % (Nx,Ny,Nz))

# Write Data files
XvF.tofile(Fxdata); YvF.tofile(Fydata); ZvF.tofile(Fzdata)

# Close all open files
Fxdata.close(); Fydata.close(); Fzdata.close()
Fxhdr.close(); Fyhdr.close();  Fzhdr.close()

print 'Complete'



