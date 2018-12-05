#*******************************************************************************************************

#*****************************************************************************************

def analizador (archivo, s, TC, N, T, ERR):
    import numpy
    import io
    # -*- coding: Windows-1252 -*-
    import codecs
    
    
    arch=archivo
     
   # print(s)
   
    #***********************************************************
   
    try: 
        f= open(arch, 'r', encoding='ascii', errors='ignore')
        
        R= open(s,'a')
    except:
        print("******* archivo inexistente ******")
        ERR=1
        return
    
    #***********************************************************
    calidadactual = 0.0
    i=0
    line1 = "  "
    line111="  "
    IT=0
    EOF=0
    k=0
    QQ=numpy.zeros((32,32), dtype=float)   
    line1= "   "
    line111= "    "
    Qi=numpy.zeros(32, dtype=float) 
    Qf=numpy.zeros(32, dtype=float) 
    k=1
         
    TC.fill(0)
    N.fill(0)
    T.fill(0)
    QQ.fill(0)


    line111 = "  "
    line1=  "  "
    EOI=0
    i=0
    EOB=0
    EOF=0
    EOI=0    
    while not  EOF==1 :
        
        line1=f.readline()
        line111=line1.strip()
  #      print(line111)
        if line111.find("INICIANDO",0,len(line1))>0:
            EOI=0
            break            
        #
        #print(line1)
        if len(line1)==0:
            EOF=1
            break
        
    ITER=1
    Qf.fill(-1)
    Qi.fill(-1)
   #     print("inicializo para iter "+str(ITER))
    for kk in range(0,11):
        N[kk,ITER-1]=0      
    while EOF == 0:         
        while  ITER < 33   and EOF==0:
             #     print("inicializo para iter "+str(ITER))
                      
                line1=f.readline()
                line111=line1.strip()
                if len(line1)==0:
                    EOF=1
                
               # print(line111)
                if len(line1)<2:
                    cuenta=0
                    while len(line1) ==1 and cuenta < 100:
                        line1=f.readline()
                        line111=line1.strip()
                        cuenta=cuenta+1
                        if len(line1) == 0:
                            EOF=1
                            ITER=ITER+1
                            k=ITER
                            EOI=1
                     #   print("*******EOF******")
                        break          
                if EOF==1 :
                    continue
                else:   
                    
                    if line1.find("FIN DE LA",0,len(line1)) >0  :
                        EOI=1
                       
                         #     print("inicializo para iter "+str(ITER))
                        ITER=ITER+1
                                             
                        if ITER < 32:
                            for kk in range(0,11):
                                N[kk,ITER]=0
                        Qf.fill(-1) 
                        Qi.fill(-1)
                        k=ITER
                        continue            
                                   
                    if line1.find(" Yo Agente OMEGA tengo mensajes para responder. Mi nivel: 1. Mi calidad: ",0,len(line1))>0:                                                                                          
                     #   print("suksdns2")
                        c =line111.find("nro:") + 5
                        m = int(line111[c:c+2])
                        c=line111.find("calidad:")+9
                        g=line111.find(". Calidad llamador:") -1 
                        calidadactual=float(line111[c:g])  
                        if Qi[m-1] == -1:
                            Qi[m-1]=calidadactual
                        #    print("iter ",k, " mensaje ",m," calidad actual",calidadactual)
                    else:
                        if line1.find("Yo Agente OMEGA. Mi calidad:",0,len(line1))>0 and line1.find("mensajes. Devuelvo el mensaje=",0,len(line1))>0 or line1.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0, len(line1))>0:    
                            c =line1.find("nro:") + 5
                            m = int(line1[c:c+2])                    
                            c=line1.find("calidad:") + 9 
                            g=line111.find(". Me") -1 
                            if line111.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0,len(line111))>0 :
                                g=line111.find(". Calidad llamador") -1 
                            calidadO=float(line111[c:g])               
                            if Qf[m-1]==-1:
                                N[int(calidadO*10),k-1]=N[int(calidadO*10),k-1]+1
                                QQ[m-1,k-1]=calidadO 
                                Qf[m-1]= calidadO
                                
                                
                            if  line1.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0,len(line1))>0:
                               
                                Qi[m-1]= calidadO
                                
                       #     print("iter ",k, " mensaje ",m,"calidad final ", calidadO)
                     #   EOI=0        
        else:
            EOF =1 
                
    f.close()
    EOF=0
    f= open(arch, 'r', encoding='ascii', errors='ignore')
   
    k=1  
               
    while k < 33 and EOF==0:
        EOI=0
        while EOF == 0 and EOI == 0:
            line1=f.readline()
            line111=line1.strip()     
        #    print(line111)
        #    print(line111[1:50],len(line111))
            if line1 == ""  :
                EOI=1
                EOF=1
                continue        
                                    
            if line111.find("FIN DE LA",0,len(line111))>0 :
                EOI=1
                continue
            if  (line1.find("Registro", 0, len(line1))>0 and (len(line111) < 40 )) :
           #     print("es registro***",line111, len(line111))
                c =line111.find("Registro") + 9
                g=line111.find(":") 
                m = int(line111[c:g])
                c =line111.find(":",0,len(line111)) + 1
                g=line111.find("mensajes",0,len(line111)) 
                if g < 0:
                    if line111.find(': 0',0,len(line111)) < 0:
                        g=line111.find("mensaje",0,len(line111))
                    else:
                        g = c+2                       
                if len(line111) > 30:
                    aux = 0
                    T[m-1, k-1]=aux
                else:
                    aux = int(line111[c:g])
                    T[m-1, k-1]=aux
        #      print('mensaje',m,'mens usados',line111[c:g], 'c',c,'g',g)

        for j in range(1,32):
            aux= int(QQ[j-1, k-1]*10)
            TC[aux, k-1]=T[j-1,k-1]+TC[aux, k-1]                         
       
        k=k+1
      

    
    R.write("****************************************************************\n")   
    R.write("  \n") 
    res="Archivo:" + arch+"\n"
    R.write(res)
    R.write("  \n") 
    R.write("****************************************************************\n")
    R.write("  \n") 

    R.close()                
