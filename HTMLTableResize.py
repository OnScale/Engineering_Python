# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\adminGH\.spyder2\.temp.py
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:29:15 2014

@author: adminGH

Script to get subdirectories and filenames

"""

root = os.getcwd()
path = os.path.join(root, "resize_table")

# create list to store file names
fname = []
fold = []

for path, subdirs, files in os.walk(path):
    
    # create lists of folders                
    fold.append(path)
    
    for name in files:        
            if ".htm" in name:        
                
                # create lists of files        
                fname.append(name)
                
                # Open html files for editing
                fileIN = open(os.path.join(path, name), "r")
                
                # read in Mylines variable
                html = fileIN.readlines()
                fileIN.close()
                
                # use tags to capture table set-up as string
                widOld = 'width="1165"'
                widNew = 'width="100%"'
                
                """
                Note: if 'width' NOT = "100%" then replace
                """
                
                # serach for everything between <table...>
                for line in html:
                    if widOld in line:
                        html = [line.replace(widOld,widNew) for line in html]                      
                        break
                
                # overwrite existing file with new list
                outFile = name
                fileOUT = open(os.path.join(path, outFile), "w")
                for i in html:
                    fileOUT.write("%s" % i)  
                fileOUT.close()






