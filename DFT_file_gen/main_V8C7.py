

#####important Note include the job name in your submission script for subsequent runs###########



####This is a script to generate the VASP input files for any system##############

VASPfiles_Dir = 'C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/V8C8_calc/files_CO2dis_VC/files_CO2dis_VC/Output_files' 

POSCAR_loc_dir = 'C:/Project3_project4/Postdoc_Projects/Project1_V_C/DFT_calc/V8C8_calc/files_CO2dis_VC/files_CO2dis_VC/POSCARS'  

Pseudopptential_dir = 'C:/Project3_project4/Postdoc_Projects/Project1_V_C/Pseudopotential_files/Recomm_potpaw_PBE_new'

###############Importing the required modules#########################

import os 
from Generate_POSCAR import vasp_POSCAR  ###D123#4#####       
from Generate_POTCAR import vasp_POTCAR  ######D##1#234####
from Generate_INCAR import vasp_INCAR    ####D#####
#from Generate_INCAR_DIMER import vasp_INCAR_DIMER    ####D#####
#from Generate_INCAR_Newton import vasp_INCAR_Newton    ####D#####
#from Generate_vib_INCAR import vasp_vib_INCAR    ###D##1#4##
from Generate_KPOINTS import vasp_KPOINTS  ###D##12##34
from Generate_MCC_sub import vasp_MCC_sub_script  #D#12#4#


###################Calling the required functions to create the submission script############
currentdir = os.getcwd()
vasp_POSCAR(VASPfiles_Dir,POSCAR_loc_dir)   ###D#####
vasp_POTCAR(VASPfiles_Dir,Pseudopptential_dir)   ###D#####
vasp_INCAR(VASPfiles_Dir) ##D##
#vasp_INCAR_DIMER(VASPfiles_Dir) 
#vasp_INCAR_Newton(VASPfiles_Dir) ##D##
#vasp_vib_INCAR(VASPfiles_Dir) ######D#####
vasp_KPOINTS(VASPfiles_Dir)  ####D#####
vasp_MCC_sub_script(VASPfiles_Dir)  ####D#####
os.chdir(currentdir)
#############################################################################################

