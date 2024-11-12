# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:42:49 2024

@author: shara
"""

########################Pl###########################################################################################

from ase.thermochemistry import IdealGasThermo

from ase.io import read

from ase.thermochemistry import HarmonicThermo

import numpy as np

import pandas as pd 

import matplotlib.pyplot as plt

import os

#####################################################################################################################



############################################Complete the diagram tomorrow#############################################################

def Energyfileparse(Finalpath):
 fid = open(Finalpath)
 Energy = float(fid.read())
 return Energy


############################To be checked again (with the MATLAB scripts) #############################################################################

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "V8C7_clean/" 
                                        
energyfiletot = "energyV8C7_clean";                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_V8C7_clean  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK


Temp = 723.00     ######in Kelvin###########

Pressure = 10^(5)  ######in pascals############


#########################################################################################################

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/gas_phase_calc/"

subfolddirtot = "CO2_gasph/" 
                                        
energyfiletot = "energyCO2_gas_phase_xc_PE_D3";                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CO2_gasph  = -22.98455916 #To be changed later



#########################################################################################################

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/gas_phase_calc/"

subfolddirtot = "CH3OH_gasph/" 
                                        
energyfiletot = "energyCH3OH_gasph";                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CH3OH_gasph  = -30.23303226  #To be changed later





###############CO2 dissociation# (Initial state)####################################################################

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "CO2_conf2_V8C7/" 
                                        
energyfiletot = "energyCO2_conf2_V8C7";                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CO2_conf2_V8C7  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK




##########CO2 dissociation# (Final state)####################################################################################

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "CO_O_V8C7_mod/" 
                                        
energyfiletot = "energyCO_O_V8C7_mod"                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CO_O_FS  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK



#########CO dissociation# (Final state)#################

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "COdis_conf3/" 
                                        
energyfiletot = "energyCOdis_conf3"                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_C_O_FS  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK




#########CH3OH (Final state)#################

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "CH3OH_V8C7_conf4/" 
                                        
energyfiletot = "energyCH3OH_V8C7_conf4"                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CH3OH_IS_conf4_V8C7  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK



#########CH3O + H (Final state)#################

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "CH3OHdiss_final_4/" 
                                        
energyfiletot = "energyCH3OHdiss_final_4"                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CH3O_H_FS_final4_V8C7  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK


#########CH3 + O + H ############

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "CH3_O_FS/" 
                                        
energyfiletot = "energyCH3_O_FS"                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CH3_O_FS_V8C7  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK


#########CH2 + 2H + O############

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "CH2_H_FS/" 
                                        
energyfiletot = "energyCH2_H_FS"                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CH2_H_FS_V8C7  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK



#########CH + 3H + O############

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "CH_H_OH_assis_FS/" 
                                        
energyfiletot = "energyCH_H_OH_assis_FS"                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_CH_H_FS_V8C7  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK



#########C + 4H + O############

currentdir = "C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/IS_calc_mod/"

subfolddirtot = "C_H_V8C7_system1/" 
                                        
energyfiletot = "energyC_H_V8C7_system1"                                                 

DFTTotalEnergygaspath = currentdir + subfolddirtot + energyfiletot;  #input1 OK 
                                                            
energy_C_H_FS_V8C7  = Energyfileparse(DFTTotalEnergygaspath) #input2 OK



############Converged ML-NEB.traj generated########################################################################

currentdir = os.getcwd()

os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\TS_calc\CO2_diss_TS_mod3_contd")

df_CO2_diss_data = pd.read_csv("results_neb.csv")

os.chdir(currentdir)

Textline_CO2_diss_first_image =  df_CO2_diss_data['# Path distance (Angstrom)'][0]

Textline_CO2_diss_first_image = Textline_CO2_diss_first_image.split() 

Formation_energy_CO2_diss_first_image = float(Textline_CO2_diss_first_image[1])


Textline_CO2_diss_TS_image =  df_CO2_diss_data['# Path distance (Angstrom)'][3]

Textline_CO2_diss_TS_image = Textline_CO2_diss_TS_image.split() 

Formation_energy_CO2_diss_TS_image = float(Textline_CO2_diss_TS_image[1])


Textline_CO2_diss_last_image =  df_CO2_diss_data['# Path distance (Angstrom)'][9]

Textline_CO2_diss_last_image = Textline_CO2_diss_last_image.split() 

Formation_energy_CO2_diss_last_image = float(Textline_CO2_diss_last_image[1])


Act_fwd_barrier_CO2_diss = Formation_energy_CO2_diss_TS_image - Formation_energy_CO2_diss_first_image

Act_rev_barrier_CO2_diss = Formation_energy_CO2_diss_TS_image - Formation_energy_CO2_diss_last_image

Rxn_energy_CO2_diss_NEB = Formation_energy_CO2_diss_last_image -  Formation_energy_CO2_diss_first_image



#####Converged ML-NEB.traj generated#######

os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\TS_calc\CO_diss_TS")

df_CO_diss_data = pd.read_csv("results_neb.csv")

os.chdir(currentdir)


Textline_CO_diss_first_image =  df_CO_diss_data['# Path distance (Angstrom)'][0]

Textline_CO_diss_first_image = Textline_CO_diss_first_image.split() 

Formation_energy_CO_diss_first_image = float(Textline_CO_diss_first_image[1])


Textline_CO_diss_TS_image =  df_CO_diss_data['# Path distance (Angstrom)'][6]

Textline_CO_diss_TS_image = Textline_CO_diss_TS_image.split() 

Formation_energy_CO_diss_TS_image = float(Textline_CO_diss_TS_image[1])


Textline_CO_diss_last_image =  df_CO_diss_data['# Path distance (Angstrom)'][9]

Textline_CO_diss_last_image = Textline_CO_diss_last_image.split() 

Formation_energy_CO_diss_last_image = float(Textline_CO_diss_last_image[1])


Act_fwd_barrier_CO_diss = Formation_energy_CO_diss_TS_image - Formation_energy_CO_diss_first_image

Act_rev_barrier_CO_diss = Formation_energy_CO_diss_TS_image - Formation_energy_CO_diss_last_image

Rxn_energy_CO_diss_NEB = Formation_energy_CO_diss_last_image -  Formation_energy_CO_diss_first_image

##########CO2 dissociation# (Final state)####################################################################################


##############CH3OH dissociation##########################################################################################################################################################

os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\TS_calc\CH3OH_diss_TS4")

df_CH3OH_diss_CH3O_H_data = pd.read_csv("results_neb.csv")

textline_CH3OH_diss_CH3O_H_first_image = df_CH3OH_diss_CH3O_H_data['# Path distance (Angstrom)'][0]

textline_CH3OH_diss_CH3O_H_first_image = textline_CH3OH_diss_CH3O_H_first_image.split()

Formation_energy_CH3OH_diss_CH3O_H_first_image = float(textline_CH3OH_diss_CH3O_H_first_image[1])


textline_CH3OH_diss_CH3O_H_TS_image = df_CH3OH_diss_CH3O_H_data['# Path distance (Angstrom)'][4]

textline_CH3OH_diss_CH3O_H_TS_image = textline_CH3OH_diss_CH3O_H_TS_image.split()

Formation_energy_CH3OH_diss_CH3O_H_TS_image = float(textline_CH3OH_diss_CH3O_H_TS_image[1])


textline_CH3OH_diss_CH3O_H_last_image = df_CH3OH_diss_CH3O_H_data['# Path distance (Angstrom)'][9]

textline_CH3OH_diss_CH3O_H_last_image = textline_CH3OH_diss_CH3O_H_last_image.split()

Formation_energy_CH3OH_diss_CH3O_H_last_image = float(textline_CH3OH_diss_CH3O_H_last_image[1])

########################################################################################################################################################################



######(CH3O dissociation CH3O = CH3 + O)####Not completely converged (ML-NEB.traj file has not been generated)############################################################################################################################################################

os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\TS_calc\CH3O_diss_CH3_O_TS_alt_contd2")

df_CH3O_diss_CH3_O_data = pd.read_csv("results_neb.csv")

textline_CH3O_diss_CH3_O_first_image = df_CH3O_diss_CH3_O_data['# Path distance (Angstrom)'][0]

textline_CH3O_diss_CH3_O_first_image = textline_CH3O_diss_CH3_O_first_image.split()

Formation_energy_CH3O_diss_CH3_O_first_image = float(textline_CH3O_diss_CH3_O_first_image[1])


#textline_CH3O_diss_CH3_O_TS_image = df_CH3O_diss_CH3_O_data['# Path distance (Angstrom)'][4]

#textline_CH3O_diss_CH3_O_TS_image = textline_CH3O_diss_CH3_O_TS_image.split()

#Formation_energy_CH3O_diss_CH3_O_TS_image = float(textline_CH3O_diss_CH3_O_TS_image[1])

###from dimer
energy_CH3O_diss_CH3_O_TS_image = -604.94167386  

Formation_energy_CH3O_diss_CH3_O_TS_image = energy_CH3O_diss_CH3_O_TS_image - energy_V8C7_clean - energy_CH3OH_gasph 

textline_CH3O_diss_CH3_O_last_image = df_CH3O_diss_CH3_O_data['# Path distance (Angstrom)'][9]

textline_CH3O_diss_CH3_O_last_image = textline_CH3O_diss_CH3_O_last_image.split()

Formation_energy_CH3O_diss_CH3_O_last_image = float(textline_CH3O_diss_CH3_O_last_image[1])



######CH3 = CH2 + H######Converged calc (ML-NEB.traj generated)###################################################################################################################################################

os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\TS_calc\CH3_CH2_H_TS_contd")

df_CH3_diss_CH2_H_data = pd.read_csv("results_neb.csv")

textline_CH3_diss_CH2_H_first_image = df_CH3_diss_CH2_H_data['# Path distance (Angstrom)'][0]

textline_CH3_diss_CH2_H_first_image = textline_CH3_diss_CH2_H_first_image.split()

Formation_energy_CH3_diss_CH2_H_first_image = float(textline_CH3_diss_CH2_H_first_image[1])


textline_CH3_diss_CH2_H_TS_image = df_CH3_diss_CH2_H_data['# Path distance (Angstrom)'][5]

textline_CH3_diss_CH2_H_TS_image = textline_CH3_diss_CH2_H_TS_image.split()

Formation_energy_CH3_diss_CH2_H_TS_image  = float(textline_CH3_diss_CH2_H_TS_image[1])


textline_CH3_diss_CH2_H_last_image = df_CH3_diss_CH2_H_data['# Path distance (Angstrom)'][9]

textline_CH3_diss_CH2_H_last_image = textline_CH3_diss_CH2_H_last_image.split()

Formation_energy_CH3_diss_CH2_H_last_image  = float(textline_CH3_diss_CH2_H_last_image[1])



######CH2 = CH + H####(OH assisted)##Converged calc (ML-NEB.traj generated)###################################################################################################################################################

os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\TS_calc\CH2_diss_TS_traj1")

df_CH2_diss_CH_H_data = pd.read_csv("results_neb.csv")

textline_CH2_diss_CH_H_first_image = df_CH2_diss_CH_H_data['# Path distance (Angstrom)'][0]

textline_CH2_diss_CH_H_first_image = textline_CH2_diss_CH_H_first_image.split()

Formation_energy_CH2_diss_CH_H_first_image = float(textline_CH2_diss_CH_H_first_image[1])

textline_CH2_diss_CH_H_TS_image = df_CH2_diss_CH_H_data['# Path distance (Angstrom)'][6]

textline_CH2_diss_CH_H_TS_image = textline_CH2_diss_CH_H_TS_image.split()

Formation_energy_CH2_diss_CH_H_TS_image = float(textline_CH2_diss_CH_H_TS_image[1])

textline_CH2_diss_CH_H_last_image = df_CH2_diss_CH_H_data['# Path distance (Angstrom)'][9]

textline_CH2_diss_CH_H_last_image = textline_CH2_diss_CH_H_last_image.split()

Formation_energy_CH2_diss_CH_H_last_image = float(textline_CH2_diss_CH_H_last_image[1])



######CH = C + H#####Converged calc (ML-NEB.traj generated)###################################################################################################################################################

os.chdir("C:\Project3_project4\Postdoc_Projects\Project1_V_C\DFT_calc\TS_calc\CH_diss_TS_system1")

df_CH_diss_C_H_data = pd.read_csv("results_neb.csv")

textline_CH_diss_C_H_first_image = df_CH_diss_C_H_data['# Path distance (Angstrom)'][0]

textline_CH_diss_C_H_first_image = textline_CH_diss_C_H_first_image.split()

Formation_energy_CH_diss_C_H_first_image = float(textline_CH_diss_C_H_first_image[1])


textline_CH_diss_C_H_TS_image = df_CH_diss_C_H_data['# Path distance (Angstrom)'][5]

textline_CH_diss_C_H_TS_image = textline_CH_diss_C_H_TS_image.split()

Formation_energy_CH_diss_C_H_TS_image = float(textline_CH_diss_C_H_TS_image[1])


textline_CH_diss_C_H_last_image = df_CH_diss_C_H_data['# Path distance (Angstrom)'][9]

textline_CH_diss_C_H_last_image = textline_CH_diss_C_H_last_image.split()

Formation_energy_CH_diss_C_H_last_image = float(textline_CH_diss_C_H_last_image[1])




########################################################################################################################################################################

Act_fwd_barrier_CH3OH_diss_CH3O_H = Formation_energy_CH3OH_diss_CH3O_H_TS_image - Formation_energy_CH3OH_diss_CH3O_H_first_image

Act_rev_barrier_CH3OH_diss_CH3O_H = Formation_energy_CH3OH_diss_CH3O_H_TS_image - Formation_energy_CH3OH_diss_CH3O_H_last_image

Rxn_energy_CH3OH_diss_CH3O_H_NEB = Formation_energy_CH3OH_diss_CH3O_H_last_image -  Formation_energy_CH3OH_diss_CH3O_H_first_image

#Act_fwd_barrier_CH3O_diss_CH3_O = Formation_energy_CH3O_diss_CH3_O_TS_image - Formation_energy_CH3O_diss_CH3_O_first_image

#Act_rev_barrier_CH3O_diss_CH3_O = Formation_energy_CH3O_diss_CH3_O_TS_image - Formation_energy_CH3O_diss_CH3_O_last_image

Rxn_energy_CH3O_diss_CH3_O_NEB =  Formation_energy_CH3O_diss_CH3_O_last_image -  Formation_energy_CH3O_diss_CH3_O_first_image

Act_fwd_barrier_CH3_diss_CH2_H =  Formation_energy_CH3_diss_CH2_H_TS_image - Formation_energy_CH3_diss_CH2_H_first_image 

Act_rev_barrier_CH3_diss_CH2_H =  Formation_energy_CH3_diss_CH2_H_TS_image  - Formation_energy_CH3_diss_CH2_H_last_image

Rxn_energy_CH3_diss_CH2_H =  Formation_energy_CH3_diss_CH2_H_last_image - Formation_energy_CH3_diss_CH2_H_first_image

Act_fwd_barrier_CH2_diss_CH_H =  Formation_energy_CH2_diss_CH_H_TS_image - Formation_energy_CH2_diss_CH_H_first_image

Act_rev_barrier_CH2_diss_CH_H = Formation_energy_CH2_diss_CH_H_TS_image - Formation_energy_CH2_diss_CH_H_last_image

Rxn_energy_CH2_diss_CH_H =  Formation_energy_CH2_diss_CH_H_last_image - Formation_energy_CH2_diss_CH_H_first_image

Act_fwd_barrier_CH_diss_C_H =  Formation_energy_CH_diss_C_H_TS_image - Formation_energy_CH_diss_C_H_first_image

Act_rev_barrier_CH_diss_C_H =  Formation_energy_CH_diss_C_H_TS_image  - Formation_energy_CH_diss_C_H_last_image

Rxn_energy_CH_diss_C_H =  Formation_energy_CH_diss_C_H_last_image - Formation_energy_CH_diss_C_H_first_image

################################################################################################################################





#####Formation energies =#########################################################################################

CO2_conf2_V8C7_FE = energy_CO2_conf2_V8C7 - energy_V8C7_clean - energy_CO2_gasph

CO_O_FS_FE = energy_CO_O_FS - energy_V8C7_clean - energy_CO2_gasph

C_O_FS_FE = energy_C_O_FS - energy_V8C7_clean - energy_CO2_gasph

CH3OH_IS_conf4_V8C7_FE = energy_CH3OH_IS_conf4_V8C7  - energy_V8C7_clean - energy_CH3OH_gasph 

CH3O_H_FS_final4_V8C7_FE = energy_CH3O_H_FS_final4_V8C7 -  energy_V8C7_clean - energy_CH3OH_gasph 

CH3_O_FS_V8C7_FE = energy_CH3_O_FS_V8C7 - energy_V8C7_clean - energy_CH3OH_gasph 

CH2_H_FS_V8C7_FE = energy_CH2_H_FS_V8C7 - energy_V8C7_clean - energy_CH3OH_gasph 

CH_H_FS_V8C7_FE  =  energy_CH_H_FS_V8C7 - energy_V8C7_clean - energy_CH3OH_gasph 

C_H_FS_V8C7_FE   =  energy_C_H_FS_V8C7 - energy_V8C7_clean - energy_CH3OH_gasph 


########DimerCH3O dissociation activation energy##########
Act_fwd_barrier_CH3O_diss_CH3_O = Formation_energy_CH3O_diss_CH3_O_TS_image - CH3O_H_FS_final4_V8C7_FE

Act_rev_barrier_CH3O_diss_CH3_O = Formation_energy_CH3O_diss_CH3_O_TS_image - CH3_O_FS_V8C7_FE


###########Checking the actual reaction energy and ML-NEB rxn energy##########Start from here#######################################################################################################################

Rxn_energy_CO2_diss =  CO_O_FS_FE - CO2_conf2_V8C7_FE 

diff_NEB_actual_CO2_diss = Rxn_energy_CO2_diss - Rxn_energy_CO2_diss_NEB 

Rxn_energy_CO_diss =  C_O_FS_FE  - CO_O_FS_FE

diff_NEB_actual_CO_diss = Rxn_energy_CO_diss - Rxn_energy_CO_diss_NEB

Rxn_energy_CH3OH_diss_CH3O_H =  CH3O_H_FS_final4_V8C7_FE  - CH3OH_IS_conf4_V8C7_FE

diff_NEB_actual_CH3OH_diss_CH3O_H =  Rxn_energy_CH3OH_diss_CH3O_H  - Rxn_energy_CH3OH_diss_CH3O_H_NEB


array_CH3OH_gasph_FE =  np.repeat(0.00,12)

array_CH3OH_IS_conf4_V8C7_FE =  np.repeat(CH3OH_IS_conf4_V8C7_FE,12)

array_CH3O_H_TS_FE = np.repeat(CH3OH_IS_conf4_V8C7_FE + Act_fwd_barrier_CH3OH_diss_CH3O_H,12)

array_CH3O_H_FS_FE = np.repeat(CH3O_H_FS_final4_V8C7_FE,12)

array_CH3O_diss_CH3_O_TS_FE = np.repeat(CH3O_H_FS_final4_V8C7_FE + Act_fwd_barrier_CH3O_diss_CH3_O,12)

array_CH3_O_FS_V8C7_FE = np.repeat(CH3_O_FS_V8C7_FE,12)

array_CH3_diss_TS_CH2_H_FE = np.repeat(CH3_O_FS_V8C7_FE+Act_fwd_barrier_CH3_diss_CH2_H,12)

array_CH2_H_FS_V8C7_FE = np.repeat(CH2_H_FS_V8C7_FE,12)

array_CH2_diss_TS_CH_H_FE = np.repeat(CH2_H_FS_V8C7_FE + Act_fwd_barrier_CH2_diss_CH_H,12)

array_CH_H_FS_V8C7_FE = np.repeat(CH_H_FS_V8C7_FE,14)

array_CH_diss_TS_C_H_FE = np.repeat(CH_H_FS_V8C7_FE + Act_fwd_barrier_CH_diss_C_H,12)

array_C_H_FS_V8C7_FE  = np.repeat(C_H_FS_V8C7_FE,12)

PES_array_CH3OH_diss = np.concatenate((array_CH3OH_gasph_FE, array_CH3OH_IS_conf4_V8C7_FE, array_CH3O_H_TS_FE, array_CH3O_H_FS_FE, array_CH3O_diss_CH3_O_TS_FE,
                            array_CH3_O_FS_V8C7_FE, array_CH3_diss_TS_CH2_H_FE, array_CH2_H_FS_V8C7_FE, array_CH2_diss_TS_CH_H_FE,
                            array_CH_H_FS_V8C7_FE, array_CH_diss_TS_C_H_FE, array_C_H_FS_V8C7_FE))


x = list(range(0,len(PES_array_CH3OH_diss)))

x_array = np.array(x)


##################Need to include labels#########################################

plt.plot(x, PES_array_CH3OH_diss, color = 'k', linewidth = '2')

plt.xlabel('Reaction coordinate')

plt.ylabel('DFT energy (eV)')

plt.gca().set_xticklabels([])

plt.text(x[16],CH3OH_IS_conf4_V8C7_FE + Act_fwd_barrier_CH3OH_diss_CH3O_H + 0.1, 
         str(round(Act_fwd_barrier_CH3OH_diss_CH3O_H,2)) + " ("+ str(round(Act_rev_barrier_CH3OH_diss_CH3O_H,2)) + ")",
         fontsize=10, color='k')


plt.text(x[38],CH3O_H_FS_final4_V8C7_FE + Act_fwd_barrier_CH3O_diss_CH3_O + 0.1, 
         str(round(Act_fwd_barrier_CH3O_diss_CH3_O,2)) + " ("+ str(round(Act_rev_barrier_CH3O_diss_CH3_O,2)) + ")*",
         fontsize=10, color='k')


plt.text(x[65],CH3_O_FS_V8C7_FE + Act_fwd_barrier_CH3_diss_CH2_H + 0.15, 
         str(round(Act_fwd_barrier_CH3_diss_CH2_H,2)) + " ("+ str(round(Act_rev_barrier_CH3_diss_CH2_H,2)) + ")",
         fontsize=10, color='k')


plt.text(x[85],CH2_H_FS_V8C7_FE + Act_fwd_barrier_CH2_diss_CH_H + 0.1, 
         str(round(Act_fwd_barrier_CH2_diss_CH_H,2)) + " ("+ str(round(Act_rev_barrier_CH2_diss_CH_H,2)) + ")",
         fontsize=10, color='k')


plt.text(x[110],CH_H_FS_V8C7_FE + Act_fwd_barrier_CH_diss_C_H + 0.1, 
         str(round(Act_fwd_barrier_CH_diss_C_H,2)) + " ("+ str(round(Act_rev_barrier_CH_diss_C_H,2)) + ")",
         fontsize=10, color='k')

plt.text(x[0] - 18,0.00 - 0.25, 
         '$CH_3OH (g)$',
         fontsize=10, color='k', rotation = 0)

plt.text(x[0]-4,CH3OH_IS_conf4_V8C7_FE - 0.25, 
         '$CH_3OH*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[22],CH3O_H_FS_final4_V8C7_FE - 0.25, 
         '$CH_3O* + H*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[44],CH3_O_FS_V8C7_FE - 0.25, 
         '$CH_3* + O* + H*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[75],CH2_H_FS_V8C7_FE - 0.35, 
         '$CH_2* + O* + 2H*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[97],CH_H_FS_V8C7_FE - 0.25, 
         '$CH* + OH* + 2H*$',
         fontsize=10, color='k', rotation = 0)

plt.text(x[122],C_H_FS_V8C7_FE - 0.3, 
         '$C* + OH* + 3H*$',
         fontsize=10, color='k', rotation = 0)



plt.ylim([-1.5, 2.1])

plt.xlim([-20, 174])

#plt.figure(figsize=(15, 15))

plt.show()


array_CO2_gasph_FE = np.repeat(0.00,4)

array_CO2_conf2_V8C7_FE = np.repeat(CO2_conf2_V8C7_FE,4)

array_CO2_diss_TS_CO_O_FE = np.repeat(CO2_conf2_V8C7_FE + Act_fwd_barrier_CO2_diss,4)

array_CO_O_FS_FE = np.repeat(CO_O_FS_FE,4)

array_CO_diss_TS_C_O_FE = np.repeat(CO_O_FS_FE + Act_fwd_barrier_CO_diss,4)

array_C_O_FS_FE = np.repeat(C_O_FS_FE,4)

PES_array_CO2_diss =np.concatenate((array_CO2_gasph_FE, array_CO2_conf2_V8C7_FE, array_CO2_diss_TS_CO_O_FE, array_CO_O_FS_FE,
                                  array_CO_diss_TS_C_O_FE, array_C_O_FS_FE))

x_CO2_diss = list(range(0,len(PES_array_CO2_diss)))

x_CO2_diss = np.array(x_CO2_diss)

#####################################################################################################

plt.plot(x_CO2_diss, PES_array_CO2_diss, color = 'k', linewidth = '2')

plt.text(x[7]+0.5,CO2_conf2_V8C7_FE + Act_fwd_barrier_CO2_diss + 0.1, 
         str(round(Act_fwd_barrier_CO2_diss,2)) + " ("+ str(round(Act_rev_barrier_CO2_diss,2)) + ")",
         fontsize=10, color='k')

plt.text(x[15]+0.5,CO_O_FS_FE + Act_fwd_barrier_CO_diss + 0.1, 
         str(round(Act_fwd_barrier_CO_diss,2)) + " ("+ str(round(Act_rev_barrier_CO_diss,2)) + ")",
         fontsize=10, color='k')


plt.text(x[0]-0.5,0.00- 0.2, 
         '$CO_2 (g)$',
         fontsize=10, color='k', rotation = 0)

plt.text(x[4]+0.5,CO2_conf2_V8C7_FE - 0.2, 
         '$CO_2*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[12],CO_O_FS_FE - 0.2, 
         '$CO* + O*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[20],C_O_FS_FE - 0.2, 
         '$C* + 2O*$',
         fontsize=10, color='k', rotation = 0)


plt.xlabel('Reaction coordinate')

plt.ylabel('DFT energy (eV)')

plt.ylim([-1.5, 2.1])

plt.gca().set_xticklabels([])

#plt.figure(figsize=(15, 15))

plt.show()

#####################12 modes########################################

script_dir = os.curdir

##############G#####################from ase.vibrations import Vibrations###Done#############################################

os.chdir("C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/gas_phase_calc/CH3OH_gasph")

atoms_CH3OH_gasph = read('CONTCAR')   # gas phase####

os.chdir(script_dir)

thermo = IdealGasThermo(
    vib_energies=[0.465719774, 0.379606365, 0.369691816, 0.363449683, 0.181142949,  0.179721265,
                  0.177208285, 0.164847256, 0.140620402, 0.130901505, 0.125078860,  0.037400731],
    atoms=atoms_CH3OH_gasph,
    geometry='nonlinear',
    symmetrynumber=12, spin=0) ####need to verify the symmetry number################


G_CH3OH_gasph = energy_CH3OH_gasph + thermo.get_gibbs_energy(temperature=Temp, pressure= Pressure)

#########################################################################################################################################


os.chdir("C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/gas_phase_calc/CO2_gasph")

atoms_CO2_gasph = read('CONTCAR')   # gas phase


thermo = IdealGasThermo(
    vib_energies=[0.293503698, 0.163545878, 0.078241577, 0.078010997],
    atoms=atoms_CO2_gasph,
    geometry='linear',
    symmetrynumber=2, spin=0)


G_CO2_gasph = energy_CO2_gasph + thermo.get_gibbs_energy(temperature=Temp, pressure= Pressure)

#########################################################################################################################################




##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.161476430, 0.122429461, 0.089719530, 0.061322775, 0.041189452,
                                      0.038649099, 0.035255219, 0.029477841, 0.024043714]) ######9 modes#############

G_CO2_conf2_V8C7 = energy_CO2_conf2_V8C7 + thermo.get_helmholtz_energy(temperature=Temp)

G_CO2_conf2_V8C7_FE = G_CO2_conf2_V8C7 - energy_V8C7_clean - G_CO2_gasph


##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.248745874, 0.050799019, 0.049535983, 0.043815559, 0.040281758,
                                      0.037441991, 0.027757132, 0.005634888, 0.004438030]) #####9 ,odes############

G_CO_O_FS = energy_CO_O_FS + thermo.get_helmholtz_energy(temperature=Temp)


G_CO_O_FS_FE = G_CO_O_FS - energy_V8C7_clean - G_CO2_gasph


##################vibration energies (in eV) ################This is not available##########################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.124850882, 0.092544842, 0.055297147, 0.045302990, 0.044721657, 
                                      0.041735075, 0.038994024, 0.029312235, 0.019513620]) #####9 modes############

G_C_O_FS = energy_C_O_FS + thermo.get_helmholtz_energy(temperature=Temp)


G_C_O_FS_FE = G_C_O_FS - energy_V8C7_clean - G_CO2_gasph



##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.440538029, 0.380624575, 0.373695054, 0.362238446, 0.180112515, 0.177852571,
                                      0.174584719, 0.160996790, 0.140148975, 0.129817688, 0.123697056, 0.062988682, 
                                      0.031690960, 0.024803797, 0.021109153, 0.016683236, 0.011115892, 0.008055691]) ######12 modes#############

G_CH3OH_IS_conf4_V8C7 = energy_CH3OH_IS_conf4_V8C7 + thermo.get_helmholtz_energy(temperature=Temp)

G_CH3OH_IS_conf4_V8C7_FE = G_CH3OH_IS_conf4_V8C7 - energy_V8C7_clean - G_CH3OH_gasph


##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.371343503, 0.369769012, 0.360582787, 0.326182648, 0.179422453, 0.177744760,
                                      0.174346711, 0.140342281, 0.139540923, 0.122503212, 0.054326523, 0.043576772, 
                                      0.034452755, 0.031265114, 0.024599927, 0.020344809, 0.015064485, 0.013022327]) ######18 modes#############

G_CH3O_H_FS_final4_V8C7 = energy_CH3O_H_FS_final4_V8C7 + thermo.get_helmholtz_energy(temperature=Temp)

G_CH3O_H_FS_final4_V8C7_FE = G_CH3O_H_FS_final4_V8C7 - energy_V8C7_clean - G_CH3OH_gasph

##################vibration energies (in eV) ######These are wrong values####################################################################################################################################


thermo = HarmonicThermo(vib_energies=[0.366423495, 0.360517829, 0.325999341, 0.321193908, 0.181525740, 0.172056503,
                                      0.164901813, 0.118066646, 0.113657339, 0.074742955, 0.056794950, 0.048459980, 
                                      0.040543507, 0.038546282, 0.034941786, 0.028050839, 0.025324198, 0.012687979]) #######18 modes#############

G_CH3_O_FS_V8C7 = energy_CH3_O_FS_V8C7 + thermo.get_helmholtz_energy(temperature=Temp)

G_CH3_O_FS_V8C7_FE = G_CH3_O_FS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph

##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.376552278, 0.345653105, 0.325932850, 0.287425994, 0.176369860, 0.117214718,
                                      0.107372461, 0.097894426, 0.092443018, 0.069886281, 0.066156276, 0.065058589,
                                      0.063348022, 0.055493075, 0.044498107, 0.041159027, 0.035471867, 0.029365443]) #######18 modes###########

G_CH2_H_FS_V8C7 = energy_CH2_H_FS_V8C7 + thermo.get_helmholtz_energy(temperature=Temp)

G_CH2_H_FS_V8C7_FE = G_CH2_H_FS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph

##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.384325670, 0.375041609, 0.311329166, 0.292057035, 0.118671423, 0.115010286, 
                                      0.107513393, 0.103497577, 0.097701795, 0.087468823, 0.059512182, 0.057401242, 
                                      0.056326935, 0.053808879, 0.051683639, 0.044519844, 0.039614005, 0.029849674]) #######18 modes######

G_CH_H_FS_V8C7 = energy_CH_H_FS_V8C7 + thermo.get_helmholtz_energy(temperature=Temp)

G_CH_H_FS_V8C7_FE = G_CH_H_FS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph


##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.368979853, 0.327041854, 0.323683464, 0.309634575, 0.125690992, 0.108894671,
                                      0.103300486, 0.085631462, 0.070387965, 0.068513317, 0.064583964, 0.062352094,
                                      0.060619863, 0.056050257, 0.049820884, 0.048204247, 0.038984402, 0.031550886]) ######18 modes#############

G_C_H_FS_V8C7 = energy_C_H_FS_V8C7  + thermo.get_helmholtz_energy(temperature=Temp)

G_C_H_FS_V8C7_FE = G_C_H_FS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph


##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.233647411, 0.069183356, 0.057007198, 0.039356843, 0.031799335, 0.022892114,
                                      0.019481242, 0.008198865]) ###############

G_CO2_diss_TS_V8C7 =  energy_CO2_conf2_V8C7 + Act_fwd_barrier_CO2_diss + thermo.get_helmholtz_energy(temperature=Temp)

G_CO2_diss_TS_V8C7_FE = G_CO2_diss_TS_V8C7 - energy_V8C7_clean - G_CO2_gasph

##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.112414017, 0.077309491, 0.068576926, 0.049848256, 0.046086599, 0.041757769,
                                      0.036592810, 0.028455307]) #############

G_CO_diss_TS_V8C7 =  energy_CO_O_FS + Act_fwd_barrier_CO_diss + thermo.get_helmholtz_energy(temperature=Temp)


G_CO_diss_TS_V8C7_FE = G_CO_diss_TS_V8C7 - energy_V8C7_clean - G_CO2_gasph


##################vibration energies (in eV) ##########################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.369544590, 0.359261051, 0.349470241, 0.177863497, 0.175041399, 0.173809002, 
                                      0.163953902, 0.140043014, 0.138987189, 0.131258729, 0.105563499, 0.045119682, 
                                      0.038443783, 0.025316939, 0.021803059, 0.016192980, 0.014187670]) ######17 modes#############

Genergy_CH3OH_diss_CH3O_H_TS_V8C7 = energy_CH3OH_IS_conf4_V8C7 + Act_fwd_barrier_CH3OH_diss_CH3O_H  + thermo.get_helmholtz_energy(temperature=Temp)

G_CH3OH_diss_CH3O_H_TS_V8C7_FE = Genergy_CH3OH_diss_CH3O_H_TS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph

##################vibration energies (in eV) ###############CH3O dissociation to CH3 + O###########################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.364148701, 0.347786170, 0.307836460, 0.296350266, 0.176170250, 0.172753496,
                                      0.151467815, 0.118097153, 0.100523404, 0.073186645, 0.067031475, 0.057269518, 
                                      0.055942380, 0.038681477, 0.035503702, 0.021242159, 0.015542380]) ######17 modes#############

Genergy_CH3O_diss_CH3_O_TS_V8C7 =  energy_CH3O_H_FS_final4_V8C7 + Act_fwd_barrier_CH3O_diss_CH3_O + thermo.get_helmholtz_energy(temperature=Temp)

G_CH3O_diss_CH3_O_TS_V8C7_FE = Genergy_CH3O_diss_CH3_O_TS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph

##################vibration energies (in eV) #########CH3 dissociation to CH2#################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.367887819, 0.361307815, 0.319359323, 0.205015973, 0.173770546, 0.122959206,
                                      0.116643563, 0.108113499, 0.089759194, 0.075032909, 0.054240773, 0.046938928, 
                                      0.045923567, 0.042814278, 0.039662492, 0.030050420, 0.021543262]) ######17 modes#############

Genergy_CH3_CH2_H_TS_V8C7 =  energy_CH3_O_FS_V8C7  + Act_fwd_barrier_CH3_diss_CH2_H + thermo.get_helmholtz_energy(temperature=Temp)

G_CH3_CH2_H_TS_V8C7_FE = Genergy_CH3_CH2_H_TS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph

##################vibration energies (in eV) ########CH2 dissociation to CH#################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.376609894, 0.312154095, 0.301812869, 0.167667200, 0.124975652, 0.117470187,
                                      0.102814907, 0.097120162, 0.093717100, 0.083009875, 0.061472016, 0.057318783, 
                                      0.054561086, 0.053617638, 0.050875238, 0.041690986, 0.032910113]) ######17 modes#############

Genergy_CH2_CH_H_TS_V8C7 = energy_CH2_H_FS_V8C7  + Act_fwd_barrier_CH2_diss_CH_H + thermo.get_helmholtz_energy(temperature=Temp)

G_CH2_CH_H_TS_V8C7_FE = Genergy_CH2_CH_H_TS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph


##################vibration energies (in eV) ########CH dissociation to C#################################################################################################################################

thermo = HarmonicThermo(vib_energies=[0.392450043, 0.325507041, 0.249429656, 0.196148976, 0.124063819, 0.121781907, 
                                      0.104504358, 0.102588105, 0.073076171, 0.059252679, 0.057668316, 0.056640258,
                                      0.047617945, 0.045976005, 0.040727999, 0.037262760, 0.030139516 ]) ######17 modes#############

Genergy_CH_C_H_TS_V8C7 = energy_CH_H_FS_V8C7 +   Act_fwd_barrier_CH_diss_C_H  + thermo.get_helmholtz_energy(temperature=Temp)

G_CH_C_H_TS_V8C7_FE = Genergy_CH_C_H_TS_V8C7 - energy_V8C7_clean - G_CH3OH_gasph






#####################################################################################################

array_CO2_gasph_FE = np.repeat(0.00,4)

array_CO2_conf2_V8C7_FE = np.repeat(G_CO2_conf2_V8C7_FE,4)

array_CO2_diss_TS_CO_O_FE = np.repeat(G_CO2_diss_TS_V8C7_FE,4)

array_CO_O_FS_FE = np.repeat(G_CO_O_FS_FE,4)

array_CO_diss_TS_C_O_FE = np.repeat(G_CO_diss_TS_V8C7_FE,4)

array_C_O_FS_FE = np.repeat(G_C_O_FS_FE,4)

FES_array_CO2_diss =np.concatenate((array_CO2_gasph_FE, array_CO2_conf2_V8C7_FE, array_CO2_diss_TS_CO_O_FE, array_CO_O_FS_FE,
                                  array_CO_diss_TS_C_O_FE, array_C_O_FS_FE))


x_CO2_diss = list(range(0,len(FES_array_CO2_diss)))

x_CO2_diss = np.array(x_CO2_diss)

plt.plot(x_CO2_diss, FES_array_CO2_diss, color = 'r', linewidth = '2')

plt.xlabel('Reaction coordinate')

plt.ylabel('Free energy (eV)')

#plt.ylim([-1.5, 2.1])

F_act_fwd_barrier_CO2_diss = G_CO2_diss_TS_V8C7_FE - G_CO2_conf2_V8C7_FE

F_act_rev_barrier_CO2_diss = G_CO2_diss_TS_V8C7_FE - G_CO_O_FS_FE

F_act_fwd_barrier_CO_diss = G_CO_diss_TS_V8C7_FE - G_CO_O_FS_FE

F_act_rev_barrier_CO_diss = G_CO_diss_TS_V8C7_FE - G_C_O_FS_FE


plt.text(x[7]+0.55,G_CO2_diss_TS_V8C7_FE+ 0.15, 
     str(round(F_act_fwd_barrier_CO2_diss,2)) + " ("+ str(round(F_act_rev_barrier_CO2_diss,2)) + ")",
     fontsize=10, color='k')
#
plt.text(x[15]+0.55,G_CO_diss_TS_V8C7_FE + 0.15, 
         str(round(F_act_fwd_barrier_CO_diss,2)) + " ("+ str(round(F_act_rev_barrier_CO_diss,2)) + ")",
         fontsize=10, color='k')


plt.text(x[0],0.00- 0.25, 
         '$CO_2 (g)$',
          fontsize=10, color='k', rotation = 0)

plt.text(x[4]+0.5,G_CO2_conf2_V8C7_FE - 0.25, 
         '$CO_2*$',
         fontsize=10, color='k', rotation = 0)

plt.text(x[12],G_CO_O_FS_FE - 0.25, 
         '$CO* + O*$',
          fontsize=10, color='k', rotation = 0)

plt.text(x[20],G_C_O_FS_FE - 0.25, 
         '$C* + 2O*$',
         fontsize=10, color='k', rotation = 0)


#plt.figure(figsize=(15, 15))

plt.ylim([-0.5, 3.9])

plt.gca().set_xticklabels([])

plt.figure(figsize=(10, 15))

plt.show()



#####################################################################################################




##########Free energy profiles ###########################################################################################

array_CH3OH_gasph_FE =  np.repeat(0.00,12)

array_CH3OH_IS_conf4_V8C7_FE =  np.repeat(G_CH3OH_IS_conf4_V8C7_FE,12)

array_CH3O_H_TS_FE = np.repeat(G_CH3OH_diss_CH3O_H_TS_V8C7_FE,12)

array_CH3O_H_FS_FE = np.repeat(G_CH3O_H_FS_final4_V8C7_FE,12)

array_CH3O_diss_CH3_O_TS_FE = np.repeat(G_CH3O_diss_CH3_O_TS_V8C7_FE,12)

array_CH3_O_FS_V8C7_FE = np.repeat(G_CH3_O_FS_V8C7_FE,12)

array_CH3_diss_TS_CH2_H_FE = np.repeat(G_CH3_CH2_H_TS_V8C7_FE,12)

array_CH2_H_FS_V8C7_FE = np.repeat(G_CH2_H_FS_V8C7_FE,12)

array_CH2_diss_TS_CH_H_FE = np.repeat(G_CH2_CH_H_TS_V8C7_FE,12)

array_CH_H_FS_V8C7_FE = np.repeat(G_CH_H_FS_V8C7_FE,12)

array_CH_diss_TS_C_H_FE = np.repeat(G_CH_C_H_TS_V8C7_FE,12)

array_C_H_FS_V8C7_FE  = np.repeat(G_C_H_FS_V8C7_FE,12)

FES_array_CH3OH_diss = np.concatenate((array_CH3OH_gasph_FE, array_CH3OH_IS_conf4_V8C7_FE, array_CH3O_H_TS_FE, array_CH3O_H_FS_FE, array_CH3O_diss_CH3_O_TS_FE,
                            array_CH3_O_FS_V8C7_FE, array_CH3_diss_TS_CH2_H_FE, array_CH2_H_FS_V8C7_FE, array_CH2_diss_TS_CH_H_FE,
                            array_CH_H_FS_V8C7_FE, array_CH_diss_TS_C_H_FE, array_C_H_FS_V8C7_FE))

x1 = list(range(0,len(FES_array_CH3OH_diss)))

x_array1 = np.array(x1)



##################Need to include labels#########################################


Free_energy_Act_fwd_barrier_CH3OH_diss_CH3O_H = G_CH3OH_diss_CH3O_H_TS_V8C7_FE  - G_CH3OH_IS_conf4_V8C7_FE
 
Free_energy_Act_rev_barrier_CH3OH_diss_CH3O_H = G_CH3OH_diss_CH3O_H_TS_V8C7_FE  - G_CH3O_H_FS_final4_V8C7_FE 

Free_energy_Act_fwd_barrier_CH3O_diss_CH3_O = G_CH3O_diss_CH3_O_TS_V8C7_FE - G_CH3O_H_FS_final4_V8C7_FE

Free_energy_Act_rev_barrier_CH3O_diss_CH3_O = G_CH3O_diss_CH3_O_TS_V8C7_FE -  G_CH3_O_FS_V8C7_FE

Free_energy_Act_fwd_barrier_CH3_diss_CH2_H  = G_CH3_CH2_H_TS_V8C7_FE - G_CH3_O_FS_V8C7_FE

Free_energy_Act_rev_barrier_CH3_diss_CH2_H  = G_CH3_CH2_H_TS_V8C7_FE - G_CH2_H_FS_V8C7_FE

Free_energy_Act_fwd_barrier_CH2_diss_CH_H = G_CH2_CH_H_TS_V8C7_FE - G_CH2_H_FS_V8C7_FE

Free_energy_Act_rev_barrier_CH2_diss_CH_H = G_CH2_CH_H_TS_V8C7_FE - G_CH_H_FS_V8C7_FE

Free_energy_Act_fwd_barrier_CH_diss_C_H = G_CH_C_H_TS_V8C7_FE - G_CH_H_FS_V8C7_FE

Free_energy_Act_rev_barrier_CH_diss_C_H = G_CH_C_H_TS_V8C7_FE - G_C_H_FS_V8C7_FE 


plt.text(x[16],G_CH3OH_diss_CH3O_H_TS_V8C7_FE + 0.1, 
       str(round(Free_energy_Act_fwd_barrier_CH3OH_diss_CH3O_H,2)) + " ("+ str(round(Free_energy_Act_rev_barrier_CH3OH_diss_CH3O_H,2)) + ")",
       fontsize=10, color='k')


plt.text(x[38],G_CH3O_diss_CH3_O_TS_V8C7_FE + 0.1, 
     str(round(Free_energy_Act_fwd_barrier_CH3O_diss_CH3_O,2)) + " ("+ str(round(Free_energy_Act_rev_barrier_CH3O_diss_CH3_O,2)) + ")*",
     fontsize=10, color='k')


plt.text(x[65],G_CH3_CH2_H_TS_V8C7_FE + 0.20, 
       str(round(Free_energy_Act_fwd_barrier_CH3_diss_CH2_H ,2)) + " ("+ str(round(Free_energy_Act_rev_barrier_CH3_diss_CH2_H,2)) + ")",
       fontsize=10, color='k')


plt.text(x[85],G_CH2_CH_H_TS_V8C7_FE + 0.1, 
      str(round(Free_energy_Act_fwd_barrier_CH2_diss_CH_H,2)) + " ("+ str(round(Free_energy_Act_rev_barrier_CH2_diss_CH_H,2)) + ")",
      fontsize=10, color='k')


plt.text(x[110],G_CH_C_H_TS_V8C7_FE + 0.1, 
     str(round(Act_fwd_barrier_CH_diss_C_H,2)) + " ("+ str(round(Act_rev_barrier_CH_diss_C_H,2)) + ")",
     fontsize=10, color='k')

plt.text(x[0],0.00 - 0.25, 
      '$CH_3OH (g)$',
      fontsize=10, color='k', rotation = 0)

plt.text(x[13],G_CH3OH_IS_conf4_V8C7_FE - 0.25, 
         '$CH_3OH*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[27],G_CH3O_H_FS_final4_V8C7_FE - 0.4, 
         '$CH_3O* + H*$',
          fontsize=10, color='k', rotation = 0)


plt.text(x[44],G_CH3_O_FS_V8C7_FE - 0.35, 
         '$CH_3* + O* + H*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[75],G_CH2_CH_H_TS_V8C7_FE  - 0.75, 
         '$CH_2* + O* + 2H*$',
         fontsize=10, color='k', rotation = 0)


plt.text(x[97],G_CH_H_FS_V8C7_FE - 0.25, 
        '$CH* + OH* + 2H*$',
         fontsize=10, color='k', rotation = 0)

plt.text(x[121],G_C_H_FS_V8C7_FE - 0.3, 
        '$C* + OH* + 3H*$',
         fontsize=10, color='k', rotation = 0)

plt.plot(x_array1, FES_array_CH3OH_diss, color = 'r', linewidth = '2')

plt.xlabel('Reaction coordinate')

plt.ylabel('Free energy (eV)')

plt.gca().set_xticklabels([])

plt.ylim([-0.5,3.9])

plt.xlim([-1, 164])

plt.show()

#plt.figure(figsize=(15, 15))


######################, figsize=(15, 15)######Figure###################################################################################################

fig1, axs = plt.subplots(1,figsize=(4, 5))

axs.plot(x_CO2_diss, PES_array_CO2_diss, color = 'k', linewidth = '2')

axs.plot(x_CO2_diss, FES_array_CO2_diss, color = 'r', linewidth = '2')




axs.text(x[8]+0.25,CO2_conf2_V8C7_FE + Act_fwd_barrier_CO2_diss + 0.45, 
         str(round(Act_fwd_barrier_CO2_diss,2)),
         fontsize=10, color='k')

axs.text(x[8]+0.05,CO2_conf2_V8C7_FE + Act_fwd_barrier_CO2_diss + 0.15, 
         "("+ str(round(Act_rev_barrier_CO2_diss,2)) + ")",
         fontsize=10, color='k')

axs.text(x[16]+0.2,CO_O_FS_FE + Act_fwd_barrier_CO_diss + 0.45, 
         str(round(Act_fwd_barrier_CO_diss,2)),
         fontsize=10, color='k')

axs.text(x[16],CO_O_FS_FE + Act_fwd_barrier_CO_diss + 0.15, 
         "("+ str(round(Act_rev_barrier_CO_diss,2)) + ")",
         fontsize=10, color='k')

axs.text(x[8]+0.25,G_CO2_diss_TS_V8C7_FE+ 0.45, 
     str(round(F_act_fwd_barrier_CO2_diss,2)),
     fontsize=10, color='k')

axs.text(x[8]+0.05,G_CO2_diss_TS_V8C7_FE+ 0.15, 
     "("+ str(round(F_act_rev_barrier_CO2_diss,2)) + ")",
     fontsize=10, color='k')
#
axs.text(x[16]+0.2,G_CO_diss_TS_V8C7_FE + 0.45, 
         str(round(F_act_fwd_barrier_CO_diss,2)),
         fontsize=10, color='k')

axs.text(x[16],G_CO_diss_TS_V8C7_FE + 0.15, 
         "("+ str(round(F_act_rev_barrier_CO_diss,2)) + ")",
         fontsize=10, color='k')

#axs.set(fontsize=12)
axs.tick_params(axis='both', which='major', labelsize=12)
axs.tick_params(axis='both', which='minor', labelsize=10)

axs.set_ylabel('Energy (eV)', fontsize=12)

axs.set_ylim([-1.6,4.3])

xmean_value = [1.5, 5.5, 13.5, 21.0]

#axs.set_yticks(fontsize=12)

xlabels =["$CO_2$",'$CO_2*$','$CO* + O*$','$C* + 2O*$']

axs.set_xticks(ticks=xmean_value, labels=xlabels, rotation=-60, fontsize=12)

axs.legend(["Potential Energy", "Free energy"],loc="upper left")

#plt.figure(figsize=(10, 15))

plt.tight_layout()

plt.show()


###########################################################################################################################

fig2, axs1 = plt.subplots(1,figsize=(7,5))

axs1.plot(x, PES_array_CH3OH_diss, color = 'k', linewidth = '2')

axs1.plot(x_array1, FES_array_CH3OH_diss, color = 'r', linewidth = '2')


axs1.text(x[27],G_CH3OH_diss_CH3O_H_TS_V8C7_FE + 0.45, 
       str(round(Free_energy_Act_fwd_barrier_CH3OH_diss_CH3O_H,2)),
       fontsize=10, color='k')

axs1.text(x[24],G_CH3OH_diss_CH3O_H_TS_V8C7_FE + 0.15, 
       "("+ str(round(Free_energy_Act_rev_barrier_CH3OH_diss_CH3O_H,2)) + ")",
       fontsize=10, color='k')

axs1.text(x[50],G_CH3O_diss_CH3_O_TS_V8C7_FE + 0.45, 
     str(round(Free_energy_Act_fwd_barrier_CH3O_diss_CH3_O,2)),
     fontsize=10, color='k')

axs1.text(x[49],G_CH3O_diss_CH3_O_TS_V8C7_FE + 0.15, 
     "("+ str(round(Free_energy_Act_rev_barrier_CH3O_diss_CH3_O,2)) + ")",
     fontsize=10, color='k')

axs1.text(x[74],G_CH3_CH2_H_TS_V8C7_FE + 0.45, 
       str(round(Free_energy_Act_fwd_barrier_CH3_diss_CH2_H ,2)),
       fontsize=10, color='k')

axs1.text(x[73],G_CH3_CH2_H_TS_V8C7_FE + 0.15, 
    "("+ str(round(Free_energy_Act_rev_barrier_CH3_diss_CH2_H,2)) + ")",
       fontsize=10, color='k')


axs1.text(x[97],G_CH2_CH_H_TS_V8C7_FE + 0.45, 
      str(round(Free_energy_Act_fwd_barrier_CH2_diss_CH_H,2)),
      fontsize=10, color='k')


axs1.text(x[96],G_CH2_CH_H_TS_V8C7_FE + 0.15, 
      "("+ str(round(Free_energy_Act_rev_barrier_CH2_diss_CH_H,2)) + ")",
      fontsize=10, color='k')


axs1.text(x[122],G_CH_C_H_TS_V8C7_FE + 0.45, 
     str(round(Act_fwd_barrier_CH_diss_C_H,2)),
     fontsize=10, color='k')


axs1.text(x[121],G_CH_C_H_TS_V8C7_FE + 0.15, 
     "("+ str(round(Act_rev_barrier_CH_diss_C_H,2)) + ")",
     fontsize=10, color='k')


axs1.text(x[27],CH3OH_IS_conf4_V8C7_FE + Act_fwd_barrier_CH3OH_diss_CH3O_H + 0.45, 
         str(round(Act_fwd_barrier_CH3OH_diss_CH3O_H,2)),
         fontsize=10, color='k')

axs1.text(x[25],CH3OH_IS_conf4_V8C7_FE + Act_fwd_barrier_CH3OH_diss_CH3O_H + 0.15, 
          "("+ str(round(Act_rev_barrier_CH3OH_diss_CH3O_H,2)) + ")",
         fontsize=10, color='k')

axs1.text(x[50],CH3O_H_FS_final4_V8C7_FE + Act_fwd_barrier_CH3O_diss_CH3_O + 0.45, 
         str(round(Act_fwd_barrier_CH3O_diss_CH3_O,2)),
         fontsize=10, color='k')

axs1.text(x[48]-0.2,CH3O_H_FS_final4_V8C7_FE + Act_fwd_barrier_CH3O_diss_CH3_O + 0.15, 
         "("+ str(round(Act_rev_barrier_CH3O_diss_CH3_O,2)) + ")",
         fontsize=10, color='k')

axs1.text(x[74],CH3_O_FS_V8C7_FE + Act_fwd_barrier_CH3_diss_CH2_H + 0.45, 
         str(round(Act_fwd_barrier_CH3_diss_CH2_H,2)),
         fontsize=10, color='k')


axs1.text(x[73],CH3_O_FS_V8C7_FE + Act_fwd_barrier_CH3_diss_CH2_H + 0.15, 
         "("+ str(round(Act_rev_barrier_CH3_diss_CH2_H,2)) + ")",
         fontsize=10, color='k')


axs1.text(x[97],CH2_H_FS_V8C7_FE + Act_fwd_barrier_CH2_diss_CH_H + 0.45, 
         str(round(Act_fwd_barrier_CH2_diss_CH_H,2)),
         fontsize=10, color='k')


axs1.text(x[96],CH2_H_FS_V8C7_FE + Act_fwd_barrier_CH2_diss_CH_H + 0.15, 
         "("+ str(round(Act_rev_barrier_CH2_diss_CH_H,2)) + ")",
         fontsize=10, color='k')


axs1.text(x[123],CH_H_FS_V8C7_FE + Act_fwd_barrier_CH_diss_C_H + 0.45, 
         str(round(Act_fwd_barrier_CH_diss_C_H,2)),
         fontsize=10, color='k')


axs1.text(x[122],CH_H_FS_V8C7_FE + Act_fwd_barrier_CH_diss_C_H + 0.15, 
         "("+ str(round(Act_rev_barrier_CH_diss_C_H,2)) + ")",
         fontsize=10, color='k')

axs1.tick_params(axis='both', which='major', labelsize=12)
axs1.tick_params(axis='both', which='minor', labelsize=10)

#plt.xlabel('Reaction coordinate')

axs1.set_ylabel('Energy (eV)', fontsize=12)

axs1.set_ylim([-1.6,4.3])

xmean_value = [6.5, 17, 41.5, 65.5, 89.5, 113.5, 137.5]

#xmean_value = [6.5-4, 17-4, 41.5-4, 65.5-4, 89.5-4, 113.5-4, 137.5-4]

#plt.xticks(xmean_value)

#plt.yticks(fontsize=12)

#xlabels =["$CH_3OH$",'$CH_3OH*$','$CH_3O* + H*$','$CH_3* + O* + H*$','$CH_2* + O* + 2H*$',
 #         "$CH* + OH* + 2H*$","$C* + OH* + 3H*$"]

xlabels =["$CH_3OH$",'$CH_3OH*$','$CH_3O* + H*$','$CH_3* + O* + H*$','$CH_2* + O* + 2H*$',
          "$CH* + OH* + 2H*$","$C* + OH* + 3H*$"]

axs1.set_xticks(ticks=xmean_value, labels=xlabels, rotation=-60, fontsize=12)

#plt.gca().set_xticklabels(xlabels,rotation=-45)

axs1.legend(["Potential Energy", "Free energy"],loc="upper left")

plt.tight_layout()

plt.show()





#

#FES_array_CH3OH_diss = np.concatenate((array_CH3OH_gasph_FE, array_CH3OH_IS_conf4_V8C7_FE, array_CH3O_H_TS_FE, array_CH3O_H_FS_FE, array_CH3O_diss_CH3_O_TS_FE,
          #                  array_CH3_O_FS_V8C7_FE, array_CH3_diss_TS_CH2_H_FE, array_CH2_H_FS_V8C7_FE, array_CH2_diss_TS_CH_H_FE,
           #                 array_CH_H_FS_V8C7_FE, array_CH_diss_TS_C_H_FE, array_C_H_FS_V8C7_FE))

#plt.xlim([-20, 174])

#plt.xticks([x[0] - 18, x[0]-4,
    #        FES_array_CH3OH_diss[60], FES_array_CH3OH_diss[84], 
     #       FES_array_CH3OH_diss[97], FES_array_CH3OH_diss[109],FES_array_CH3OH_diss[132]])

