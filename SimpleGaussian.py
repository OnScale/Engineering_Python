# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:34:23 2014

@author: adminGH
"""

#create array of elements
Xelem = np.linspace(0,10,100)
Xcent = 5

# Define Gaussian function
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    
# Call function to create distributions
for mu, sig in [(Xcent,2)]:
    Amp = gaussian(Xelem, mu, sig)
    


 
