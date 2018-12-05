import numpy

import io
# -*- coding: Windows-1252 -*-
import codecs
arch="20 ag 1000 reg32 ejec WEB.txt"
#***********************************************************

f= open(arch, 'r', encoding='ascii', errors='ignore')

#***********************************************************
ESTRICTOS=0
AMPLIOS = 0
cant = 0
mant = 0
calidadant = 0.0
calidadf = 0.0
calidadactual = 0.0
calidadi = 0.0
ciclonuevo = 0
i=0
Qi= []
Qf=[]
line1 = "  "
line111="  "
IT=0
EOF=0
k=0

T_O=0
while not(line1 == ""):
   line1=f.readline()
   line111=line1.strip()
#   print(line111)
   if "SERVICO NO LLEG A ESPERAR" in line111:
      T_O=T_O+1
g=f.close()  
f= open(arch, 'r', encoding='ascii', errors='ignore')


line1= "   "
line111= "    "
EOF=0
EOI=0

for k in range(1,33): 
   EOI=0
   i=0
   Qi=[]
   Qf=[]
   for i in range(1,33): 
      Qi.append(0.00)  
      Qf.append(0.00)    
   
   while  EOF== 0 and EOI == 0 :
      if  ("INICIANDO" in line111)   :
            IT=IT+1
            line1=f.readline()
            line111=line1.strip()
      #      print("espero",line111)
         
      if "FIN DE LA" in line111 :
            EOF=1
            EOI=1
            continue            
 
      if EOI == 1 :
         continue
        
      if " Yo Agente OMEGA tengo mensajes para responder. Mi nivel: 1. Mi calidad: " in line111:
            c =line111.find("nro:") + 5
            m = int(line111[c:c+2])
            c=line111.find("calidad:")+9
            g=line111.find(". Calidad llamador:") -1 
            calidadactual=float(line111[c:g])  
            
         #   print("calidad actual",calidadactual)
            if  Qi[m-1] == 0.0 :
               Qi[m-1]=calidadactual
              
      else:
            if ("Yo Agente OMEGA. Mi calidad:" in line111) and ("mensajes. Devuelvo el mensaje=" in line111) or "Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:" in line111:  
               
               c =line1.find("nro:") + 5
               m = int(line1[c:c+2])                    
               c=line1.find("calidad:") + 9 
               g=line111.find(". Me") -1 
               if  "Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:" in line111:
                  g=line111.find(". Calidad llamador") -1 
               
               calidadO=float(line111[c:g])               
               if  Qf[m-1] == 0.0 :
                        Qf[m-1]= calidadO
               if  "Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:" in line111:
                  if  Qi[m-1] == 0.0 :
                        Qi[m-1]= calidadO                  
      line1=f.readline()   
      line111=line1.strip()
     # print (line111)
      if line111 == "" :
         i=0
         while line111 == "" and i < 100:
            line1=f.readline()   
            line111=line1.strip()
            i=i+1
      if i==100 :
         EOF=1
    
         continue
      if ("ITERACIN" in line111) and ("INICIO" in line111):
         c=line111.find("ITERACIN") + 9  
         nro=int(line111[c:c+1])         
         if nro > k:
            EOI=1
            pass
            continue
     
      if EOI== 1 :
         continue 
      if line111== "":
         pass  
         continue
                   
   for i in range(1,33) :
      if Qf[i-1] > Qi[i-1] :
   #      print(i-1, ESTRICTOS, Qf[i-1], Qi[i-1])
         ESTRICTOS = ESTRICTOS + 1
         AMPLIOS = AMPLIOS +1 
            
      else :
         if Qf[i-1] == Qi[i-1] and Qf[i-1]> 0:
               AMPLIOS = AMPLIOS +1
print("****************************************************************")   
print("Archivo:", arch)
print("***************************************************************")
print (" ESTRICTOS =", ESTRICTOS, "AMPLIOS =", AMPLIOS)
print(" ")
print(" TIME OUTS =", T_O)
print("  ")
f.close()

import numpy

f= open(arch, 'r', encoding='ascii', errors='ignore')

i=0

line1 = "  "
line111="  "
IT=0
EOF=0
k=0


