
def vasp_POSCAR(VASPfiles_Dir,POSCAR_loc_dir):
    
    import shutil
    import os
    
    files = os.listdir(POSCAR_loc_dir)

    for i in range(len(files)):
        if("POSCAR" in files[i]):
            vasp_dir_file_name = files[i][7:]
            destination = os.path.join(VASPfiles_Dir,vasp_dir_file_name)
            os.mkdir(destination)
            print("The dirctory has been created as", vasp_dir_file_name,"at destination")
            POSCAR_File_name = files[i]
            source_POSCAR = os.path.join(POSCAR_loc_dir,POSCAR_File_name)
            shutil.copy(source_POSCAR,destination)
            os.chdir(destination)
            os.rename(files[i],'POSCAR')
            os.chdir(POSCAR_loc_dir)            
    
    
    