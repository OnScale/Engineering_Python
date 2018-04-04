# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:58:01 2014

@author: Gerry Harvey

Script to interpolate XY Velocities and 
write to 2 col ascii for import to Flex

Improvements:
    - Write direct into out1 format
    - be callable from flxinp file
    - need to have pylibs pathed for that

"""

# Read Velocity files 
data = loadtxt('PZFlex2d.csv', delimiter=',');

# Read positional data
X = data[:,0];
Y = data[:,1];

# Read velocity data
Xv = data[:,2];
Yv = data[:,3];

"""
set up grid and flip out for symm conditions
No. of points can be read from flxinp or symb files
"""
Nx_sym = 188;
Nx =  Nx_sym*2;
Ny = 1872;
Nelem = Nx*Ny
Nelem_sym = Nx_sym*Ny

# Get max and min X & Y
XMax = max(X);
XMin = min(X);
YMax = max(Y);
YMin = min(Y);

# Create interp frid
Xi = linspace(XMin,XMax,Nx);
Yi = linspace(YMin,YMax,Ny);

[XGrid, YGrid] = meshgrid(Xi,Yi);

# interpolate
XvInt = griddata(X,Y,Xv,XGrid,YGrid);
YvInt = griddata(X,Y,Yv,XGrid,YGrid);

# Half Arrays along X-axis for symm conditions in Flex
XvInt = XvInt[:,Nx_sym:]
YvInt = YvInt[:,Nx_sym:]

# Format for export to text file
XvInt_colm = reshape(XvInt,Nelem_sym,1);
YvInt_colm = reshape(YvInt,Nelem_sym,1);

# Remove NaN/Masked array vaules
XvInt_colm = np.nan_to_num(XvInt_colm)
YvInt_colm = np.nan_to_num(YvInt_colm)

# Create array for 2-col format
XY_Vels = zeros([Nelem_sym,2]);

# place interpolated values in correct cols
XY_Vels[:,0] = XvInt_colm;
XY_Vels[:,1] = YvInt_colm;

# write file
savetxt('XYvels.dat', XY_Vels, delimiter=' ')
