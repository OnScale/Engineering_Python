# -*- coding: utf-8 -*-
"""
Created on Thu May 08 14:04:19 2014

@author: adminGH
"""

# This example shows how to use Delaunay3D with alpha shapes.

import vtk

# The points to be triangulated are generated randomly in the unit
# cube located at the origin. The points are then associated with a
# vtkPolyData.
math = vtk.vtkMath()
points = vtk.vtkPoints()

filename = 'PZFlex.csv'
data = loadtxt(filename, delimiter=',')

# Read positional data
X = data[:,0]; Y = data[:,1]; Z = data[:,2]

# Read velocity data
Xv = data[:,3]; Yv = data[:,4]; Zv = data[:,5]

Np = len(data)

for i in range(0, Np):
    points.InsertPoint(i, X[i], Y[i], Z[i])

profile = vtk.vtkPolyData()
profile.SetPoints(points)

# Delaunay3D is used to triangulate the points. The Tolerance is the
# distance that nearly coincident points are merged
# together. (Delaunay does better if points are well spaced.) The
# alpha value is the radius of circumcircles, circumspheres. Any mesh
# entity whose circumcircle is smaller than this value is output.
delny = vtk.vtkDelaunay3D()
delny.SetInput(profile)
delny.SetTolerance(0.001)
delny.SetAlpha(0.02)
delny.BoundingTriangulationOn()

print 'done'

# Shrink the result to help see it better.
shrink = vtk.vtkShrinkFilter()
shrink.SetInputConnection(delny.GetOutputPort())
shrink.SetShrinkFactor(0.9)

map = vtk.vtkDataSetMapper()
map.SetInputConnection(shrink.GetOutputPort())

triangulation = vtk.vtkActor()
triangulation.SetMapper(map)
triangulation.GetProperty().SetColor(1, 0, 0)

# Create graphics stuff
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Add the actors to the renderer, set the background and size
ren.AddActor(triangulation)
ren.SetBackground(1, 1, 1)
renWin.SetSize(250, 250)
renWin.Render()

cam1 = ren.GetActiveCamera()
cam1.Zoom(1.5)

iren.Initialize()
renWin.Render()
iren.Start()
