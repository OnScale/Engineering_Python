"""
Title: Vector Rotation

Created on Tue Dec 22 11:04:08 2015

@author: PZFlex
"""

# Import packages
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Inputs
rxdeg = 45.
rydeg = 20.
rzdeg = 0.

# Convert to radians
rx = rxdeg * pi / 180.
ry = rydeg * pi / 180.
rz = rzdeg * pi / 180.

# Set up vectors
ux = np.matrix([[1], [0], [0]])
uy = np.matrix([[0], [1], [0]])
uz = np.matrix([[0], [0], [1]])

# Rotation matrix
Rx = np.matrix([[1, 0, 0], [0, cos(rx), -sin(rx)], [0, sin(rx), cos(rx)]])
Ry = np.matrix([[cos(ry), 0, sin(ry)], [0, 1, 0], [-sin(ry), 0, cos(rx)]])
Rz = np.matrix([[cos(rz), -sin(rz), 0], [sin(rz), cos(rx), 0], [0, 0, 1]])
R = Rx*Ry*Rz

# Rotate vectors
uxr = R * ux
uyr = R * uy
uzr = R * uz

# Create plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0,ux[0]],[0,ux[1]],[0,ux[2]],'r',linewidth=1)
ax.plot([0,uy[0]],[0,uy[1]],[0,uy[2]],'g',linewidth=1)
ax.plot([0,uz[0]],[0,uz[1]],[0,uz[2]],'b',linewidth=1)
ax.plot([0,uxr[0]],[0,uxr[1]],[0,uxr[2]],'r',linewidth=4)
ax.plot([0,uyr[0]],[0,uyr[1]],[0,uyr[2]],'g',linewidth=4)
ax.plot([0,uzr[0]],[0,uzr[1]],[0,uzr[2]],'b',linewidth=4)
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
plt.show()