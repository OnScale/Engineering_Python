# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 14:39:07 2014

Author: Gerry Harvey

- Read in XYZ point cloud mesh
- Read in Scalar values and apply a single one
- Create mesh from delaunay
- Export to VTK format for visualisation in Paraview

Updates:
- Read all 3 velocities in as a vector and apply to dataset (SetVectors?)
"""

# This example shows how to use Delaunay3D with alpha shapes.
import vtk
from vtk import *

# prevent error window from popping up
ow = vtk.vtkOutputWindow()
ow.DebugOff()
ow.GlobalWarningDisplayOff()

large = 1
if ( large == 1 ):
    filename = '0010.csv'
    Name = 'Vol'
    cols = [0,1,2,3,4,5]
else:
    filename = 'grid_vels.csv'
    Name = 'Surf'
    cols = [1,2,3,4,5,6]

# Read positional & Vel data
data = loadtxt(filename, delimiter=',', usecols=cols)
X = data[:,3]; Y = data[:,4]; Z = data[:,5]
Xv = data[:,0]; Yv = data[:,1]; Zv = data[:,2]

# Get number of unique points
Np = len(data)

# The points to be triangulated are generated randomly in the unit
# cube located at the origin. The points are then associated with a
# vtkUnstructuredGrid
points = vtk.vtkPoints()

# Set up arrays for data on points
xvel = vtk.vtkFloatArray()
xvel.SetName("X-velocity")
xvel.SetNumberOfComponents(1)
xvel.SetNumberOfValues(Np)

# Also create vel DataSet
for i in range(0, Np):
    points.InsertPoint(i, X[i], Y[i], Z[i])
    xvel.SetValue(i, Xv[i])
        
# Create unstructured grid object
profile = vtk.vtkUnstructuredGrid()
profile.SetPoints(points)
profile.GetPointData().SetScalars(xvel)


# Option to subsample the points using MaskPoints
subsamp = 0
if (subsamp == 1):
    ptMask = vtk.vtkMaskPoints()
    ptMask.SetInput(profile)
    ptMask.SetOnRatio(3)
    ptMask.RandomModeOff()
    ptMask.GenerateVerticesOn()
    
    # perform delaunay on points
    delny = vtk.vtkDelaunay3D()
    delny.SetInput(ptMask.GetOutput())
    delny.SetTolerance(0.0001)
    delny.SetAlpha(0)
    delny.BoundingTriangulationOff()
    
else:
    # perform delaunay on points
    delny = vtk.vtkDelaunay3D()
    delny.SetInput(profile)
    delny.SetTolerance(0.0001)
    delny.SetAlpha(0.002)
    delny.BoundingTriangulationOff()
    
# Extract convex hull data
ch = vtkDataSetSurfaceFilter()
ch.SetInputConnection(delny.GetOutputPort())
ch.Update()

chOUT = vtkPolyDataWriter()
chOUT.SetFileName("ConvexHull.vtk")
chOUT.SetInput(ch.GetOutput())
chOUT.Write()

# Copy to 'new' Unstructured Grid
us = vtk.vtkUnstructuredGrid()
delny.Update()
us.DeepCopy(delny.GetOutputDataObject(0))

# Allocate Scalers to points in Unstructured Grid
Nc = us.GetNumberOfCells()
mat = vtk.vtkFloatArray()
mat.SetName("Material")
mat.SetNumberOfComponents(1)
mat.SetNumberOfValues(Nc)
for i in range(0, Nc):
    mat.SetValue(i, 1)
    
us.GetPointData().SetScalars(xvel)
us.GetCellData().SetScalars(mat)
us.Update()

# write data to file for paraview
vtkDataOut = vtk.vtkUnstructuredGridWriter()
vtkDataOut.SetFileName(Name + "Mesh.vtk")
vtkDataOut.SetInputConnection(us.GetProducerPort())
vtkDataOut.Write()

# Read data in
reader = vtk.vtkUnstructuredGridReader()
reader.SetFileName(Name + "Mesh.vtk")
reader.Update()
vtkDataIn = reader.GetOutput()
