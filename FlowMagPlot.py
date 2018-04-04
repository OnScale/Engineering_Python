# -*- coding: utf-8 -*-
"""
Created on Tue May 06 19:57:15 2014

@author: adminGH
"""

from pylab import *
import mayavi.mlab as maya
# Set limits and number of points in grid
xmax = 1
xmin =-xmax
NX = 50
ymax= 1
ymin =-ymax
NY = 50
zmax = 0.2
zmin = -zmax
NZ = 10
# Make grid and calculate vector components
x = linspace(xmin, xmax, NX)
y = linspace(ymin, ymax, NY)
z = linspace(zmin, zmax, NZ)
X, Y, Z = meshgrid(x, y, z)
S2 = X**2 + Y**2 + Z**2
# This is the radius squared
Bx =-Y/S2
By = +X/S2
Bz = S2
maya.figure(bgcolor=(1,1,1))
maya.quiver3d(X,Y,Z,Bx,By,Bz)
