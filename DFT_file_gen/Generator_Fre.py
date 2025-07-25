#!/bin/env python3
import linecache
import os
import shutil
linecache.clearcache()
filename = 'POSCAR'
freqname = 'freq15'
weigh = 0.2
filename1 = filename +'_add'
filename2 = filename +'_sub'
filename3 = filename +'_generating'
name1 = 'Addition'
name2 = 'Subtraction'



a1 = []
for n in range (3):
    a = linecache.getline(filename,n+3)        
    b = a.replace(' ','\n')
    a = b
    with open(filename3,'w') as ff:
        ff.write(b)
    with open(filename3,'r') as f:
        a = f.readlines()
        for i in range(len(a)):
            b = a[i].replace('\n','')
            a[i] = b
        while '' in a:
            a.remove('')
        for i in range(len(a)):
            b = eval(a[i])
            a[i] = b
    a1.extend([a[0],a[1],a[2]])
    
    
    
    
    
with open(filename2,'w') as ff:
    for i in range(8):  
        a = linecache.getline(filename,i+1)
        ff.write(a)
    ff.write('Cartesian\n')
with open(filename1,'w') as ff:
    for i in range(8):  
        a = linecache.getline(filename,i+1)
        ff.write(a)
    ff.write('Cartesian\n')








################################## n1 #########################################
a = linecache.getline(filename,7)
b = a.replace(' ','\n')
with open(filename3,'w') as ff:
    ff.write(b)
with open(filename3,'r') as ff:
    a = ff.readlines()
    for i in range(len(a)):
        b = a[i].replace('\n','')
        a[i] = b
    while '' in a:
        a.remove('')
    for i in range(len(a)):
        b = eval(a[i])
        a[i] = b
n1 = 0
for i in range(len(a)):
    n1 = n1 + a[i] #calculate the total number of atoms (n1)
################################# n1 ##########################################




for n in range (n1):
    a = linecache.getline(filename,n+10)
    e2 = a.find("F")
    b = a.replace(' ','\n')
    a = b
    b = a.replace('T','\n')
    a = b
    b = a.replace('F','\n')
    with open(filename3,'w') as ff:
        ff.write(b)
    with open(filename3,'r') as ff:
        a = ff.readlines()
        for i in range(len(a)):
            b = a[i].replace('\n','')
            a[i] = b
        while '' in a:
            a.remove('')
        for i in range(len(a)):
            b = eval(a[i])
            a[i] = b
    a2 = linecache.getline(freqname,n+3)
    b = a2.replace(' ','\n')
    a2 = b
    with open(filename3,'w') as ff:
        ff.write(b)
    with open(filename3,'r') as ff:
        a2 = ff.readlines()
    for i in range(len(a2)):
        b = a2[i].replace('\n','')
        a2[i] = b
    while '' in a2:
        a2.remove('')
    for i in range(len(a2)):
        b = eval(a2[i])
        a2[i] = b
    b1 = a[0]*a1[0]+a[1]*a1[3]+a[2]*a1[6]+a2[3]*weigh
    b2 = a[0]*a1[1]+a[1]*a1[4]+a[2]*a1[7]+a2[4]*weigh
    b3 = a[0]*a1[2]+a[1]*a1[5]+a[2]*a1[8]+a2[5]*weigh
    atem = a
    a[0] = b1
    a[1] = b2
    a[2] = b3
    aa = [str(i) for i in a]
    ab = ' '.join(aa)
    with open(filename1,'a') as ff:
        if e2>=0:
            ff.write(ab+" F F F\n")
        else:
            ff.write(ab+" T T T\n")
    a = atem
    b1 = a[0]-2*a2[3]*weigh
    b2 = a[1]-2*a2[4]*weigh
    b3 = a[2]-2*a2[5]*weigh
    a[0] = b1
    a[1] = b2
    a[2] = b3
    aa = [str(i) for i in a]
    ab = ' '.join(aa)
    with open(filename2,'a') as ff:
        if e2>=0:
            ff.write(ab+" F F F\n")
        else:
            ff.write(ab+" T T T\n")
os.remove(filename3)
linecache.clearcache()
os.mkdir(name1)
os.mkdir(name2)
shutil.move(filename1,name1)
os.chdir(name1)
os.rename(filename1,"POSCAR")
os.chdir(os.pardir)
shutil.move(filename2,name2)
os.chdir(name2)
os.rename(filename2,"POSCAR")
linecache.clearcache()