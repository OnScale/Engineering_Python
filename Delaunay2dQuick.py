# -*- coding: utf-8 -*-
"""
Super quick Delaunay test
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as sp

# Read Velocity files 
data = loadtxt('PZFlex2d.csv', delimiter=',', dtype='float32')

# Read positional data
X = data[:,0]
Y = data[:,1]
Xv = data[:,2]
Yv = data[:,3]

points = np.array([data[:,0],data[:,1]])
points = points.T
s=10

figure()
tri = sp.Delaunay(points)
sp.delaunay_plot_2d(tri)

figure()
vor = sp.Voronoi(points)
sp.voronoi_plot_2d(vor)