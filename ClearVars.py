# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 02:19:54 2014

@author: adminGH

Clear all variables

"""

def clear():
    os.system('cls')
    return none
    
cls = clear

def clear_all():
    cls()
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue:
            if 'func' in str(globals()var[]):continue:
                if 'module'in str(globals()var[]):continue:
                    
                    del globals()[var]
            
