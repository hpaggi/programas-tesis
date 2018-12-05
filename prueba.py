import io
import codecs

# -*- coding: Windows-1252 -*-
f= open("30 ag 1000 reg 32 ejec SIMPLE.txt", 'r', encoding='ascii', errors='ignore')

line111=" "
line1=b"a" 

line1=f.read()
#line111 = bytes.decode(line1)
#    line111=codecs.decode(line11)    
print(line1)
print(">>>>>>>>>>>",line111)
        
    
    
#while not(line1 == ''):
#    line1=f.readline()
#    #en line 11 deberiaponer la version en bytes de line 1
#    line11 = line1.encode(encoding='UTF-8')
#    line111=codecs.decode(line11)
#    print(line1, line1[66:74] )
#    if  (("ITERACI" in line111) and ("INICIO" in line111))  :
#        print("svsvsvosnvsoivnSOInvSOvnSDvSDL")