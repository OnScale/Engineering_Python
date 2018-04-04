import numpy as np
from matplotlib import pyplot as plt
path=os.getcwd()
os.chdir(path)
print path
filhdr = "presvals.hdr"
filbin = "presvals.bin"
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
# I am assuming nd3 = 1; Fortran storage ordering
pres = pp.reshape(nd1,nd2,nd3, order='F')
print(pres.shape)
plt.imshow(pres,interpolation='nearest')
plt.show()

    