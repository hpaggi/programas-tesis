

import numpy



import io
# -*- coding: Windows-1252 -*-
import codecs

arch="5 ag 10 mens 32 ejec SIMPLE.txt"

f= open(arch, 'r', encoding='ascii', errors='ignore')

i=0

line1 = "  "
line111="  "
IT=0
EOF=0
k=0


CM=numpy.zeros((32,32), dtype=int) # cantidad de mensajes que quedan luego de responder al mens nro x en la iteracion y

Q=numpy.zeros((32,32), dtype=float) # calidad con que se respondio al mensaje nro x en la iteracion y

T=numpy.zeros((32,32), dtype=int) # cantidad de mensajes usados pra responder el mensaje nro x en la iteracion y

TC=numpy.zeros((32,32), dtype=int) #Total de mensajes usados para la calidad x en la iteracion y 
P=numpy.zeros((11), dtype=float) # promedio de mensajes usados para la calidad x considerando todas las iteraciones
N=numpy.zeros((11), dtype=int) # cantidad de veces que se respondio con la calidad x 


LIMITE=10  # nro de mensajes max del agente


        
 #**************************************************                   

for k in range(1,32):
      EOI=0
      while EOF == 0 and EOI == 0:
            line1=f.readline()
            line111=line1.strip()            
            if line1 == ""  :
                  EOI=1
                  continue
            if "FIN DE LA" in line111 :
                  EOI=1
                  continue
            if " Yo Agente OMEGA. Mi calidad:" in line111 and "mensajes. Devuelvo el mensaje= " in line111:
                  c =line111.find("nro:") + 5
                  m = int(line111[c:c+2])
                  c=line111.find("calidad:") + 9 
                  g=line111.find(". Me")-1
                  calidadO =float(line111[c:g] )             
                  Q[m-1,k-1]=calidadO
              #    print(Q[(m-1)*32+k])
                  c =line111.find("quedan") + 7
                  i= int((m-1)*32+k)
                  g=line111.find("mensajes")-1
                  CM[m-1,k-1]= int(line111[c:g])
                  
              #    print("mensaje",m, "calidad",calidadO,"quedan",CM[i])
                                 
             #     print ("calidad",calidadO,"quedan",CM[m-1,k-1])
                              
      for i in range (1,33):
            if i == 1:
                  T[i-1,k-1] = LIMITE - CM [i-1,k-1]
            else:
                  T[i-1,k-1] = CM[i-2,k-1] - CM [i-1,k-1]
     
            
        
         #   print("mensaje",i, "use",T[(i-1)*32+k])
          

#for i1 in range (1,33):
#      for j1 in range (1,33):
#             print(T[(i1-1)*33+j1], " ", end="")
#      print(".")      

      
for k in range (1,33):
      for i in range(1,33):
            aux= int(Q[i-1,k-1]*10)
            TC[aux,k-1]=T[i-1,k-1]+TC[aux,k-1]
        #    print("mens por calidad","calidad", int(Q[i-1,k-1]*10), "tot mens", TC[aux,k-1], "mens", i)
            
            
for j in range(1,12):
      P[j-1]=0.0
      
      
for j in range(1,12):
      for k in range (1,33):
            P[j-1]= TC[j-1,k-1]+P[j-1]
         #   print("j",j,"p",P[j-1],"k",k,"TC",TC[j-1,k-1])
            if TC[j-1][k-1]>0:
                  N[j-1]=N[j-1]+1
      print (P[j-1])
      if N[j-1] > 0:
            P[j-1]=P[j-1]/N[j-1]
      else:
            P[j-1]=0 




#************************************************
for j in range (0,11):
      print ("Calidad", j/10,"promedio", P[j])
#*************************************************
#print ("PROMEDIOS DE MENS POR CALIDAD",P)
            
           



