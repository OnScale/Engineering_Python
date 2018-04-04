# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:23:15 2016

Simple roatations of 2d planes in 3d space
TODO - set start points for image plane
- different from rotation point
"""
from mpl_toolkits.mplot3d import Axes3D
from mayavi import mlab

thetaX = 45. * pi/180 
thetaY = 45. * pi/180 
thetaZ = 0. * pi/180 
# Create rotation matrices
Rx = np.array([ [1, 0, 0],
                [0, cos(thetaX), -sin(thetaX)],
                [0, sin(thetaX), cos(thetaX)]])
                  
Ry = np.array([ [cos(thetaY), 0, sin(thetaY)],
                [0, 1, 0],
                [-sin(thetaY), 0, cos(thetaY)]])
                  
Rz = np.array([ [cos(thetaZ), -sin(thetaZ), 0],
                [sin(thetaZ), cos(thetaZ), 0],
                [0, 0, 1]])

# Set up origin plane              
Nx = 10
Ny = 10
Nz = 10

Lx = 1
Ly = 1
Lz = 1

# Origin Plane
X = np.arange(0, 1, 1./Nx)
Y = np.arange(0, 1, 1./Ny)
Z = zeros(Nz)

[Xd, Yd, Zd]=meshgrid(X,Y,Z)

# plot origin plane points
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(Xd, Yd, Zd, c='g')

# Create point to rotate around and shift to origin
Pr = np.array([0.5, 0.5, 0.5])
Po = np.array([-Pr[0], -Pr[1], -Pr[2]])
Pto = np.array([Po[0]+Lx, Po[1]+Ly, Po[2]+Lz])

# Create Image Plane
Xp = np.arange(Po[0], Pto[0], 1./Nx)
Yp = (ones(Ny) * 0.)
Zp = np.arange(Po[2], Pto[2], 1./Nz)

[Xi, Yi, Zi]=meshgrid(Xp,Yp,Zp)

# Rotate Image plane 90deg on X
R = np.dot(Rx, Ry, Rz)
(Xr, Yr, Zr) = np.dot(R,[ravel(Xi),ravel(Yi),ravel(Zi)])
Xt = Xr.reshape([Nx,Ny,Nz],order='C')
Yt = Yr.reshape([Nx,Ny,Nz],order='C')
Zt = Zr.reshape([Nx,Ny,Nz],order='C')

# Shift Plane back to reference point
Xt = Xt + Pr[0]
Yt = Yt + Pr[1]
Zt = Zt + Pr[2]

# plot new image plane points
ax.scatter(Xt, Yt, Zt)