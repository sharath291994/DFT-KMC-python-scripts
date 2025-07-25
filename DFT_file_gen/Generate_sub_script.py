
def vasp_sub_script(VASPfiles_Dir):
    import os
    vasp_fldrs = os.listdir(VASPfiles_Dir)
    for i in range(len(vasp_fldrs)):
        vasp_sub_file = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'vasp_sub')
        f = open(vasp_sub_file,"w")
        f.write("#!/bin/bash -l \n")
        f.write("#Batch script to run an MPI parallel job on Legion with the upgraded software \n")
        f.write("#stack under SGE with Intel MPI \n")
        f.write("#Budgeting \n \n")
        f.write("#$ -P Gold \n \n")
        f.write("#$ -A UCL_chemE_Stamatakis \n \n")
        f.write("# 1. Force bash as the executing shell. \n")
        f.write("#$ -S /bin/bash \n \n")
        f.write("# 2. Request wallclock time (format hours:minutes:seconds). \n")
        f.write("#$ -l h_rt=24:00:00 \n \n")
        f.write("# 5. Set the name of the job.  \n"); 
        f.write("#$ -N CO2_calc \n \n"); 
        f.write("# Email Notification  \n"); 
        f.write("#$ -M sai.yadavalli.18@ucl.ac.uk \n \n"); 
        f.write("# 6. Select the MPI parallel environment and number of processes. \n"); 
        f.write("#$ -pe mpi 80 \n \n"); 
        f.write("# 7. Set the Current Working Directory \n"); 
        f.write("#$ -cwd \n \n"); 
        f.write("# 8. Load the correct modules for this version of VASP. This also outputs some information about  \n"); 
         #########Futher commands to be included in this line################
        f.write("module load vasp/5.4.4-18apr2017/intel-2019 \n \n"); 
        f.write("# 9. Run our MPI job. GERun is a wrapper that launches MPI jobs on Legion. \n"); 
        f.write("gerun vasp_std > vasp_output.$JOB_ID \n"); 
        f.close()
        