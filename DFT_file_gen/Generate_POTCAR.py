##########The recommended pseudopotentials are being used to V, H, C and O###################

from copying_POTCAR import POTCAR_copy

def vasp_POTCAR(VASPfiles_Dir,Pseudopptential_dir):
    import os
    #from copying_POTCAR import POTCAR_copy
    vasp_fldrs = os.listdir(VASPfiles_Dir)
    for i in range(len(vasp_fldrs)):
        POSCAR_file = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'POSCAR')
        fid_POSCAR = open(POSCAR_file,"r")
        j = 0
        while 1:
            j = j + 1 
            line = fid_POSCAR.readline()
            if(j==6):  ####The sixth line of POSCAR contains the elements##
                elements = line.split()
                break
        print('There are totally ' + str(len(elements)) + ' elements in the system ' + str(vasp_fldrs[i] + ' \n'))    
        print(elements)
        fid_POSCAR.close()    
        
        ############POTCAR creation############
        POTCAR_creation_dir = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'POTCAR')
        pspot_fldrs = os.listdir(Pseudopptential_dir)    
        for m in range(len(elements)):
            for k in range(len(pspot_fldrs)): ######Covering all cases for POTCAR copy 
                if len(elements[m]) == 2 and len(pspot_fldrs[k]) == 2:
                    if elements[m] in pspot_fldrs[k][0:2]:
                        POTCAR_creation_dir = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'POTCAR') 
                        POTCAR_element_dir = os.path.join(Pseudopptential_dir,pspot_fldrs[k],'POTCAR')
                        POTCAR_copy(POTCAR_element_dir, POTCAR_creation_dir)
                        print("The POTCAR has been copied from fldr " + str(pspot_fldrs[k]) + " for the element " + str(elements[m]))
            
                elif len(elements[m]) == 2 and len(pspot_fldrs[k]) > 2 and pspot_fldrs[k][2] == "_":
                    if elements[m] in pspot_fldrs[k][0:2]:
                        POTCAR_creation_dir = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'POTCAR') 
                        POTCAR_element_dir = os.path.join(Pseudopptential_dir,pspot_fldrs[k],'POTCAR')
                        POTCAR_copy(POTCAR_element_dir, POTCAR_creation_dir)
                        print("The POTCAR has been copied from fldr " + str(pspot_fldrs[k]) + " for the element " + str(elements[m]))
            
                elif len(elements[m]) == 1 and len(pspot_fldrs[k]) == 1:   
                    if elements[m] in pspot_fldrs[k][0:1]:
                        POTCAR_creation_dir = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'POTCAR')
                        POTCAR_element_dir = os.path.join(Pseudopptential_dir,pspot_fldrs[k],'POTCAR')
                        POTCAR_copy(POTCAR_element_dir, POTCAR_creation_dir)
                        print("The POTCAR has been copied from fldr " + str(pspot_fldrs[k]) + " for the element " + str(elements[m]))
            
                elif len(elements[m]) == 1 and len(pspot_fldrs[k]) > 1 and pspot_fldrs[k][1] == "_":
                    if elements[m] in pspot_fldrs[k][0:1]:
                        POTCAR_creation_dir = os.path.join(VASPfiles_Dir,vasp_fldrs[i],'POTCAR') 
                        POTCAR_element_dir = os.path.join(Pseudopptential_dir,pspot_fldrs[k],'POTCAR')
                        POTCAR_copy(POTCAR_element_dir, POTCAR_creation_dir)
                        print("The POTCAR has been copied from fldr " + str(pspot_fldrs[k]) + " for the element " + str(elements[m]))
            
            
           
          
  