# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:29:15 2014

Iterate through directory and convert tiff to png

"""

import os
import sys
import PIL.Image
sys.modules['Image'] = PIL.Image

# Current directory
root = os.getcwd()

# Iterate through tiff files in Dir and convert
for file in os.listdir(root):      
    if ".tiff" in file:        
    
        fname, fext = os.path.splitext(file)
        im = PIL.Image.open(file)
        im.save(fname + '.png')
                
                




