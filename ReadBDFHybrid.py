# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:41:18 2013

Description: Script to parse bdf files to 
current nastran readable format.

Also acts as converter for short-form (',')

Date: Sept 10th 2013

Author: Gerry Harvey

Update: 1/10/2013:  Free vs Short form check
                    Forces written out to file

"""

# get filename from user - hardcode for now
# Later this will launch a dialog for browsing files
name = "mmap"
ext = ".bdf"
filename = name + ext

# Open new file for re-formatted BDF
fileOUT = open("reformat.bdf", "w")
fileOUT.close()

# Open newfile for nodes and elements
nodeOUT = open("nodes.txt", "w")
nodeOUT.write("geom\n\tskew gcon\n")

tetOUT = open("Tet.txt", "w")
tetOUT.write("tet\n\tbufr 400000\n")

hexOUT = open("Hex.txt", "w")
hexOUT.write("hex\n\tbufr 400000\n")

frcOUT = open("Force.txt", "w")

# No need to close, but may help clashes when switching open mode
nodeOUT.close()
tetOUT.close()
hexOUT.close()
frcOUT.close()

# read current BDF file
fileIN = open (filename, "r")

# Get number of lines in file - not needed
num_lines = sum(1 for line in open(filename))

# Open files needed for output formats
nodeOUT = open("nodes.txt", "a")
fileOUT = open("reformat.bdf", "a")
tetOUT = open("Tet.txt", "a")
hexOUT = open("Hex.txt", "a")
frcOUT = open("Force.txt", "a")

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
        
        #Write Out GRID point in BDF Short Field
        label = "GRID"                  # can replace with nodeLoc[0]
        label = label.ljust(8)

        fileOUT.write('%.8s%.8s%.8s%.8s%.8s%.8s%.8s\n' \
        %(label, nodeLoc[1], nodeLoc[2], nodeLoc[3], nodeLoc[4], nodeLoc[5], nodeLoc[6]))  
        
        
    # Get nodes and materials for Tets
    elif (lineNow.startswith('CTETRA')):
                       
        # Perform 'free-form' or 'short form' check
        if "," in lineNow:
            tetElm = lineNow.split(',')
            
        else:
            tetElm = [lineNow[i:i+n] for i in range(0, len(lineNow), n)]
        
        # Extract Node number, material and 1st 4 nodes
        # Note: can ignore 2nd CTETRA line - midline nodes. Can use '.readlines' in future
        tetNum = int(tetElm[1])
        matNum = int(tetElm[2])
        node1 = int(tetElm[3])
        node2 = int(tetElm[4])
        node3 = int(tetElm[5])
        node4 = int(tetElm[6])
        
        # Write out Element list
        tetOUT.write('\t%s %s %d %d %d %d\n' \
        %("gcon", "mat1", node1, node2, node3, node4) )
        
        # Write out ELEMENTS in BDF Short Form
        label = "CTETRA"                    # can replace with tetElm[0]

        fileOUT.write('%-8s%-8d%-8d%-8d%-8d%-8d%-8d\n' \
        %(label, tetNum, matNum, node1, node2, node3, node4))
		
    elif (lineNow.startswith('CHEXA')):
        
        # HEX elements split over 2 lines so read next line and add
        lineNxt = fileIN.readline()

        # Perform 'free-form' or 'short form' check
        if "," in lineNow:
            hexElm = lineNow.split(',') + lineNxt.split(',')
            
        else:
            hexElm = [lineNow[i:i+n] for i in range(0, len(lineNow), n)]  \
            + [lineNxt[i:i+n] for i in range(0, len(lineNxt), n)]       
        
        # Extract Node number, material and 1st 8 nodes
        hexNum = int(hexElm[1])
        matNum = int(hexElm[2])
        node1 = int(hexElm[3])
        node2 = int(hexElm[4])
        node3 = int(hexElm[5])
        node4 = int(hexElm[6])
        node5 = int(hexElm[7])
        node6 = int(hexElm[8])
        node7 = int(hexElm[10])
        node8 = int(hexElm[11])
        
        # Write out Element list
        hexOUT.write('\t%s %s %d %d %d %d %d %d %d %d\n' \
        %("gcon", "mat1", node1, node2, node3, node4, node5, node6, node7, node8) )
        
        # Write out ELEMENTS in BDF Short Form
        # will have to split two lines to be formatted correctly
        label = "CHEXA"                   
        fileOUT.write('%-8s%-8d%-8d%-8d%-8d%-8d%-8d%-8d%-8d\n%-8s%-8d%-8d\n' \
        %(label, hexNum, matNum, node1, node2, node3, node4, node5, node6, "", node7, node8))
        
    elif (lineNow.startswith('CPENTA')):
        
        # HEX elements split over 2 lines so read next line and add
        lineNxt = fileIN.readline()

        # Perform 'free-form' or 'short form' check
        if "," in lineNow:
            hexElm = lineNow.split(',') + lineNxt.split(',')
            
        else:
            hexElm = [lineNow[i:i+n] for i in range(0, len(lineNow), n)]  \
            + [lineNxt[i:i+n] for i in range(0, len(lineNxt), n)] 
        
        # Extract Node number, material and 1st 8 nodes
        hexNum = int(hexElm[1])
        matNum = int(hexElm[2])
        node1 = int(hexElm[3])
        node2 = int(hexElm[4])
        node3 = int(hexElm[5])
        node4 = int(hexElm[5])
        node5 = int(hexElm[6])
        node6 = int(hexElm[7])
        node7 = int(hexElm[8])
        node8 = int(hexElm[8])
        
        """
        will need logic to find out which point is would be shared for the
        degenerate HEX element
        """
        
        # Write out Element list
        hexOUT.write('\t%s %s %d %d %d %d %d %d %d %d\n' \
        %("gcon", "mat1", node1, node2, node3, node4, node5, node6, node7, node8) )
        
        # Write out ELEMENTS in BDF Short Form - split into 2 lines
        label = "CHEXA"                    
        fileOUT.write('%-8s%-8d%-8d%-8d%-8d%-8d%-8d%-8d%-8d\n%-8s%-8d%-8d\n' \
        %(label, hexNum, matNum, node1, node2, node3, node4, node5, node6, "", node7, node8))
        
        
    elif(lineNow.startswith('FORCE')):
        
        # Perform 'free-form' or 'short form' check
        if "," in lineNow:
            Forces = lineNow.split(',')
            
        else:
            Forces = [lineNow[i:i+n] for i in range(0, len(lineNow), n)]
        
        # Grab Node number from List and write to 'Forces' file
        ForceNode = int(Forces[2])
        
        frcOUT.write("\t%s %d\n" %("gcon", ForceNode))

    if not lineNow: break   #EOF
        
        
# while loops end - Write ENDDATA to reformat.bdf and close all
fileOUT.write("ENDDATA")
fileOUT.close() 

fileIN.close()
fileOUT.close()
nodeOUT.close()
tetOUT.close()
hexOUT.close()
frcOUT.close()
        
        
        
        
        