CM=numpy.zeros((32,32), dtype=int) # cantidad de mensajes que quedan luego de responder al mens nro x en la iteracion y

QQ=numpy.zeros((32,32), dtype=float) # calidad con que se respondio al mensaje nro x en la iteracion y

T=numpy.zeros((32,32), dtype=int) # cantidad de mensajes usados pra responder el mensaje nro x en la iteracion y

TC=numpy.zeros((32,32), dtype=int) #Total de mensajes usados para la calidad x en la iteracion y 
P=numpy.zeros((11,32), dtype=float) # promedio de mensajes usados para la calidad x en la iteracion y
N=numpy.zeros((11,32), dtype=int) # cantidad de veces que se respondio con la calidad x en la iteracion y

PP=numpy.zeros(11, dtype=float) # promedio de promedios de mensajes usados para la calidad x en todas las iteraciones
NN=numpy.zeros(11, dtype=int) # cantidad de veces que se respondio con la calidad x en  todas las iteraciones





   #**************************************************      
   
   
ITERACION=" "  
EOF=0
k=1
f.close()
f= open(arch, 'r', encoding='ascii', errors='ignore')
while k < 33 and EOF==0:
  
   ITERACION="ITERACIN "+str(k)+" INICIO"
 #  print(k,ITERACION)
   posicion= True
   while posicion: 
      line1=f.readline()
      line111=line1.strip()            
      if line1 == ""  :
         EOF=1
         posicion = False
         continue
      else:
        # print(line111)
         if ITERACION in line111:
            posicion = False
      continue
   if EOF == 1:
      continue
   
   EOI=0
   while EOF == 0 and EOI == 0:
      line1=f.readline()
      line111=line1.strip()            
      if line1 == ""  :
         EOI=1
         EOF=1
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
         QQ[m-1,k-1]=calidadO
    #     print ('mensaje', m,  QQ[m-1,k-1])
   
   f.close()
   EOF=0
   EOI=0
   f= open(arch, 'r', encoding='ascii', errors='ignore')
   EOI=0
   while EOF == 0 and EOI == 0:
      line1=f.readline()
     # print(line1)
      line111=line1.strip() 
      
     # print(line111)
      if line1 == ""  :
         EOI=1
         continue
      if "FIN DE LA" in line111 :
         EOI=1
         continue
      if "Registro " in line111 and "mensajes." in line111:
       #  print(line111)
         c =line111.find("Registro") + 9
         g=line111.find(":") 
         m = int(line111[c:g])
         c =line111.find(": ") +2
         g=line111.find(" mensajes.")  
         if not "Yo Agente OMEGA. Mi calidad:" in line111:
            aux = int(line111[c:g])
         else:
            aux = 0
         T[m-1, k-1]=aux
   #      print('mensaje',m,'mens usados',line111[c:g], 'c',c,'g',g)
       
   for j in range(1,33):
      aux= int(QQ[j-1, k-1]*10)
      TC[aux, k-1]=T[j-1,k-1]+TC[aux, k-1]
    #  print('reg',j,'iterac',k,'indice calidad',aux,'mens usados para ese reg',T[j-1,k-1],'total mens para cal.',TC[aux, k-1]) 
      if T[aux,k-1] > 0:
         N[aux,k-1]=N[aux,k-1]+1
        # print('reg',j, 'aux',aux, N[aux,k-1])
     
   k=k+1
  
   
for j in range(1,12) :
   for k in range (1,33):
      if N[j-1,k-1] > 0:
         P[j-1,k-1]=TC[j-1, k-1]/N[j-1,k-1]
      else:
         P[j-1,k-1]=TC[j-1, k-1]
   for k in range (1,33):
      PP[j-1]= P[j-1,k-1]+ PP[j-1]
      NN[j-1]= N[j-1,k-1] + NN[j-1]
if NN[j-1]>0:
   PP[j-1]=PP[j-1]/NN[j-1]
       

      
      
#************************************************
print ("PROMEDIOS DE MENS POR CALIDAD")
for j in range (0,11):
   print ("Calidad", j/10,"promedio", PP[j])
print(" ")
print("para excel:")
print(" ")
for j in range (0,11):
   print (PP[j])   
   
#*************************************************







