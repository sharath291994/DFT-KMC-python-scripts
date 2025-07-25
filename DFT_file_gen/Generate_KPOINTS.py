
def vasp_KPOINTS(VASPfiles_Dir):
    import os
    vasp_fldrs = os.listdir(VASPfiles_Dir)
    for i in range(len(vasp_fldrs)):
        KPOINTS_file = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'KPOINTS')
        f = open(KPOINTS_file,"w")
        f.write("Automatic mesh \n")
        f.write("0 \n")
        f.write("Gamma \n")
        f.write("5 5 1 \n")
        f.write("0 0 0 \n")
        f.close()