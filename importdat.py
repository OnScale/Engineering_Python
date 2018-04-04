import numpy as np
from matplotlib import pyplot as plt
from pyevtk.hl import gridToVTK 

path = os.getcwd()
filhdr = "vtkOut.hdr"
filbin = "vtkOut.bin"

# Read header - Flex data manager array definition
with open(filhdr,"r") as f:
    for line in f:
        name, ndim, nd1, nd2, nd3, typ = line.split()
        ndim = int(ndim);
        nd1 = int(nd1);
        nd2 = int(nd2);
        nd3 = int(nd3);

print(name,ndim,nd1,nd2,nd3,typ)

# Load array at once
pp = np.fromfile(filbin,typ,-1)

# Fortran storage ordering
prmx = pp.reshape(nd1,nd2,nd3,order='F')

# Dimensions 
lx, ly, lz = 0.5600000E-02, 0.7680000E-01, 0.4000000E-02  
dx, dy, dz = lx/nd1, ly/nd2, lz/nd3 

ncells = nd1 * nd2 * nd3 
npoints = (nd1 + 1) * (nd2 + 1) * (nd3 + 1) 

# Coordinates 
x = np.arange(0, lx, dx, dtype='float32') 
y = np.arange(0, ly, dy, dtype='float32') 
z = np.arange(0, lz, dz, dtype='float32') 

# Export to VTK
gridToVTK("./Strct", x, y, z, cellData = {"pressure" : prmx})     