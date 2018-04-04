# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:29:15 2014

@author: adminGH

Script to get subdirectories and filenames

"""


root = os.getcwd()
path = os.path.join(root)

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
                
                # first table tag entry
                ChkTop = "<table"
                end = ">"
                
                # last table tag entry
                ChkBot = "</table>"
                
                # serach for tags and remove top <table>
                for i in html:
                    if ChkTop in i: 
                        top =  i[:-len(end)]
                        html.remove(i)       
                        break
                
                # reverse html to remove bottom tag
                list.reverse(html)
                
                for i in html:
                    if ChkBot in i:
                        bot = i[:-len(end)]
                        html.remove(i)
                        break
                    
                # reverse back to original format
                list.reverse(html)
                
                # overwrite existing file with new list
                outFile = name
                fileOUT = open(os.path.join(path, outFile), "w")
                for i in html:
                    fileOUT.write("%s" % i)  
                fileOUT.close()
                




