# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:49:32 2024

@author: shara
"""

import os 

import matplotlib.pyplot as plt

import numpy as np 

################################provide the directiory of the K-Ni(111) sin########################################

dir = "C:/Project3_project4/Project4_Potassium_calc_PBE_D3/KMC_results/KMC_results_JCC_2_1/K_Ni111_2_8/MSR_model_1273K_10bar_1NN_KmodON2.8/"

procstat_file = "procstat_output.txt"

final_dir = os.path.join(dir,procstat_file)

fid = open(final_dir,"r")

textline = "Temp"

count = 0

NSites = 1250;

NSitesKmod = 36*6; 

NSitesKmod_actual = 36*6 + 36;

NsitesNi = NSites - NSitesKmod_actual; 

while textline!= "":
   textline = fid.readline() 
   count = count + 1
   #if(textline.find(textline,"configuration                 6000")):
       
   if(count == 1):      ######configuration                 6000
       b0 = textline
       c0 = b0.split() 
       
   if(count == 11999):      ######configuration                 4000################
     tss =  float(textline.split()[3])
     textline = fid.readline() 
     count = count + 1
     textline = fid.readline()
     count = count + 1
     b1 = textline
     c1 = b1.split() 
     
   if(count == 29999):      ######configuration                 10000################
     tfinal =  float(textline.split()[3])
     textline = fid.readline() 
     count = count + 1
     textline = fid.readline()
     count = count + 1
     b2 = textline
     c2 = b2.split()   
     
   ######configuration                 6000
   
for i in range(len(c0)):
    
 if(c0[i] == "CHOH_formation_fwd"):
  N_CHOH_formation_fwd = float(c2[i]) - float(c1[i])
          
 if(c0[i] == "CHOH_formation_rev"):
  N_CHOH_formation_rev = float(c2[i]) - float(c1[i])       
   
 if(c0[i] == "CHOH_diss_CHO_H_fwd"):
  N_CHOH_CHO_pathway_fwd = float(c2[i]) - float(c1[i])
        
 if(c0[i] == "CHOH_diss_CHO_H_rev"):
  N_CHOH_CHO_pathway_rev = float(c2[i]) - float(c1[i])    
           
 if(c0[i] == "CHOH_diss_COH_H_fwd"):
  N_CHOH_COH_pathway_fwd = float(c2[i]) - float(c1[i])
         
 if(c0[i] == "CHOH_diss_COH_H_rev"):
  N_CHOH_COH_pathway_rev = float(c2[i]) - float(c1[i])    
  
 if(c0[i] == "CHO_formation_fwd"):
  N_CHO_pathway_fwd = float(c2[i]) - float(c1[i])
         
 if(c0[i] == "CHO_formation_rev"):
  N_CHO_pathway_rev = float(c2[i]) - float(c1[i])
  
 if(c0[i] == "COH_formation_fwd"):
  N_COH_pathway_fwd = float(c2[i]) - float(c1[i])
          
 if(c0[i] == "COH_formation_rev"):
  N_COH_pathway_rev = float(c2[i]) - float(c1[i])
             
 if(c0[i] == "CO_formation_fwd"):
  N_CO_pathway_fwd = float(c2[i]) - float(c1[i])
          
 if(c0[i] == "CO_formation_rev"):
  N_CO_pathway_rev = float(c2[i]) - float(c1[i])
  
 if(c0[i] == "CO2_dissociation_fwd"):
  N_CO2_dissociation_fwd = float(c2[i]) - float(c1[i])
   
 if(c0[i] == "CO2_dissociation_rev"):
  N_CO2_dissociation_rev = float(c2[i]) - float(c1[i]) 
   
 if(c0[i] == "CHO_dissociation_fwd"):
  N_CHO_dissociation_fwd = float(c2[i]) - float(c1[i])
    
 if(c0[i] == "CHO_dissociation_rev"):
  N_CHO_dissociation_rev = float(c2[i]) - float(c1[i])
   
 if(c0[i] == "COH_dissociation_fwd"):
  N_COH_dissociation_fwd = float(c2[i]) - float(c1[i])
  
 if(c0[i] == "COH_dissociation_rev"):
  N_COH_dissociation_rev = float(c2[i]) - float(c1[i])  
    
 if(c0[i] == "CO_adsorption_fwd"):
  N_CO_adsorption_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "CO_adsorption_rev"):
  N_CO_adsorption_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2O_adsorption_fwd"):
  N_H2O_adsorption_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2O_adsorption_rev"):
  N_H2O_adsorption_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2O_dissociation_fwd"):
  N_H2O_dissociation_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2O_dissociation_rev"):
  N_H2O_dissociation_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "OH_dissociation_fwd"):
  N_OH_dissociation_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "OH_dissociation_rev"):
  N_OH_dissociation_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2_dissociation_fwd"):
  N_H2_dissociation_fwd = float(c2[i]) - float(c1[i])    

 if(c0[i] == "H2_dissociation_rev"):
  N_H2_dissociation_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "CH_dissociation_fwd"):
  N_CH_dissociation_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "CH_dissociation_rev"):
  N_CH_dissociation_rev = float(c2[i]) - float(c1[i])
  
 if(c0[i] == "CH2_dissociation_fwd"):
  N_CH2_dissociation_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "CH2_dissociation_rev"):
  N_CH2_dissociation_rev = float(c2[i]) - float(c1[i])  
  
 if(c0[i] == "CH3_dissociation_fwd"):
  N_CH3_dissociation_fwd = float(c2[i]) - float(c1[i])
  
 if(c0[i] == "CH3_dissociation_rev"):
  N_CH3_dissociation_rev = float(c2[i]) - float(c1[i])
  
 if(c0[i] == "CH4_dissociation_fwd"):
  N_CH4_dissociation_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "CH4_dissociation_rev"):
  N_CH4_dissociation_rev = float(c2[i]) - float(c1[i])  
  
  
  ###############kmod parsing##################################
  
 if(c0[i] == "CHOH_formation_kmod_fwd"):
  N_CHOH_formation_kmod_fwd = float(c2[i]) - float(c1[i])
          
 if(c0[i] == "CHOH_formation_kmod_rev"):
  N_CHOH_formation_kmod_rev = float(c2[i]) - float(c1[i])         
  
 if(c0[i] == "CO2_dissociation_kmod_fwd"):
  N_CO2_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])
    
 if(c0[i] == "CO2_dissociation_kmod_rev"):
  N_CO2_dissociation_kmod_rev = float(c2[i]) - float(c1[i]) 
    
 if(c0[i] == "CHO_dissociation_kmod_fwd"):
  N_CHO_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])
     
 if(c0[i] == "CHO_dissociation_kmod_rev"):
  N_CHO_dissociation_kmod_rev = float(c2[i]) - float(c1[i])
    
 if(c0[i] == "COH_dissociation_kmod_fwd"):
  N_COH_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])
   
 if(c0[i] == "COH_dissociation_kmod_rev"):
  N_COH_dissociation_kmod_rev = float(c2[i]) - float(c1[i])  
     
 if(c0[i] == "CO_adsorption_kmod_fwd"):
  N_CO_adsorption_kmod_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "CO_adsorption_kmod_rev"):
  N_CO_adsorption_kmod_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2O_adsorption_kmod_fwd"):
  N_H2O_adsorption_kmod_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2O_adsorption_kmod_rev"):
  N_H2O_adsorption_kmod_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2O_dissociation_kmod_fwd"):
  N_H2O_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2O_dissociation_kmod_rev"):
  N_H2O_dissociation_kmod_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "OH_dissociation_kmod_fwd"):
  N_OH_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "OH_dissociation_kmod_rev"):
  N_OH_dissociation_kmod_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "H2_dissociation_kmod_fwd"):
  N_H2_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])    

 if(c0[i] == "H2_dissociation_kmod_rev"):
  N_H2_dissociation_kmod_rev = float(c2[i]) - float(c1[i])

 if(c0[i] == "CH_dissociation_kmod_fwd"):
  N_CH_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "CH_dissociation_kmod_rev"):
  N_CH_dissociation_kmod_rev = float(c2[i]) - float(c1[i])
   
 if(c0[i] == "CH2_dissociation_kmod_fwd"):
  N_CH2_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "CH2_dissociation_kmod_rev"):
  N_CH2_dissociation_kmod_rev = float(c2[i]) - float(c1[i])  
   
 if(c0[i] == "CH3_dissociation_kmod_fwd"):
  N_CH3_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])
   
 if(c0[i] == "CH3_dissociation_kmod_rev"):
  N_CH3_dissociation_kmod_rev = float(c2[i]) - float(c1[i])
   
 if(c0[i] == "CH4_dissociation_Kmod_fwd"):
  N_CH4_dissociation_kmod_fwd = float(c2[i]) - float(c1[i])

 if(c0[i] == "CH4_dissociation_Kmod_rev"):
  N_CH4_dissociation_kmod_rev = float(c2[i]) - float(c1[i])  
   
 if(c0[i] == "CHOH_diss_CHO_H_kmod_fwd"):
   N_CHOH_diss_CHO_H_kmod_pathway_fwd = float(c2[i]) - float(c1[i])
           
 if(c0[i] == "CHOH_diss_CHO_H_kmod_rev"):
   N_CHOH_diss_CHO_H_kmod_pathway_rev = float(c2[i]) - float(c1[i])   

 if(c0[i] == "CHOH_diss_COH_H_kmod_fwd"):
   N_CHOH_diss_COH_H_kmod_pathway_fwd = float(c2[i]) - float(c1[i])
           
 if(c0[i] == "CHOH_diss_COH_H_kmod_rev"):
   N_CHOH_diss_COH_H_kmod_pathway_rev = float(c2[i]) - float(c1[i])   

 if(c0[i] == "CHO_formation_kmod_fwd"):
   N_CHO_formation_kmod_pathway_fwd = float(c2[i]) - float(c1[i])
           
 if(c0[i] == "CHO_formation_kmod_rev"):
   N_CHO_formation_kmod_pathway_rev = float(c2[i]) - float(c1[i])   

 if(c0[i] == "COH_formation_kmod_fwd"):
   N_COH_formation_kmod_pathway_fwd = float(c2[i]) - float(c1[i])
           
 if(c0[i] == "COH_formation_kmod_rev"):
   N_COH_formation_kmod_pathway_rev = float(c2[i]) - float(c1[i])   

 if(c0[i] == "COH_formation_kmod_fwd"):
   N_COH_formation_kmod_pathway_fwd = float(c2[i]) - float(c1[i])
           
 if(c0[i] == "COH_formation_kmod_rev"):
   N_COH_formation_kmod_pathway_rev = float(c2[i]) - float(c1[i])   

 if(c0[i] == "CO_formation_kmod_fwd"):
   N_CO_formation_kmod_pathway_fwd = float(c2[i]) - float(c1[i])
          
 if(c0[i] == "CO_formation_kmod_rev"):
   N_CO_formation_kmod_pathway_rev = float(c2[i]) - float(c1[i])  
  
  
########################################################################################################

rate_CH4_dissociation_fwd = N_CH4_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CH4_dissociation_rev = N_CH4_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))    

net_rate_CH4_dissociation = rate_CH4_dissociation_fwd - rate_CH4_dissociation_rev

pe_ratio_CH4_dissociation = rate_CH4_dissociation_fwd/(rate_CH4_dissociation_fwd + rate_CH4_dissociation_rev)



print(f"{net_rate_CH4_dissociation:.2e}")

rate_CH3_dissociation_fwd = N_CH3_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CH3_dissociation_rev = N_CH3_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CH3_dissociation  = rate_CH3_dissociation_fwd  - rate_CH3_dissociation_rev

pe_ratio_CH3_dissociation = rate_CH3_dissociation_fwd/(rate_CH3_dissociation_fwd + rate_CH3_dissociation_rev)


print(f"{net_rate_CH3_dissociation:.2e}")


rate_CH2_dissociation_fwd = N_CH2_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CH2_dissociation_rev = N_CH2_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))   

net_rate_CH2_dissociation = rate_CH2_dissociation_fwd  - rate_CH2_dissociation_rev

pe_ratio_CH2_dissociation = rate_CH2_dissociation_fwd/(rate_CH2_dissociation_fwd + rate_CH2_dissociation_rev)

print(f"{net_rate_CH2_dissociation:.2e}")


rate_CH_dissociation_fwd = N_CH_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CH_dissociation_rev = N_CH_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))   

net_rate_CH_dissociation = rate_CH_dissociation_fwd - rate_CH_dissociation_rev

pe_ratio_CH_dissociation = rate_CH_dissociation_fwd/(rate_CH_dissociation_fwd + rate_CH_dissociation_rev)


print(f"{net_rate_CH_dissociation:.2e}")


rate_H2_dissociation_fwd = N_H2_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_H2_dissociation_rev = N_H2_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))    

net_rate_H2_dissociation = rate_H2_dissociation_fwd - rate_H2_dissociation_rev

pe_ratio_H2_dissociation = rate_H2_dissociation_fwd/(rate_H2_dissociation_fwd + rate_H2_dissociation_rev)

print(f"{net_rate_H2_dissociation:.2e}")


rate_H2O_adsorption_fwd = N_H2O_adsorption_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_H2O_adsorption_rev = N_H2O_adsorption_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))  

net_rate_H2O_adsorption = rate_H2O_adsorption_fwd - rate_H2O_adsorption_rev 

pe_ratio_H2O_adsorption = rate_H2O_adsorption_fwd/(rate_H2O_adsorption_fwd + rate_H2O_adsorption_rev)

print(f"{net_rate_H2O_adsorption:.2e}")


rate_H2O_dissociation_fwd = N_H2O_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_H2O_dissociation_rev = N_H2O_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_H2O_dissociation = rate_H2O_dissociation_fwd - rate_H2O_dissociation_rev

pe_ratio_H2O_dissociation = rate_H2O_dissociation_fwd/(rate_H2O_dissociation_fwd + rate_H2O_dissociation_rev)

print(f"{net_rate_H2O_dissociation:.2e}")

  
rate_OH_dissociation_fwd = N_OH_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_OH_dissociation_rev = N_OH_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))

net_rate_OH_dissociation = rate_OH_dissociation_fwd - rate_OH_dissociation_rev

pe_ratio_OH_dissociation = rate_OH_dissociation_fwd/(rate_OH_dissociation_fwd + rate_OH_dissociation_rev)

print(f"{net_rate_OH_dissociation:.2e}")


rate_CHOH_formation_fwd = N_CHOH_formation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_formation_rev = N_CHOH_formation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CHOH_formation = rate_CHOH_formation_fwd - rate_CHOH_formation_rev

pe_ratio_CHOH_formation = rate_CHOH_formation_fwd/(rate_CHOH_formation_fwd + rate_CHOH_formation_rev)

print(f"{net_rate_CHOH_formation:.2e}")


rate_CHOH_CHO_pathway_fwd = N_CHOH_CHO_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_CHO_pathway_rev = N_CHOH_CHO_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))        

net_rate_CHOH_CHO_pathway = rate_CHOH_CHO_pathway_fwd - rate_CHOH_CHO_pathway_rev
                                                
#pe_ratio_CHOH_CHO_pathway = rate_CHOH_CHO_pathway_fwd/(rate_CHOH_CHO_pathway_fwd + rate_CHOH_CHO_pathway_rev)

print(f"{net_rate_CHOH_CHO_pathway:.2e}")


rate_CHOH_COH_pathway_fwd = N_CHOH_COH_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_COH_pathway_rev = N_CHOH_COH_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CHOH_COH_pathway = rate_CHOH_COH_pathway_fwd - rate_CHOH_COH_pathway_rev

pe_ratio_CHOH_COH_pathway = rate_CHOH_COH_pathway_fwd/(rate_CHOH_COH_pathway_fwd + rate_CHOH_COH_pathway_rev)

print(f"{net_rate_CHOH_COH_pathway:.2e}")



rate_CHO_pathway_fwd = N_CHO_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CHO_pathway_rev = N_CHO_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))      

net_rate_CHO_pathway = rate_CHO_pathway_fwd - rate_CHO_pathway_rev

pe_ratio_CHO_pathway = rate_CHO_pathway_fwd/(rate_CHO_pathway_fwd + rate_CHO_pathway_rev)


print(f"{net_rate_CHO_pathway:.2e}")



rate_CHO_dissociation_fwd = N_CHO_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CHO_dissociation_rev = N_CHO_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))      

net_rate_CHO_dissociation = rate_CHO_dissociation_fwd - rate_CHO_dissociation_rev

pe_ratio_CHO_dissociation = rate_CHO_dissociation_fwd/(rate_CHO_dissociation_fwd + rate_CHO_dissociation_rev)

print(f"{net_rate_CHO_dissociation:.2e}")




rate_COH_pathway_fwd = N_COH_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_COH_pathway_rev = N_COH_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))            

net_rate_COH_pathway = rate_COH_pathway_fwd - rate_COH_pathway_rev

pe_ratio_COH_pathway = rate_COH_pathway_fwd/(rate_COH_pathway_fwd + rate_COH_pathway_rev)

print(f"{net_rate_COH_pathway:.2e}")


rate_COH_dissociation_fwd = N_COH_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_COH_dissociation_rev = N_COH_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))            

net_rate_COH_dissociation = rate_COH_dissociation_fwd - rate_COH_dissociation_rev

pe_ratio_COH_dissociation = rate_COH_dissociation_fwd/(rate_COH_dissociation_fwd + rate_COH_dissociation_rev)

print(f"{net_rate_COH_dissociation:.2e}")



rate_CO_pathway_fwd = N_CO_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CO_pathway_rev = N_CO_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CO_pathway = rate_CO_pathway_fwd - rate_CO_pathway_rev 

pe_ratio_CO_pathway = rate_CO_pathway_fwd/(rate_CO_pathway_fwd + rate_CO_pathway_rev)

print(f"{net_rate_CO_pathway:.2e}")


rate_CO_adsorption_fwd = N_CO_adsorption_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CO_adsorption_rev = N_CO_adsorption_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CO_adsorption = rate_CO_adsorption_fwd - rate_CO_adsorption_rev 

pe_ratio_CO_adsorption = rate_CO_adsorption_fwd/(rate_CO_adsorption_fwd + rate_CO_adsorption_rev)



rate_CO2_dissociation_fwd = N_CO2_dissociation_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CO2_dissociation_rev = N_CO2_dissociation_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CO2_dissociation = rate_CO2_dissociation_fwd  - rate_CO2_dissociation_rev

pe_ratio_CO2_dissociation = rate_CO2_dissociation_fwd/(rate_CO2_dissociation_fwd + rate_CO2_dissociation_rev)

print(f"{net_rate_CO2_dissociation:.2e}")



########################################################################################################

rate_CH4_dissociation_kmod_fwd = N_CH4_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CH4_dissociation_kmod_rev = N_CH4_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))    

net_rate_CH4_dissociation_kmod = rate_CH4_dissociation_kmod_fwd - rate_CH4_dissociation_kmod_rev

pe_ratio_CH4_dissociation_kmod = rate_CH4_dissociation_kmod_fwd/(rate_CH4_dissociation_kmod_fwd + rate_CH4_dissociation_kmod_rev)



print(f"{net_rate_CH4_dissociation_kmod:.2e}")

rate_CH3_dissociation_kmod_fwd = N_CH3_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CH3_dissociation_kmod_rev = N_CH3_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CH3_dissociation_kmod  = rate_CH3_dissociation_kmod_fwd  - rate_CH3_dissociation_kmod_rev

pe_ratio_CH3_dissociation_kmod = rate_CH3_dissociation_kmod_fwd/(rate_CH3_dissociation_kmod_fwd + rate_CH3_dissociation_kmod_rev)

print(f"{net_rate_CH3_dissociation_kmod:.2e}")


rate_CH2_dissociation_kmod_fwd = N_CH2_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CH2_dissociation_kmod_rev = N_CH2_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))   

net_rate_CH2_dissociation_kmod = rate_CH2_dissociation_kmod_fwd  - rate_CH2_dissociation_kmod_rev

pe_ratio_CH2_dissociation_kmod = rate_CH2_dissociation_kmod_fwd/(rate_CH2_dissociation_kmod_fwd + rate_CH2_dissociation_kmod_rev)

print(f"{net_rate_CH2_dissociation_kmod:.2e}")


rate_CH_dissociation_kmod_fwd = N_CH_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CH_dissociation_kmod_rev = N_CH_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))   

net_rate_CH_dissociation_kmod = rate_CH_dissociation_kmod_fwd - rate_CH_dissociation_kmod_rev

pe_ratio_CH_dissociation_kmod = rate_CH_dissociation_kmod_fwd/(rate_CH_dissociation_kmod_fwd + rate_CH_dissociation_kmod_rev)


print(f"{net_rate_CH_dissociation_kmod:.2e}")


rate_H2_dissociation_kmod_fwd = N_H2_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_H2_dissociation_kmod_rev = N_H2_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))    

net_rate_H2_dissociation_kmod = rate_H2_dissociation_kmod_fwd - rate_H2_dissociation_kmod_rev

pe_ratio_H2_dissociation_kmod = rate_H2_dissociation_kmod_fwd/(rate_H2_dissociation_kmod_fwd + rate_H2_dissociation_kmod_rev)

print(f"{net_rate_H2_dissociation_kmod:.2e}")


rate_H2O_adsorption_kmod_fwd = N_H2O_adsorption_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_H2O_adsorption_kmod_rev = N_H2O_adsorption_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))  

net_rate_H2O_adsorption_kmod = rate_H2O_adsorption_kmod_fwd - rate_H2O_adsorption_kmod_rev 

pe_ratio_H2O_adsorption_kmod = rate_H2O_adsorption_kmod_fwd/(rate_H2O_adsorption_kmod_fwd + rate_H2O_adsorption_kmod_rev)

print(f"{net_rate_H2O_adsorption_kmod:.2e}")


rate_H2O_dissociation_kmod_fwd = N_H2O_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_H2O_dissociation_kmod_rev = N_H2O_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_H2O_dissociation_kmod = rate_H2O_dissociation_kmod_fwd - rate_H2O_dissociation_kmod_rev

pe_ratio_H2O_dissociation_kmod = rate_H2O_dissociation_kmod_fwd/(rate_H2O_dissociation_kmod_fwd + rate_H2O_dissociation_kmod_rev)

print(f"{net_rate_H2O_dissociation_kmod:.2e}")

  
rate_OH_dissociation_kmod_fwd = N_OH_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_OH_dissociation_kmod_rev = N_OH_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))

net_rate_OH_dissociation_kmod = rate_OH_dissociation_kmod_fwd - rate_OH_dissociation_kmod_rev

pe_ratio_OH_dissociation_kmod = rate_OH_dissociation_kmod_fwd/(rate_OH_dissociation_kmod_fwd + rate_OH_dissociation_kmod_rev)

print(f"{net_rate_OH_dissociation_kmod:.2e}")


rate_CHOH_formation_kmod_fwd = N_CHOH_formation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_formation_kmod_rev = N_CHOH_formation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CHOH_formation_kmod = rate_CHOH_formation_kmod_fwd - rate_CHOH_formation_kmod_rev

pe_ratio_CHOH_formation_kmod = rate_CHOH_formation_kmod_fwd/(rate_CHOH_formation_kmod_fwd + rate_CHOH_formation_kmod_rev)

print(f"{net_rate_CHOH_formation_kmod:.2e}")


rate_CHOH_CHO_pathway_kmod_fwd = N_CHOH_diss_CHO_H_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_CHO_pathway_kmod_rev = N_CHOH_diss_CHO_H_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))        

net_rate_CHOH_CHO_pathway_kmod = rate_CHOH_CHO_pathway_kmod_fwd - rate_CHOH_CHO_pathway_kmod_rev
                                                
#pe_ratio_CHOH_CHO_pathway_kmod = rate_CHOH_CHO_pathway_kmod_fwd/(rate_CHOH_CHO_pathway_kmod_fwd + rate_CHOH_CHO_pathway_kmod_rev)

print(f"{net_rate_CHOH_CHO_pathway_kmod:.2e}")


rate_CHOH_COH_pathway_kmod_fwd = N_CHOH_diss_COH_H_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_COH_pathway_kmod_rev = N_CHOH_diss_COH_H_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CHOH_COH_pathway_kmod = rate_CHOH_COH_pathway_kmod_fwd - rate_CHOH_COH_pathway_kmod_rev

pe_ratio_CHOH_COH_pathway_kmod = rate_CHOH_COH_pathway_kmod_fwd/(rate_CHOH_COH_pathway_kmod_fwd + rate_CHOH_COH_pathway_kmod_rev)

print(f"{net_rate_CHOH_COH_pathway_kmod:.2e}")



rate_CHO_pathway_kmod_fwd = N_CHO_formation_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CHO_pathway_kmod_rev = N_CHO_formation_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))      

net_rate_CHO_pathway_kmod = rate_CHO_pathway_kmod_fwd - rate_CHO_pathway_kmod_rev

pe_ratio_CHO_pathway_kmod = rate_CHO_pathway_kmod_fwd/(rate_CHO_pathway_kmod_fwd + rate_CHO_pathway_kmod_rev)


print(f"{net_rate_CHO_pathway_kmod:.2e}")



rate_CHO_dissociation_kmod_fwd = N_CHO_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CHO_dissociation_kmod_rev = N_CHO_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))      

net_rate_CHO_dissociation_kmod = rate_CHO_dissociation_kmod_fwd - rate_CHO_dissociation_kmod_rev

pe_ratio_CHO_dissociation_kmod = rate_CHO_dissociation_kmod_fwd/(rate_CHO_dissociation_kmod_fwd + rate_CHO_dissociation_kmod_rev)

print(f"{net_rate_CHO_dissociation_kmod:.2e}")




rate_COH_pathway_kmod_fwd = N_COH_formation_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_COH_pathway_kmod_rev = N_COH_formation_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))            

net_rate_COH_pathway_kmod = rate_COH_pathway_kmod_fwd - rate_COH_pathway_kmod_rev

pe_ratio_COH_pathway_kmod = rate_COH_pathway_kmod_fwd/(rate_COH_pathway_kmod_fwd + rate_COH_pathway_kmod_rev)

print(f"{net_rate_COH_pathway_kmod:.2e}")


rate_COH_dissociation_kmod_fwd = N_COH_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_COH_dissociation_kmod_rev = N_COH_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))            

net_rate_COH_dissociation_kmod = rate_COH_dissociation_kmod_fwd - rate_COH_dissociation_kmod_rev

pe_ratio_COH_dissociation_kmod = rate_COH_dissociation_kmod_fwd/(rate_COH_dissociation_kmod_fwd + rate_COH_dissociation_kmod_rev)

print(f"{net_rate_COH_dissociation_kmod:.2e}")



rate_CO_pathway_kmod_fwd = N_CO_formation_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CO_pathway_kmod_rev = N_CO_formation_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CO_pathway_kmod = rate_CO_pathway_kmod_fwd - rate_CO_pathway_kmod_rev 

pe_ratio_CO_pathway_kmod = rate_CO_pathway_kmod_fwd/(rate_CO_pathway_kmod_fwd + rate_CO_pathway_kmod_rev)

print(f"{net_rate_CO_pathway_kmod:.2e}")


rate_CO_adsorption_kmod_fwd = N_CO_adsorption_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CO_adsorption_kmod_rev = N_CO_adsorption_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CO_adsorption_kmod = rate_CO_adsorption_kmod_fwd - rate_CO_adsorption_kmod_rev 

pe_ratio_CO_adsorption_kmod = rate_CO_adsorption_kmod_fwd/(rate_CO_adsorption_kmod_fwd + rate_CO_adsorption_kmod_rev)



rate_CO2_dissociation_kmod_fwd = N_CO2_dissociation_kmod_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CO2_dissociation_kmod_rev = N_CO2_dissociation_kmod_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 

net_rate_CO2_dissociation_kmod = rate_CO2_dissociation_kmod_fwd  - rate_CO2_dissociation_kmod_rev

pe_ratio_CO2_dissociation_kmod = rate_CO2_dissociation_kmod_fwd/(rate_CO2_dissociation_kmod_fwd + rate_CO2_dissociation_kmod_rev)

print(f"{net_rate_CO2_dissociation_kmod:.2e}")   














