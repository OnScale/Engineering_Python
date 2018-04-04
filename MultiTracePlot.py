# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 19:48:21 2014

@author: adminGH

Read in multiple files and plot in a single plot.
"""

cav = linspace(750, 15000, 20).astype(int)
pre = 'Vrx.4mm.300um.'
suf = 'um.dat'

Vrx = []
Time = []
figure(facecolor='w')
for idx, val in enumerate(cav):
    filename = pre + val.astype(str) + suf
    data = loadtxt(filename)
    Time.append(data[:,0])
    Vrx.append(data[:,1]) 
    plot(Time[idx], Vrx[idx], label=val)
    
title('VRx for 0.75mm shifts in Chamber Length')
xlabel('Time (s)')
ylabel('Voltage (V)')
legend(loc='upper right')
    
    
    
    
