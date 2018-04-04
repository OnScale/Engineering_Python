# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 14:45:58 2014

@author: adminGH
"""

data={}
figure(facecolor='w')
for i in range(5,35,5):
    data[i]=genfromtxt('FFdsp.' + str(i) + '.txt')
    plot(data[i][:,0], data[i][:,1], label='ratio '+ str(i))
    legend(loc='upper right')
    
figure(facecolor='w')
for i in range(5,20,5):
    plot(data[i][:,0], data[i][:,1], label='ratio '+ str(i))
    legend(loc='upper right')