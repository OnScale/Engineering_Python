import scipy.io
import numpy as np
from pyevtk.hl import imageToVTK
from pyevtk.hl import gridToVTK
from pyevtk.hl import pointsToVTK 

mat = scipy.io.loadmat('pmag.mat')
pres = mat['e1_0000000_pmag']
pres = np.ascontiguousarray(pres)

[nx, ny, nz] = np.shape(pres)

dx = 0.5e2 / nx
dy = 0.5e2 / ny
dz = 1e2 / nz

x = numpy.arange(0, 0.5e2, dx)
y = numpy.arange(0, 0.5e2, dy)
z = numpy.arange(0, 1e2, dz)

[Xg, Yg, Zg] = np.meshgrid(x,y,z)

xp = Xg.ravel() 
yp = Yg.ravel()
zp = Zg.ravel() 

prespp = pres.ravel(order='C')

pointsToVTK("pmag_pp", xp, yp, zp, data = {"pressure" : prespp})

gridToVTK("pres_grid", x,y,z, pointData = {"pressure" : pres})

