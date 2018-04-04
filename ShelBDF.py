# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:41:18 2013

Description: Script to gcon shel bdf files to flex format

Date: June 1st 2015

Author: Gerry Harvey

"""

# get filename from user - hardcode for now
# Later this will launch a dialog for browsing files
name = "CarCoarse"
ext = ".bdf"
filename = name + ext


# Open newfile for nodes and elements
nodeOUT = open("nodes.txt", "w")
shelOUT = open("shel.txt", "w")
glueOUT = open("glue.txt", "w")

# No need to close, but may help clashes when switching open mode
nodeOUT.close()
shelOUT.close()
glueOUT.close()

# read current BDF file
fileIN = open (filename, "r")

# Get number of lines in file - not needed
num_lines = sum(1 for line in open(filename))

# Open files needed for output formats
nodeOUT = open("nodes.txt", "a")
shelOUT = open("shel.txt", "a")
glueOUT = open("glue.txt", "a")

# Set number of characters in columns
n = 8

# Logic for parsing file
while True:
    
    # Update current line    
    lineNow = fileIN.readline()
        
    # Get X Y Z node locations from GRID
    if (lineNow.startswith('GRID')):
        
        # Perform 'free-form' or 'short form' check
        if "," in lineNow:
            
            # Create list of strings on line
            nodeLoc = lineNow.split(',')
            nitems = len(nodeLoc)
            
        else:
            nodeLoc = [lineNow[i:i+n] for i in range(0, len(lineNow), n)]
            nitems = len(nodeLoc)
        
        i = 1
        for i in range(1,nitems):        
            # Strip Whitespace from strings        
            nodeLoc[i] = nodeLoc[i].lstrip()

            # Justify strings correctly for formatting
            nodeLoc[i] = nodeLoc[i].rjust(8)            
            i = i+1

        # extract node number, X, Y and Z loc - real numbers
        nodeNum = float(nodeLoc[1]); int(nodeNum)
        xLoc = float(nodeLoc[3])
        yLoc = float(nodeLoc[4])
        zLoc = float(nodeLoc[5])
        
        # Write Out Node List
        nodeOUT.write('\t%s %d %f %f %f\n' \
        %("gcon",nodeNum, xLoc, yLoc, zLoc) )
        
    # Get nodes and materials for Quad Shells
    elif (lineNow.startswith('CQUAD4')):
                       
        # Perform 'free-form' or 'short form' check
        if "," in lineNow:
            quadElm = lineNow.split(',')
            
        else:
            quadElm = [lineNow[i:i+n] for i in range(0, len(lineNow), n)]
        
        # Extract Node number, material and 1st 4 nodes
        quadNum = int(quadElm[1])
        matNum = int(quadElm[2])
        node1 = int(quadElm[3])
        node2 = int(quadElm[4])
        node3 = int(quadElm[5])
        node4 = int(quadElm[6])
        
        # Write out Element list
        shelOUT.write('\t%s %s %d %d %d %d\n' \
        %("gcon", "mbrn", node1, node2, node3, node4) )
        
        # Write out Glue list
        glueOUT.write('\t%s %s %d %d %d %d\n' \
        %("master", "surf", node1, node2, node3, node4) )
        		
    elif (lineNow.startswith('CTRIA3')):
        
        # Perform 'free-form' or 'short form' check
        if "," in lineNow:
            quadElm = lineNow.split(',')
            
        else:
            quadElm = [lineNow[i:i+n] for i in range(0, len(lineNow), n)]
        
        # Extract Node number, material and 1st 4 nodes
        quadNum = int(quadElm[1])
        matNum = int(quadElm[2])
        node1 = int(quadElm[3])
        node2 = int(quadElm[4])
        node3 = int(quadElm[5])
        node4 = int(quadElm[5])
        
        # Write out Element list
        shelOUT.write('\t%s %s %d %d %d %d\n' \
        %("gcon", "mbrn", node1, node2, node3, node4) )
        
        # Write out Glue list
        glueOUT.write('\t%s %s %d %d %d %d\n' \
        %("master", "surf", node1, node2, node3, node4) )
        

    if not lineNow: break   #EOF
        
        
# while loops end - close all

fileIN.close()
nodeOUT.close()
shelOUT.close()
glueOUT.close()
        
        
        
        
        


