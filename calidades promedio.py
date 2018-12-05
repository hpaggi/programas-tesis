


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


CM=[] # cantidad de mensajes que quedan luego de responder al mens nro x en la iteracion y
Q=[] # calidad con que se respondio al mensaje nro x en la iteracion y
T=[] # cantidad de mensajes usados pra responder el mensaje nro x en la iteracion y
TC=[] #Total de mensajes usados para la calidad x en la iteracion y 
P=[0.0] # promedio de mensajes usados para la calidad x considerando todas las iteraciones
N=[0] # cantidad de veces que se respondio con la calidad x 


LIMITE=10  # nro de mensajes max del agente


for i in range(1,12):
      N.append(0)
      P.append(0)
      for j in range(1,33):
            TC.append(0.0)
TC.append(0.0)            
for i in range(1,33):
      for j in range(1,33):
            CM.append(0.0)
            Q.append(0.0)
            T.append(0.0)
CM.append(0.0)
Q.append(0.0)
T.append(0.0)           
 #**************************************************                   

for k in range(1,2):
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
                  Q[(m-1)*32+k]=calidadO
              #    print(Q[(m-1)*32+k])
                  c =line111.find("quedan") + 7
                  i= int((m-1)*32+k)
                  g=line111.find("mensajes")-1
                  CM[i]= int(line111[c:g])
                  
              #    print("mensaje",m, "calidad",calidadO,"quedan",CM[i])
                                 
                  print ("calidad",calidadO,"quedan",CM[m-1][k])
                              
      for i in range (1,33):
            if i == 1:
                  T[(i-1)*32+k] = LIMITE - CM [(i-1)*32+k]
            else:
                  T[(i-1)*32+k] = CM[(i-2)*32+k] - CM [(i-1)*32+k]
     
            
        
         #   print("mensaje",i, "use",T[(i-1)*32+k])
          

#for i1 in range (1,33):
#      for j1 in range (1,33):
#             print(T[(i1-1)*33+j1], " ", end="")
#      print(".")      

      
for k in range (1,33):
      for i in range(1,33):
            aux= (int(Q[(i-1)*32+k]*10)-1)*11+k
            TC[aux]=T[(i-1)*32+k]+TC[aux]
            print("mens por calidad","calidad", int(Q[(i-1)*32+k]*10), "tot mens", TC[aux], "mens", i)
            
            
for j in range(1,12):
      P[j]=0.0
      
      
for j in range(1,12):
      for k in range (1,33):
            P[j]= TC[(j-1)*11+k]+P[j]
            print("j",j,"p",P[j],"k",k,"TC",TC[(j-1)*11+k])
            if TC[(j-1)*11+k]>0:
                  N[j]=N[j]+1
      print (P[j])
      if N[j] > 0:
            P[j]=P[j]/N[j]
      else:
            P[j]=0 
for j in range (0,11):
      print ("Calidad", j/10,"promedio", P[j])
      

#print ("PROMEDIOS DE MENS POR CALIDAD",P)
            
           



