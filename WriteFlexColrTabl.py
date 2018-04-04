# -*- coding: utf-8 -*-
"""
Created on Thu Oct 02 16:03:38 2014

@author: adminGH
"""
colr = loadtxt('redblue.txt')
colr = colr/255
colr = colr[::7]
NColr = size(colr[:,0])
colrSTR = colr.astype('|S5')
fileOUT = open('flex.colr', 'w')
fileOUT = open('flex.colr', 'a')
n = 1
for i in range(NColr):
    fileOUT.write('\t %s %s %d  %s %s %s \n' \
    %("colr", "user", n, colrSTR[i,0],colrSTR[i,1],colrSTR[i,2]))
    n += 1
fileOUT.close()
    