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
  
  

rate_CHOH_CHO_pathway_fwd = N_CHOH_CHO_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_CHO_pathway_rev = N_CHOH_CHO_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))                                                        


rate_CHOH_COH_pathway_fwd = N_CHOH_COH_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_COH_pathway_rev = N_CHOH_COH_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 


rate_CHO_pathway_fwd = N_CHO_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CHO_pathway_rev = N_CHO_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))          


rate_COH_pathway_fwd = N_COH_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_COH_pathway_rev = N_COH_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))            


rate_CO_pathway_fwd = N_CO_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CO_pathway_rev = N_CO_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))         



########################################################################################################

rate_CHOH_diss_CHO_H_kmod_pathway_fwd = N_CHOH_diss_CHO_H_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_diss_CHO_H_kmod_pathway_rev = N_CHOH_diss_CHO_H_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))                                                        


rate_CHOH_diss_COH_H_kmod_fwd = N_CHOH_diss_COH_H_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                        
rate_CHOH_diss_COH_H_kmod_rev = N_CHOH_diss_COH_H_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss)) 


rate_CHO_formation_kmod_pathway_fwd = N_CHO_formation_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CHO_formation_kmod_pathway_rev = N_CHO_formation_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))          


rate_COH_formation_kmod_pathway_fwd = N_COH_formation_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_COH_formation_kmod_pathway_rev = N_COH_formation_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))            


rate_CO_formation_kmod_pathway_fwd =  N_CO_formation_kmod_pathway_fwd/((NsitesNi + NSitesKmod)*(tfinal - tss))
                                                         
rate_CO_formation_kmod_pathway_rev =  N_CO_formation_kmod_pathway_rev/((NsitesNi + NSitesKmod)*(tfinal - tss))         

########################################################################################################


net_rate_CHOH_CHO_pathway = rate_CHOH_CHO_pathway_fwd - rate_CHOH_CHO_pathway_rev

net_rate_CHOH_COH_pathway = rate_CHOH_COH_pathway_fwd - rate_CHOH_COH_pathway_rev

net_rate_CHO_pathway = rate_CHO_pathway_fwd - rate_CHO_pathway_rev 

net_rate_COH_pathway = rate_COH_pathway_fwd - rate_COH_pathway_rev

net_rate_CO_pathway = rate_CO_pathway_fwd  - rate_CO_pathway_rev

net_rate_CHOH_diss_CHO_H_kmod_pathway  = rate_CHOH_diss_CHO_H_kmod_pathway_fwd - rate_CHOH_diss_CHO_H_kmod_pathway_rev 

net_rate_CHOH_diss_COH_H_kmod_fwd_pathway = rate_CHOH_diss_COH_H_kmod_fwd - rate_CHOH_diss_COH_H_kmod_rev

net_rate_CHO_formation_kmod_pathway = rate_CHO_formation_kmod_pathway_fwd - rate_CHO_formation_kmod_pathway_rev

net_rate_COH_formation_kmod_pathway = rate_COH_formation_kmod_pathway_fwd - rate_COH_formation_kmod_pathway_rev

net_rate_CO_formation_kmod_pathway = rate_CO_formation_kmod_pathway_fwd  - rate_CO_formation_kmod_pathway_rev
                                       

Totat_net_rate = net_rate_CHOH_CHO_pathway + net_rate_CHOH_COH_pathway + net_rate_CHO_pathway + net_rate_COH_pathway + net_rate_CO_pathway + net_rate_CHOH_diss_CHO_H_kmod_pathway + net_rate_CHOH_diss_COH_H_kmod_fwd_pathway + net_rate_CHO_formation_kmod_pathway + net_rate_COH_formation_kmod_pathway + net_rate_CO_formation_kmod_pathway

perc_CHOH_CHO_pathway = (net_rate_CHOH_CHO_pathway/Totat_net_rate)*100

perc_CHOH_COH_pathway = (net_rate_CHOH_COH_pathway/Totat_net_rate)*100

perc_CHO_pathway = (net_rate_CHO_pathway/Totat_net_rate)*100

perc_COH_pathway = (net_rate_COH_pathway/Totat_net_rate)*100

perc_CO_pathway = (net_rate_CO_pathway/Totat_net_rate)*100

perc_CHOH_diss_CHO_H_kmod_pathway = (net_rate_CHOH_diss_CHO_H_kmod_pathway/Totat_net_rate)*100

perc_CHOH_diss_COH_H_kmod_fwd_pathway = (net_rate_CHOH_diss_COH_H_kmod_fwd_pathway/Totat_net_rate)*100

perc_CHO_formation_kmod_pathway = (net_rate_CHO_formation_kmod_pathway/Totat_net_rate)*100

perc_COH_formation_kmod_pathway = (net_rate_COH_formation_kmod_pathway/Totat_net_rate)*100

perc_CO_formation_kmod_pathway = (net_rate_CO_formation_kmod_pathway/Totat_net_rate)*100


perc_array_K_Ni111_1273  = np.array([perc_CHOH_CHO_pathway + perc_CHOH_COH_pathway + perc_COH_pathway + perc_CO_pathway + perc_CHOH_diss_CHO_H_kmod_pathway + perc_CHOH_diss_COH_H_kmod_fwd_pathway, perc_CHO_pathway, 
                           perc_COH_formation_kmod_pathway, perc_CHO_formation_kmod_pathway, 
                           perc_CO_formation_kmod_pathway])

mylabels = ["others", "CHO-Ni-pathway", "CHO-K-pathway", "COH-K-pathway", "CO-K-pathway"]

plt.pie(perc_array_K_Ni111_1273, labels = mylabels, startangle = 90, autopct='%1.0f%%', textprops={'fontname': 'Arial'} )

plt.show()


########include these lines############
#os.chdir('C:/Project3_project4/Project4_Potassium_calc_PBE_D3/DFT_Final_calculations/MSR_Free_energy_images')

#fig1.savefig("CH4_dissociation.png",format="png",dpi=1200,transparent=True)












