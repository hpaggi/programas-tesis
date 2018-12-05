

import io
# -*- coding: Windows-1252 -*-
import codecs
f= open("30 ag 15 mens 32 ejec SIMPLE.txt", 'r', encoding='ascii', errors='ignore')
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
for i in range(1,39): 
    # deberia ser 39 en vez de 3
    Qi.append(0.00)  
    Qf.append(0.00)
while not ("ITERACIÓN 32 FIN" in line111 ) or EOF == 1 :
 #  print ("/////***** ESTRICTOS =", ESTRICTOS, "AMPLIOS =", AMPLIOS,  "*****\\\\\\")
    line1=f.readline()
   
  # print(">>>>>>>>>>>", line1)
    #line11 = line1.encode(encoding='UTF-8')
    #line111=codecs.decode(line11)
    line111=line1.strip() 
    #if line111=="" :
    #    break
    EOF=1
    i=0
    while i < 10 :
        if line111 == "" or line111=="\n":
            print(i)
            i=i+1
            line1=f.readline()
            line111=line1.strip()
        else:
            if "ITERACIÓN 32 FIN" in line111: 
                break
            else :
                EOF=0
                break    
    if EOF ==1 :
        break
    print("**** ",line111)
    if  ("INICIANDO" in line111)   :
        IT=IT+1
       # print (Qf)
        
        for i in range(1,39) :
            if Qf[i-1] > Qi[i-1] :
                ESTRICTOS = ESTRICTOS + 1
                AMPLIOS = AMPLIOS +1
        #        print(AMPLIOS)
            else :
                if Qf[i-1] == Qi[i-1] and Qf[i-1]> 0:
                    AMPLIOS = AMPLIOS +1
         #       print(ESTRICTOS)
        del Qi[:]
        del Qf[:]            
        for i in range(1,39):
            # deberia ser 39 en vez de 3
            Qi.append(0.00)    
            Qf.append(0.00)  
        while not (("ITERACION" in line111) and ("INICIO" in line111)) and EOF == 0 :
            ciclonuevo =1
            line1=f.readline()
            line111=line1.strip()
            EOF=1
            if "ITERACION 32 FIN" in line111 :
                EOF=1
                for j in range(1,39) :
                    if Qf[j-1] > Qi[j-1] :
                        ESTRICTOS = ESTRICTOS + 1
                        AMPLIOS = AMPLIOS +1
                                       #        print(AMPLIOS)
                    else :
                        if Qf[j-1] == Qi[j-1] and Qf[j-1]> 0:
                            AMPLIOS = AMPLIOS +1
                                         #       print(ESTRICTOS)                    
                          
                print ("/////***** ESTRICTOS =", ESTRICTOS, "AMPLIOS =", AMPLIOS,  "*****\\\\\\")
                break            
            i=0
            while i < 10 :
                if line1 == "" or line1=="\n":
                    print(i)
                  
                    i=i+1
                    line1=f.readline()
                else:
                    EOF=0
                    break
            if EOF == 1 :
                for j in range(1,39) :
                    if Qf[j-1] > Qi[j-1] :
                        ESTRICTOS = ESTRICTOS + 1
                        AMPLIOS = AMPLIOS +1
                        #        print(AMPLIOS)
                    else :
                        if Qf[j-1] == Qi[j-1] and Qf[j-1]> 0:
                            AMPLIOS = AMPLIOS +1
                            #       print(ESTRICTOS)                    
                    print ("/////***** ESTRICTOS =", ESTRICTOS, "AMPLIOS =", AMPLIOS,  "*****\\\\\\")
                    print (Qi , Qf)
                
                continue
         
            line111=line1.strip() 
      #      print(">>>>>>>>>>",line111)
            if "ITERACION 32 FIN" in line111 :
                EOF=1
                print ("/////***** ESTRICTOS =", ESTRICTOS, "AMPLIOS =", AMPLIOS,  "*****\\\\\\")
                break
                
       #     print(">>>>>>>>",line111[1:100])
        
            if " Yo Agente OMEGA tengo mensajes para responder. Mi nivel: 1. Mi calidad: " in line111 :  
                print("XXXXXXXXXXXXXXXXXX")
                c =line111.find("nro:") + 5
                m = int(line111[c:c+2])
                c=line111.find("calidad:") + 9                  
                if    line111[c+3:c+4] == "."  :
                    calidadactual =float(line111[c:c+3])
                else:
                    calidadactual=float(line111[c:c+4])  
                if  Qi[m-1] == 0.0 :
                    Qi[m-1]=calidadactual
                
            else:
                if ("Yo Agente OMEGA. Mi calidad:" in line111) and ("mensajes. Devuelvo el mensaje=" in line111):
                    print("YYYYYYYYYY")
                    c =line1.find("nro:") + 5
                              
                    m = int(line1[c:c+2])                    
                    c=line1.find("calidad:") + 9                    
                    if  line111[c+3:c+4] == "."  :
                        calidadO =float(line111[c:c+3]) 
                    else:
                        calidadO=float(line111[c:c+4])         
                    Qf[m-1]= calidadO
            #        print(' Calidad final',m, Qf[m-1] )
                   
else:
    print ("/////***** ESTRICTOS =", ESTRICTOS, "AMPLIOS =", AMPLIOS,  "*****\\\\\\")

