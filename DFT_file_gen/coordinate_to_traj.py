# -*- coding: utf-8 -*-

"""
Created on Mon Mar  4 17:19:43 2024

@author: shara
"""

import os

from ase.io import read, write

from ase.visualize import view

###############CO_O directory###########


##var1 D1

os.chdir('C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\POSCAR_input_files\ML_Trajectory_files\CH3O_diss_CH3_O')

atoms_final = read('CONTCAR_FS')

currentdir = os.curdir

##var2D1

os.chdir('C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\POSCAR_input_files\ML_Trajectory_files\CH3O_diss_CH3_O') 

write('final.traj',atoms_final)

view(atoms_final)


###############CO2 directoryy###########

##var3D1
os.chdir('C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\POSCAR_input_files\ML_Trajectory_files\CH3O_diss_CH3_O')

atoms_initial = read('CONTCAR_IS')

currentdir = os.curdir

##var4D1
os.chdir('C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\POSCAR_input_files\ML_Trajectory_files\CH3O_diss_CH3_O')

write('initial.traj',atoms_initial)

view(atoms_initial)


#view(atoms_mod)



