# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:44:54 2014

@author: adminGH

Script to remove over-riding table format
of html files. Will allow better creation
of printed documentation and formatting
with ROBOHELP
"""

"""
function to get files and paths
"""
def subdir ():
    root = "\WORK\Python"
    path = os.path.join(root, "HTML")

    # create list to store file names
    fname = []
    fold = []

    for path, subdirs, files in os.walk(path):
        for name in files:        
            if ".htm" in name:        
                fname.append(name)
                fold.append(path)
                print os.path.join(path, name)
            
    return fname, fold

[nfile, nfolder] = subdir()




# open file to edit
filename = "TableTest.htm"
fileIN = open(filename, "r")

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
fileOUT = open("TableOut.htm", "w")
for i in html:
    fileOUT.write("%s" % i)  
fileOUT.close()
    
