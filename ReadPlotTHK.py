# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 02:20:33 2014

@author: adminGH

Read in multiple files to an array then plot
"""

# figure set-up
plt.close('all')
plt.figure(facecolor='w')
run_name = 'Water Load - Perfect Matched Backing - No Absr'

# useful vars
thk = [0.1, 0.25, 0.5, 1, 5]
nfiles = len(thk)

# create string for file name and loading
pre = 'back_pzt.'
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
for i in range(len(thk)):
    
    # create index and convert to string     
    n = str(i)
    filename = pre + n + suf
    
    # create labels
    title = 'back_thk = '
    record = str(thk[i])
    titles = title + record + 'mm'
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

    

    
    
    
