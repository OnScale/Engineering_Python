# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 16:11:59 2014

@author: adminGH
"""

nfrq = linspace(1, 20, 20).astype(int)
preW = 'freq_watr.'
preS = 'freq_sand.'
suf = '.dat'

DirW  = []
NptsW = []

DirS  = []
NptsS = []
  
for idx, val in enumerate(nfrq):
    # Open figure    
    figure(facecolor='w')    
    
    # Loop through files and load data    
    labl = val * 2.5
    fileW = preW + val.astype(str) + suf
    dataW = loadtxt(fileW)
    
    fileS = preS + val.astype(str) + suf
    dataS = loadtxt(fileS)
    
    # Normalise, shift and create Array    
    AmaxW = max(dataW[:,1])
    dataW[:,1] = dataW[:,1]/AmaxW
    dataW[:,0] = dataW[:,0] - 90
    NptsW.append(dataW[:,0])
    DirW.append(dataW[:,1])
    
    AmaxS = max(dataS[:,1])
    dataS[:,1] = dataS[:,1]/AmaxS
    dataS[:,0] = dataS[:,0] - 90
    NptsS.append(dataS[:,0])
    DirS.append(dataS[:,1])
    
    # Plot to specific figure and save    
    titl = 'Frequency ' + labl.astype(str) + 'kHz'
    title(titl)
    xlim(-90, 90)
    xlabel('Degrees')
    ylim(0, 1)
    ylabel('Normalised Amplitude') 
    plot(NptsW[idx], DirW[idx], label='Water')
    plot(NptsS[idx], DirS[idx], label='Sand')
    legend(loc='upper right')
    
    ImgFileName = 'Watr Vs Sand' + labl.astype(str) + '.png'
    savefig(ImgFileName, format='png')
    clf()
    close()
    
