import io
import codecs

# -*- coding: Windows-1252 -*-
f= open("30 ag 1000 reg 32 ejec SIMPLE.txt", 'r', encoding='ascii', errors='ignore')
i=1
line111="  "
line1="  "
for line1 in f :
  i=i+1
  while i in range (1,70):
    
    line1=f.readline()
    print(line1)
    line11=line1.strip()
    print(">>>>>>>>>>>",line11)   
#    #en line 11 deberiaponer la version en bytes de line 1
#    line11 = line1.encode(encoding='UTF-8')
#    line111=codecs.decode(line11)
#    print(line1, line1[66:74] )
#    if  (("ITERACI" in line111) and ("INICIO" in line111))  :
#        print("svsvsvosnvsoivnSOInvSOvnSDvSDL")
    
    
    
#while not(line1 == ''):
#    line1=f.readline()
#    #en line 11 deberiaponer la version en bytes de line 1
#    line11 = line1.encode(encoding='UTF-8')
#    line111=codecs.decode(line11)
#    print(line1, line1[66:74] )
#    if  (("ITERACI" in line111) and ("INICIO" in line111))  :
#        print("svsvsvosnvsoivnSOInvSOvnSDvSDL")