# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 11:27:29 2015

@author: Gerry Harvey

Convert Full name to: Sal / First / Name
"""

isaf = genfromtxt('ISAF2010.txt', dtype=str, delimiter='\t')
names = isaf[:,0].tolist()
sal, first, last = [], [], []
for name in names:        
    sal = append(sal, name.split()[0])
    first = append(first, name.split()[1])
    item = name.split(' ', 2)[2:]
    if item:
        last = append(last, name.split(' ', 2)[2:])
    else:
        print name
        
final = vstack((sal, first, last, isaf[:,1], isaf[:,2])).T
savetxt('ISAF2010_fmt.csv', final, fmt='%s', delimiter=',')