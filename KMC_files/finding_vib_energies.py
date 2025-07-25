# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:22:20 2024

@author: shara
"""

import os

import numpy as np

  

###########Vib energies array############################

def vibrational_energies(OUTCAR_dir,number_of_modes):
  
    vib_energies = np.zeros(number_of_modes)
    
    fulldir = os.path.join(OUTCAR_dir,'OUTCAR')
    
    fid = open(fulldir,'r')
    
    text1 = 'f  ='
    text2 = 'meV'
    count = 1
    
    while 1:
        textline = fid.readline()
        if text1 in textline and text2 in textline and count<= number_of_modes:
            textline = textline.split()
            vib_energies[count-1] = float(textline[9])/1000 ######converting to eV
            count = count + 1
        
        if(count>number_of_modes):
            return vib_energies
            break



   
