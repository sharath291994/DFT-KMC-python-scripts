# -*- coding: utf-8 -*-

"""
Created on Thu Feb 29 15:09:01 2024

@author: shara

"""

from ase.visualize import view

from ase.io import read, write

import os 

os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\POSCAR_input_files\ML_Trajectory_files\CH3O_diss_CH3_O\CH3O_diss_CH3_O_TS")

atoms1 = read("initial.traj")

atoms2 = read("final.traj")


view(atoms1)

view(atoms2)

#os.chdir("C:/Project3_project4/Project4_Potassium_calc_PBE_D3/ML_NEB_Diffusion_TS/Failed_calc/Ongoing_calc/CH_diff_TS_kmod/optimized_structures")

#os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\TS_calc\IS_FS_CO2diss")

#write('Coordinates_CO2_V8C7.xyz',atoms)


#os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\IS_calc_mod\Temp\Addn_calc_Methanol_25_Mar\CH3OH_V8C7_conf3")

#atoms_POSCAR = read("POSCAR")

#view(atoms_POSCAR)


#os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\IS_calc_mod\Temp\Addn_calc_Methanol_25_Mar\CH3OH_V8C7_conf4")

#atoms_POSCAR = read("POSCAR")

#view(atoms_POSCAR)


#os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\IS_calc_mod\Temp\Addn_calc_Methanol_25_Mar\CH3OH_V8C7_conf5")

#atoms_POSCAR = read("POSCAR")

#view(atoms_POSCAR)


#os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\IS_calc_mod\Temp\Addn_calc_CO_O_system\COdif")

#atoms_POSCAR = read("POSCAR")

#view(atoms_POSCAR)


#os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\IS_calc_mod\Temp\Addn_calc_CO_O_system\COdis_v1")

#atoms_POSCAR = read("POSCAR")

#view(atoms_POSCAR)


#os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\IS_calc_mod\Temp\Addn_calc_CO_O_system\COdis_v2")

#atoms_POSCAR = read("POSCAR")

#view(atoms_POSCAR)



#toms2_CONTCAR = read("CONTCAR") 

#view(atoms_POSCAR)

#os.chdir("C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/POSCAR_input_files/")

#$ase gui CONTCAR