# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:39:38 2024

@author: shara
"""

import os 

import matplotlib.pyplot as plt

import numpy as np 

#############################################################################################################

from pathway_analysis_Ni111_973 import perc_array_Ni111_973

from pathway_analysis_Ni111_1273K import perc_array_Ni111_1273

from pathway_analysis_K_Ni111_973 import perc_array_K_Ni111_973

from pathway_analysis_K_Ni111_1273 import perc_array_K_Ni111_1273

#############################################################################################################


script_dir = os.getcwd()

mylabels = ["others (2%)", "CHO-Ni-pathway (98%)"]

#plt.subplot(2, 2, 1)  # 1 row, 2 columns, first subplo

colors = ["blue", "green"]

fig1, axs1 = plt.subplots(1,figsize=(6, 6))

axs1.pie(perc_array_Ni111_973, labels = mylabels, startangle = -90, colors = colors, textprops={'fontsize': 18, 'fontfamily': 'Arial'})

#for autotext in autotexts:
 #   autotext.set_fontsize(14)  # Set desired fontsize for autopct
  #  autotext.set_fontfamily('Arial')  # Optional
    
os.chdir('C:/Project3_project4/Project4_Potassium_calc_PBE_D3/KMC_results/KMC_results_JCC_2_1/Results_post_processing/Pathway_Flux_analysis/Final_images')

fig1.savefig("MSR_pathways_Ni111_973K.png",format="png",dpi=1200,transparent=True)

os.chdir(script_dir)

plt.show()

#plt.subplot(2, 2, 2)  # 1 row, 2 columns, first subplo

colors = ["blue", "green","yellow"]

mylabels = ["others (3%)", "CHO-Ni-pathway (83%)", "COH-Ni-pathway (14%)"]

fig2, axs2 = plt.subplots(1,figsize=(6, 6))

axs2.pie(perc_array_Ni111_1273, labels = mylabels, startangle = -90, colors = colors, textprops={'fontsize': 18, 'fontfamily': 'Arial'})

os.chdir('C:/Project3_project4/Project4_Potassium_calc_PBE_D3/KMC_results/KMC_results_JCC_2_1/Results_post_processing/Pathway_Flux_analysis/Final_images')

fig2.savefig("MSR_pathways_Ni111_1273K.png",format="png",dpi=1200,transparent=True)

os.chdir(script_dir)

plt.show()


#######################################################################, autopct='%1.0f%%'#######################################################

colors = ["blue", "green","purple"]

mylabels = ["others (6%)", "CHO-Ni-pathway (88%)", "CO-K-pathway (6%)"]

fig3, axs3 = plt.subplots(1,figsize=(6, 6))

axs3.pie(perc_array_K_Ni111_973, labels = mylabels, startangle =-90, colors = colors, textprops={'fontsize': 18, 'fontfamily': 'Arial'})


os.chdir('C:/Project3_project4/Project4_Potassium_calc_PBE_D3/KMC_results/KMC_results_JCC_2_1/Results_post_processing/Pathway_Flux_analysis/Final_images')

fig3.savefig("MSR_pathways_K_Ni111_973K.png",format="png",dpi=1200,transparent=True)

os.chdir(script_dir)

plt.show()

##############################################################################################################################




##############################################################################################################################

mylabels = ["others (2%)", "CHO-Ni-pathway (29%)","COH-K-pathway (4%)", "CHO-K-pathway (8%)", "CO-K-pathway (57%)"]

colors = ["blue", "green","red","orange","purple"]

fig4, axs4 = plt.subplots(1,figsize=(8, 8))

axs4.pie(perc_array_K_Ni111_1273, labels = mylabels, startangle = -180, colors = colors, textprops={'fontsize': 24, 'fontfamily': 'Arial'})

#for autotext in autotexts:
 #   autotext.set_fontsize(14)  # Set desired fontsize for autopct
  #  autotext.set_fontfamily('Arial')  # Optional
    
os.chdir('C:/Project3_project4/Project4_Potassium_calc_PBE_D3/KMC_results/KMC_results_JCC_2_1/Results_post_processing/Pathway_Flux_analysis/Final_images')

fig4.savefig("MSR_pathways_K_Ni111_1273K.png",format="png",dpi=1200,transparent=True)

os.chdir(script_dir)

plt.show()


##############################################################################################################################

 



