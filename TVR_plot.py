# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 14:44:59 2014

@author: adminGH
"""

stck3d = loadtxt('TVR_15L_2mm.csv', delimiter=',', dtype='float')
curv3d = loadtxt('TVR_15L_2mm_curv.csv', delimiter=',', dtype='float')

figure(facecolor='w')
title('TVR Comparison')
#yscale('log')
plot(stck3d[:,0], stck3d[:,1], 'b', label='Flat' )
plot(curv3d[:,0], curv3d[:,1], 'g', label='Curve')
legend(loc='upper right')
ylim(ymin=50); ylim(ymax=150)
xlabel('Frequency (Hz)')
ylabel('TVR @ 1m')

