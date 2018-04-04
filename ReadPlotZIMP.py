# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 02:20:33 2014

@author: adminGH

Read in multiple files to an array then plot
"""

# figure set-up
plt.close('all')
plt.figure(facecolor='w')
run_name = 'Steel - 0.5mm backing, Zimp sweep - No Absr'

# Set up list of backing impedances
nfiles=10
zimp = [None]*nfiles
zval = 5
for i in range(0, 10):
    zimp[i] = zval
    zval = zval + 5

# create string for file name and loading
pre = 'back_zimp.'
suf = '.dat'

filename = pre + '0' + suf

# read in file to get dimensions
time = loadtxt(filename, usecols=[0])
nlen = size(time)
nsamp = nlen / 4

# create array to read records into
data = zeros((nfiles,nlen))
data[0,:] = time

# loop through files store data in colms
for i in range(len(zimp)):
    
    # create index and convert to string     
    n = str(i)
    filename = pre + n + suf
    
    # create labels
    title = 'back_Zimp = '
    record = str(zimp[i])
    titles = title + record + 'MRay'
    print titles
    
    # read pressue data into array rows
    data[i,:]=loadtxt(filename, usecols=[1])
    
    # data, hold and label    
    plt.subplot(211)    
    plt.plot(time, data[i,:], label=titles)
    plt.legend(loc=4)
    plt.title(run_name)
    plt.subplot(212)
    plt.plot(time[0:nsamp], data[i,0:nsamp], label=titles)
    plt.title('1/4 run time zoom')
    plt.hold(True)

    

    
    
    