#************************************************************************************************************************
def main():
    import io
    # -*- coding: Windows-1252 -*-
    import codecs
    import numpy    
    
    #*************************************************
    # archivo con la lista de logs a procesar
    #
    lista='pepe.txt'
    #
    #*************************************************
    # El archivo de salida es  RESULTADOS CALIDAD
    #
    
    
    import datetime
    now = datetime.datetime.now() 
    s1=str(now)
    s1=s1.replace(':','-')
    s1=s1[1:16]
    s="RESULTADOS CALIDAD "+s1
    R=open(s,'w')
    R.write(" ")
    R.close    
    l = open(lista, 'r', encoding='ascii', errors='ignore')
    EOF=0
    TC=numpy.zeros((11,32), dtype=int)
    T=numpy.zeros((32,32), dtype=int)
    N=numpy.zeros((11,32),  dtype=int)
    TOT_TC=numpy.zeros((11,32), dtype=int)
    TOT_TC_SIMPLE=numpy.zeros((11,32), dtype=int)
    TOT_N=numpy.zeros((11,32), dtype=int)
    TOT_N_SIMPLE=numpy.zeros((11,32), dtype=int)
      
     
    while not EOF==1:
        line1=l.readline()
        line111=line1.strip()
     #   print(line111)
        if line1=="":
            EOF =1
            continue
        if not ".txt" in line111 or lista in line111 :
            continue
    
        c=line111.find(".txt")+4
        arch=line111[39:c]
        TC.fill(0)
        N.fill(0)
        T.fill(0) 
        
        print(" ")
        
        print("Procesando  :", arch)
        ERR =0
        analizador(arch, s, TC, N, T, ERR)
        
        
        R= open(s,'a')
        R.write("\n" )
        if ERR ==0:
            
       
        #  R.write("================================================== \n")
            R.write("\n" )
            R.write(arch+"***** TOTAL DE MENSAJES USADOS POR CALIDAD E ITERACION   ***** \n")
               # print(TOTINTELIG)
            R.write("\n ")
            for j in range (0,11):
                res="Calidad = "+str(j/10)+" \n "
                R.write(res)
                for i in range(0,32):
                    R.write(str(TC[j,i])+" ")
                    if "SIMPLE" in arch:
                        TOT_TC_SIMPLE[j,i]=TOT_TC_SIMPLE[j,i]+TC[j,i]
                    else:
                        TOT_TC[j,i]=TOT_TC[j,i]+TC[j,i]
                R.write("\n ")
            R.write("Para Excel===== \n")
            for j in range(0,11):
                res=arch +" ***** Calidad = "+str(j/10)+" ***** \n "
                R.write(res)        
                for i in range(0,32):
                    res=str(TC[j,i])+"\n"
                    R.write(res)
                    
            R.write("\n ")    
            R.write(arch+"***** TOTALES DE VECES QUE SE DIO UNA CALIDAD POR ITERACION  *****   \n")
            R.write("\n ")
            for j in range (0,11):
                    res="Calidad = "+str(j/10)+" \n "
                    R.write(res)
                    for i in range(0,32):
                        R.write(str(N[j,i])+" " ) 
                        if "SIMPLE" in arch:
                            TOT_N_SIMPLE[j,i]=TOT_N_SIMPLE[j,i]+N[j,i]
                        else:
                            TOT_N[j,i]=TOT_N[j,i]+N[j,i]                        
                    R.write("\n ")
            R.write("Para Excel===== \n")
            for j in range(0,11):
                res=arch + " ***** Calidad = "+str(j/10)+" ***** \n "
                R.write(res)        
                for i in range(0,32):
                    res=str(N[j,i])+"\n"
                    R.write(res)
                
            R.write("\n ")
            R.write("\n ")
            R.write("======================================================== \n")    
            R.close()
            
    R=open(s,'a')
    R.write("\n ***************************************************************************************** \n")   
    R.write("***** TOTAL DE MENSAJES USADOS POR CALIDAD PARA TODOS LOS ARCHIVOS  POR ITERACION ***** \n")
        # print(TOTINTELIG)
    R.write("\n   *** INTELIGENTE *** \n")
    for j in range (0,11):
        res="Calidad = "+str(j/10)+" \n "
        R.write(res)
        for i in range (0,32):
            R.write(str(TOT_TC[j,i])+" ")
        R.write("\n ")
        R.write("Calidad = "+str(j/10)+" para Excel===== \n")
        for i in range (0,32):
            R.write(str(TOT_TC[j,i])+"\n ")
    R.write("\n") 
    R.write("\n   *** SIMPLE *** \n")
    for j in range (0,11):
        res="Calidad = "+str(j/10)+" \n "
        for i in range (0,32):
            R.write(str(TOT_TC_SIMPLE[j,i])+" ")
        R.write("\n ")
        R.write("Calidad = "+str(j/10)+" para Excel===== \n")
        for i in range (0,32):
            R.write(str(TOT_TC_SIMPLE[j,i])+"\n ")
    R.write("\n") 
    R.write("\n")    
        
                    




    R.write("***** TOTAL DE VECES QUE SE DIO UNA CALIDAD PARA TODOS LOS ARCHIVOS   ***** \n")
            # print(TOTINTELIG)
    R.write("\n   *** INTELIGENTE *** \n")
    for j in range (0,11):
        res="Calidad = "+str(j/10)+" \n "
        R.write(res)
        for i in range (0,32):
            R.write(str(TOT_N[j,i])+" ")
        R.write("\n ")
        R.write("Calidad = "+str(j/10)+" para Excel===== \n")
        for i in range (0,32):
            R.write(str(TOT_N[j,i])+"\n ")
    R.write("\n") 
    R.write("\n   *** SIMPLE *** \n")
    for j in range (0,11):
        res="Calidad = "+str(j/10)+" \n "
        for i in range (0,32):
            R.write(str(TOT_N_SIMPLE[j,i])+" ")
        R.write("\n ")
        R.write("Calidad = "+str(j/10)+" para Excel===== \n")
        for i in range (0,32):
            R.write(str(TOT_N_SIMPLE[j,i])+"\n ")
    R.write("\n") 
    R.write("\n") 
    R.write("\n \n")    
                              
                                
    R.write("***** MENSAJES PROMEDIOS POR CALIDAD PARA TODOS LOS ARCHIVOS   ***** \n")
                        # print(TOTINTELIG)
    R.write("\n   *** INTELIGENTE *** \n")
    for j in range (0,11):
        res="Calidad = "+str(j/10)+" \n "
        R.write(res)
        for i in range (0,32):
            if TOT_N[j,i] > 0:
                R.write(str(TOT_TC[j,i]/TOT_N[j,i])+" ")
            else:
                R.write(" -- ")
        R.write("\n ")
        R.write("Calidad = "+str(j/10)+" para Excel===== \n")
        for i in range (0,32):
            if TOT_N[j,i] > 0:
                R.write(str(TOT_TC[j,i]/TOT_N[j,i])+"\n ")
            else:
                R.write(" \n ")
    R.write("\n") 
    R.write("\n   *** SIMPLE *** \n")
    for j in range (0,11):
        res="Calidad = "+str(j/10)+" \n "
        for i in range (0,32):
            if TOT_N_SIMPLE[j,i] > 0:
                R.write(str(TOT_TC_SIMPLE[j,i]/TOT_N_SIMPLE[j,i])+" ")
            else:
                R.write(" -- ")
        R.write("\n ")
        R.write("Calidad = "+str(j/10)+" para Excel===== \n")
        for i in range (0,32):
            if TOT_N_SIMPLE[j,i] > 0:
                R.write(str(TOT_TC_SIMPLE[j,i]/TOT_N_SIMPLE[j,i])+"\n ")
            else:
                R.write(" \n ")
                
    R.write("\n") 
    R.write("\n") 
    R.write("\n ***********************************************************************************  ")    
                                
                                                                      
    l.close()
    print("*** FIN ***")
   
      
#******************************************************************************************************


      
#----------------------------------------------
main() 
#----------------------------------------------