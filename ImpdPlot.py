# -*- coding: utf-8 -*-
"""
Created on Fri Aug 01 11:29:19 2014

@author: adminGH

Simple script to read impedance data and plot
"""
#import os
#os.system('pzflex disc.flxinp')
#os.system('review postpro.revinp')

data = loadtxt('PZT only.txt', skiprows=8, delimiter='\t', dtype='float')
flex = loadtxt('flex.impd.txt')
optm = loadtxt('flex.impd.optm.txt')
imlf = loadtxt('impdlf.txt', skiprows=1)
imhf = loadtxt('impdhf.txt', skiprows=1)


figure(facecolor='w')
title('Radial Mode')
yscale('log')
plot(data[:,0], data[:,1], 'b', label='Measurement' )
plot(flex[:,0], flex[:,1], 'g', label='PZFlex - Original Data')
plot(imlf[:,0], imlf[:,1], 'r', label='PZFlex - Optimised Data')
legend(loc='upper right')
xlim(xmin=1000); xlim(xmax=8.5e5)
ylim(ymin=1); ylim(ymax=1e5)
xlabel('Frequency (Hz)')
ylabel('Impedance Magnitude (Ohms)')

figure(facecolor='w')
legend(loc='upper right')
yscale('log')
title('Thickness Mode')
plot(data[:,0], data[:,1], 'b', label='Measurement' )
plot(flex[:,0], flex[:,1], 'g', label='PZFlex - Original Data')
plot(imhf[:,0], imhf[:,1], 'r', label='PZFlex - Optimised Data')
legend(loc='upper right')
xlim(xmin=0.25e6); xlim(xmax=3.25e6)
ylim(ymin=1); ylim(ymax=1e5)
xlabel('Frequency (Hz)')
ylabel('Impedance Magnitude (Ohms)')

