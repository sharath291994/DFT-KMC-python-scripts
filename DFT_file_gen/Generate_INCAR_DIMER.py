
###This is a function to create the INCAR files#############################

def vasp_INCAR_DIMER(VASPfiles_Dir):
    import os
    vasp_fldrs = os.listdir(VASPfiles_Dir)
    for i in range(len(vasp_fldrs)):
        INCAR_file = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'INCAR')
        f = open(INCAR_file,"w")
        
        ###################DIMER Calculations###########################
        f.write("ICHAIN = 2  \n")
        f.write("IBRION = 3 \n") 
        f.write("POTIM  = 0.0  \n")
        f.write("IOPT  = 2   \n")
        
        f.write("EDIFF = 1.00e-05 \n")  ## (Two decimal places)
        f.write("EDIFFG = -0.01 \n")    ## (Two decimal places)
        f.write("NSW = 500 \n")
        f.write("NELM = 300 \n")
        f.write("ISMEAR = 1 \n")
        f.write("SIGMA = 0.2 \n")
        f.write("LWAVE = .FALSE. \n") 
        f.write("LCHARG = .FALSE. \n")
        f.write("ENCUT = 415.00 \n")      ## (Two decimal places)
        f.write("ALGO = Fast \n")
        f.write("LREAL = Auto \n")
        f.write("GGA = PE \n")
        f.write("IVDW = 11 \n")
        f.write("LDIPOL = .TRUE. \n")
        f.write("IDIPOL = 3 \n")
        f.write("DIPOL = 0.50 0.50 0.50 \n")  #  ## (Two decimal places)#
        f.write("LASPH = .TRUE. \n") #######To be discussed########
        f.write("NPAR = 4 \n")
        f.write("KPAR = 4 \n")
        f.close()

