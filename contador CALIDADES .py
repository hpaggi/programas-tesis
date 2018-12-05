

import io
# -*- coding: Windows-1252 -*-
import codecs
arch="5 ag 20 mens 32 ejec SIMPLE.txt"

LIMITE = 20

f= open(arch, 'r', encoding='ascii', errors='ignore')
Q=[]
C=[]
c=0


for i in range(1,12):
        Q.append(0) 
        C.append(0)
for line1 in f:
        line1=f.readline()
        if line1== "" :
                break
        
        line111=line1.strip() 
        print(line111)
        
        if ("Yo Agente OMEGA. Mi calidad:" in line111) and ("mensajes. Devuelvo el mensaje=" in line111) :
                c =line1.find("nro:") + 5                           
                m = int(line1[c:c+2])                    
                c=line1.find("calidad:") + 9                    
                if  line111[c+3:c+4] == "."  :
                        calidadO =float(line111[c:c+3]) 
                else:
                        calidadO=float(line111[c:c+4])  
                k= int(calidadO*10)       
                Q[k]=Q[k]+1
                
                #calculo la cantidad de mensajes usados en c
                C[k] = C[k] + c

for i in range(0,12):
        if C[i] >0:
                print("q=",i/10,"prom=",C[i]/Q[i])
      
        
