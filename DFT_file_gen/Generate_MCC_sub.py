
def vasp_MCC_sub_script(VASPfiles_Dir):
    import os
    vasp_fldrs = os.listdir(VASPfiles_Dir)
    for i in range(len(vasp_fldrs)):
        vasp_sub_file = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'vasp_sub')
        f = open(vasp_sub_file,"w")
        f.write("#!/bin/bash -l \n")
        f.write("#$ -S /bin/bash \n")
        f.write("#$ -P Free \n")
        #f.write("#$ -A UCL_chemE_Stamatakis \n")
        f.write("#$ -A MCC_react_sta \n")
        f.write("#$ -l h_rt=24:00:00 \n")
        f.write("#$ -l mem=2G \n")
        f.write("#$ -pe mpi 80 \n")
        f.write("#$ -N DFT_calc \n \n"); 
        f.write("#$ -cwd \n")
        f.write("module unload -f compilers mpi \n")
        f.write("module load compilers/intel/2019/update5 \n")
        f.write("module load mpi/intel/2019/update5/intel \n")
        f.write("module load vasp/5.4.4-18apr2017/intel-2019 \n")
        f.write("gerun vasp_std > vasp.out \n")
        f.close()
        