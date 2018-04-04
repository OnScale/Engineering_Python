# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:53:44 2013

@author: Gerry Harvey

Description:
    Read in GRID points from nastran format
    Re-order nodes to suit bldgrdo format
        -loop through i, j then k
    Write out a bldgrdo frmt form for Flex import
    
"""
# get filename from user - hardcode for now
# Later this will launch a dialog for browsing files
name = "skew"
ext = ".bdf"
filename = name + ext

output = "skew_reform.bdf"

# Open newfile for nodes and elements
nodeOUT = open("nodes.txt", "w")
nodeOUT.close()

# read current BDF file
fileIN = open (filename, "r")

gridpoints = 0

# Logic for parsing file
while True:
    
    # Update current line    
    lineNow = fileIN.readline()
    
    """
        Code to look for 8/16 char delimiter for splitting:
            n=8
            [lineNow[i:i+n] for i in range(0, len(line), n)]
            
        Can be used in a case statement at start to check for format
    """
       
    # Get X Y Z node locations from GRID
    if (lineNow.startswith('GRID')):
        
        # Create list of strings on line
        nodeLoc = lineNow.split(',')
        
        
        # extract node number, X, Y and Z loc - real numbers
        nodeNum = float(nodeLoc[1]); int(nodeNum)
        xLoc = float(nodeLoc[3])
        yLoc = float(nodeLoc[4])
        zLoc = float(nodeLoc[5])
        
        # Write Out Node List - insert TAB at start if final export
        nodeOUT = open("nodes.txt", "a")
        nodeOUT.write('\t%f %f %f\n' \
        %(xLoc, yLoc, zLoc) )
        nodeOUT.close()
        
        #Get total number of grid points
        gridpoints = gridpoints + 1
        
        """
            Can populate on the fly but would need some list into lists
        """
        
    if not lineNow: break   #EOF
    
# close out files
nodeOUT.close()





         
        
    
