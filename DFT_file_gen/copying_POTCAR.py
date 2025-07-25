
def POTCAR_copy(POTCAR_element_dir, POTCAR_creation_dir):

    fid_POTCAR_in = open(POTCAR_element_dir,'r')
    
    fid_POTCAR_out = open(POTCAR_creation_dir,'a')

    while 1:  
        textline = fid_POTCAR_in.readline()
        if textline == "":
            break
        else:
            fid_POTCAR_out.write(textline)
            
    fid_POTCAR_in.close()
    fid_POTCAR_out.close()   