#*******************************************************************************************************

#*****************************************************************************************

def analizador (archivo, TOTSIMPLE, TOTINTELIG, NROSAG, TOTSIMPLEAG, TOTINTELIGAG, TOTSIMPLEMENS, TOTINTELIGMENS,NROSMENS,ESTRICTOS_I,ESTRICTOS_S,T_I,T_S,nroarchivo):
    import datetime
    now = datetime.datetime.now()
    s1=str(now.year)+str(now.month)+str(now.date)   
  #  print(s)
    import numpy
    import io
    # -*- coding: Windows-1252 -*-
    import codecs
    
    
    arch=archivo
    nroag=int(arch[0:arch.find("ag")-1])
    nroag=NROSAG.index(nroag)
    c=arch.find("ag")+2
    g=arch.find("mens")-1
    nromens=int(arch[c:g])
    nromens=NROSMENS.index(nromens)
    
  
   # print(s)
   
    #***********************************************************
    s="RESULTADOS EXITOS"
    try: 
        f= open(arch, 'r', encoding='ascii', errors='ignore')
       
        R= open(s,'a')
    except:
        print("***** ARCHIVO INEXISTENTE *****" )
        return
    
    #***********************************************************
    ESTRICTOS=0
    e=0
    AMPLIOS = 0
    calidadactual = 0.0
    i=0
    Qi= []
    Qf=[]
    line1 = "  "
    line111="  "
    IT=0
    EOF=0
    k=0
        
    line1= "   "
    line111= "    "
    EOF=0
    EOI=0
    Qi=numpy.zeros(32, dtype=float) 
    Qf=numpy.zeros(32, dtype=float) 
    k=1
    
     
    while k < 33  and EOF==0:
        e=0
        if EOF == 0:
            for kk in range(0,32):
                Qi[kk]=0
                Qf[kk]=0
            
      #      cuentoexitos(ESTRICTOS, AMPLIOS, Qi, Qf, nroag, k, arch, EOF, TOTINTELIGAG, TOTSIMPLEAG) 
            # cuenta la cantidad de exitos en UNA iteracion (las anotaciones entre un COMIENZO DE ITERACION y FIN DE ITERACION)
            #   print("entre a cuentoexitos")
            line111 = "  "
            line1=  "  "
            EOI=0
            i=0
            
            a=AMPLIOS
            while not  (line111.find("INICIANDO",0,len(line1))>0):
                line1=f.readline()
                line111=line1.strip() 
                  #
                  #print(line1)
                if len(line1)==0:
                    cuenta=0
                    while  (len(line1) ==0) and cuenta < 100:
                        line1=f.readline()
                        line111=line1.strip()
                        if line111.find("INICIANDO",0,len(line1))>0:
                            e=0
                            break
                        cuenta=cuenta+1
                    else:
                        EOF=1
                        EOI=1
                   #     print("*******EOF******")
                        return
            
            while  EOF == 0 and EOI == 0 and len(line1)>0:
                line1=f.readline()
                line111=line1.strip() 
                if len(line1)==0:
                    cuenta=0
                    while len(line1) ==0 and cuenta < 100:
                        line1=f.readline()
                        line111=line1.strip()
                        cuenta=cuenta+1
                    else:
                        if len(line1) == 0:
                            EOF=1
                            EOI=1
                  #          print("*******EOF******")
                            break          
                 
                if EOF == 0:   
                    if line1.find("FIN DE LA",0,len(line1))>0 :
                        EOI=1
                        continue            
                                   
                    if line1.find(" Yo Agente OMEGA tengo mensajes para responder. Mi nivel: 1. Mi calidad: ",0,len(line1))>0:                                                                                          
                     #   print("suksdns2")
                        c =line111.find("nro:") + 5
                        m = int(line111[c:c+2])
                        c=line111.find("calidad:")+9
                        g=line111.find(". Calidad llamador:") -1 
                        calidadactual=float(line111[c:g])  
                        if Qi[m-1] == 0:
                            Qi[m-1]=calidadactual
                          #  print("iter ",k, " mensaje ",m," calidad actual",calidadactual)
                    else:
                        if line1.find("Yo Agente OMEGA. Mi calidad:",0,len(line1))>0 and line1.find("mensajes. Devuelvo el mensaje=",0,len(line1))>0 or line1.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0, len(line1))>0:    
                            c =line1.find("nro:") + 5
                            m = int(line1[c:c+2])                    
                            c=line1.find("calidad:") + 9 
                            g=line111.find(". Me") -1 
                            if line111.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0,len(line111))>0 :
                                g=line111.find(". Calidad llamador") -1 
                            calidadO=float(line111[c:g])
                            
                            if Qf[m-1]==0:
                                Qf[m-1]= calidadO
                            if  line1.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0,len(line1))>0:
                                Qi[m-1]= calidadO
                                
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
                        if not len(line111) > 30:
            
                            aux = int(line111[c:g])
                            if not "SIMPLE" in arch:
                                T_I[nroarchivo,k-1]=aux +  T_I[nroarchivo,k-1]  
                            else:
                                T_S[nroarchivo,k-1]=aux +  T_S[nroarchivo,k-1]
                          #  print("iter ",k, " mensaje ",m,"calidad final ", calidadO)
           # print("calculo exitos")  
            # i varia sobre ls mensajes
            for i in range(1,33) :
                if Qf[i-1] > Qi[i-1] :
              #      print("calidades-----", i-1,  Qf[i-1], Qi[i-1])
                    e=e+1
                    a=a+1 
                    
                    if "SIMPLE" in arch:
                        TOTSIMPLEAG[nroag,k-1]=TOTSIMPLEAG[nroag,k-1] + 1
                        TOTSIMPLEMENS[nromens,k-1]=TOTSIMPLEMENS[nromens,k-1] + 1
                        
                 #       print("SIMPLE -- agentes ",  nroag,"iteracion ", k,"TOT ",  str(TOTSIMPLEAG[nroag,k-1]), "mens nro ", i )
                    else:
                        TOTINTELIGMENS[nromens,k-1]=TOTINTELIGMENS[nromens,k-1] + 1
                        TOTINTELIGAG[nroag,k-1]=TOTINTELIGAG[nroag,k-1] + 1
                 #       print("INTELIG -- agentes ",  nroag,"iteracion ", k-1,"TOT ", TOTINTELIGAG[nroag, k-1], "mens nro ", i )
                else :
                    if Qf[i-1] == Qi[i-1] and Qf[i-1]> 0:
                        a=a+1    
                        
        ESTRICTOS=e+ESTRICTOS
         #   AMPLIOS=a            
        k=k+1
        e=0
    
    R.write("****************************************************************\n")   
    R.write("  \n") 
    s="Archivo:" + arch+"\n"
    R.write(s)
    R.write("  \n") 
    if "SIMPLE" not in arch:

        ESTRICTOS_I[nroarchivo]=ESTRICTOS
    else:
    
        ESTRICTOS_S[nroarchivo]=ESTRICTOS
    
    s=" ESTRICTOS = "+ str(ESTRICTOS) + " AMPLIOS = " + str(AMPLIOS) +"\n"
    R.write (s)
    R.write("  \n") 
    R.write("***************************************************************\n")
    R.write("  \n") 

                    
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
    # El archivo de salida es  RESULTADOS exitos
    #
    s="RESULTADOS EXITOS"
    R=open(s,'w')
    R.close    
    l = open(lista, 'r', encoding='ascii', errors='ignore')
    EOF=0
    TOTSIMPLE=numpy.zeros((11,32), dtype=int)
    ESTRICTOS_I=numpy.zeros((120,32), dtype=int)
    ESTRICTOS_S=numpy.zeros((120,32), dtype=int)
    T_I=numpy.zeros((120,32), dtype=int)
    T_S=numpy.zeros((120,32), dtype=int)
    E=numpy.zeros(120, dtype=int)
    t=numpy.zeros(120, dtype=int)
    T=numpy.zeros(32, dtype=int)
    TOTINTELIG=numpy.zeros((11,32),  dtype=int)
    TOTSIMPLEAG=numpy.zeros((11,32), dtype=int)
    TOTINTELIGAG=numpy.zeros((11,32),  dtype=int) 
    TOTSIMPLEMENS=numpy.zeros((11,32), dtype=int)
    TOTINTELIGMENS=numpy.zeros((11,32),  dtype=int)    
    NROSAG=numpy.zeros(11,  dtype=int)  
    NROMENS=numpy.zeros(11,  dtype=int)  
    NROSAG=[5,10,15,20,30,100,300,600,0,0,0]
    NROSMENS=[5,10,15,20,30,100,1000,0,0,0,0]
    ARCHIVO=numpy.empty(120, dtype='S50')
    nroarchivo=0
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
        print(" ")
        print("Procesando  :", arch)
        T.fill(0)
        ARCHIVO[nroarchivo]=arch
        
        analizador(arch, TOTSIMPLE, TOTINTELIG, NROSAG, TOTSIMPLEAG, TOTINTELIGAG,TOTSIMPLEMENS, TOTINTELIGMENS, NROSMENS,ESTRICTOS_I,ESTRICTOS_S,T_I,T_S,nroarchivo)
        
        nroarchivo=nroarchivo+1
    R.close()
    R=open(s,'a')
    R.write("\n" )
  
    
    
    R.write("\n" )
    R.write("\n" )
    R.write(" ================================================== \n")
    R.write("\n" )
    R.write(" TOTALES DE EXITOS ESTRICTOS POR AGENTES PARA INTELIGENTE     \n")
       # print(TOTINTELIG)
    R.write("\n ")
    for j in range (0,11):
        if NROSAG[j] > 0:
            res=str(TOTINTELIGAG[j])+"\n"
            R.write(res)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSAG[j] > 0:
            res="INTELIG -- NRO. DE AGs: "+str(NROSAG[j])+"\n"
            R.write(res)
            for k in range(0,32):
                res=str(TOTINTELIGAG[j,k])+"\n"
                R.write(res)
    R.write("\n ")    
    R.write("TOTALES DE EXITOS ESTRICTOS POR AGENTES PARA SIMPLE       \n")
    R.write("\n ")
    for j in range (0,11):
        if NROSAG[j] > 0:
            res=str(TOTSIMPLEAG[j])+"\n"
            R.write(res)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSAG[j] > 0:
            res="SIMPLE -- NRO. DE AGs: "+str(NROSAG[j])+"\n"
            R.write(res)
            for k in range(0,32):
                res=str(TOTSIMPLEAG[j,k])+"\n"
                R.write(res)
    R.write("\n ")
    R.write("\n ")
    R.write("======================================================== \n")  
    
    R.write(" ================================================== \n")
    R.write("\n" )
    R.write(" TOTALES DE EXITOS ESTRICTOS POR MENSAJES PARA INTELIGENTE     \n")
       # print(TOTINTELIG)
    R.write("\n ")
    for j in range (0,11):
        if NROSMENS[j] > 0:
            res=str(TOTINTELIGMENS[j])+"\n"
            R.write(res)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSMENS[j] > 0:
            res="INTELIG -- NRO. DE MENS: "+str(NROSMENS[j])+"\n"
            R.write(res)
            for k in range(0,32):
                res=str(TOTINTELIGMENS[j,k])+"\n"
                R.write(res)
    R.write("\n ")    
    R.write("TOTALES DE EXITOS ESTRICTOS POR MENSAJES PARA SIMPLE       \n")
    R.write("\n ")
    for j in range (0,11):
        if NROSMENS[j] > 0:
            res=str(TOTSIMPLEMENS[j])+"\n"
            R.write(res)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSMENS[j] > 0:
            res="SIMPLE -- NRO. DE MENS: "+str(NROSMENS[j])+"\n"
            R.write(res)
            for k in range(0,32):
                res=str(TOTSIMPLEMENS[j,k])+"\n"
                R.write(res)
    R.write("\n ")
    R.write("\n ")
    R.write("======================================================== \n")   
    
    R.write(" ======================================================= \n")
    R.write("\n" )
    R.write(" PROMEDIOS DE MENSAJES POR EXITO PARA INTELIGENTE     \n")
       # print(TOTINTELIG)
    R.write("\n ")
    for p in range (0,120):
        E[p]=0
        t[p]=0
        for j in range(0,32):
            E[p]=E[p]+ESTRICTOS_I[p,j]
            t[p]=T_I[p,j]+t[p]
    for j in range (0,120):
        res1=str(ARCHIVO[j])
        if res1.find("SIMPLE",0,len(res1))<0:
                if t[j] > 0:
                    res="ARCHIVO "+res1+" Promedio: "+str(E[j]/t[j])+"\n"
                    R.write(res)
                    
                else:
                    res="-- \n"
                    R.write(res)            
    R.write("Para Excel===== \n")
    for j in range (0,120):
        res1=str(ARCHIVO[j])
        if not "SIMPLE" in res1:    
            if t[j] > 0:
                res=str(E[j]/t[j])+"\n"
                
                R.write(res)
                
            else:
                res="-- \n"
                R.write(res)   
                
    R.write("\n ")    
    R.write("PROMEDIOS DE MENSAJES POR EXITO PARA SIMPLE       \n")
    R.write("\n ")
  
    for p in range (0,120):
        E[p]=0
        t[p]=0
        for j in range(0,32):
            E[p]=E[p]+ESTRICTOS_S[p,j]
            t[p]=T_S[p,j]+t[p]
    for j in range (0,120):
        res1=str(ARCHIVO[j])
        if  "SIMPLE" in res1:
                if t[j] > 0:
                    res="ARCHIVO "+res1+" Promedio: "+str(E[j]/t[j])+"\n"
                    R.write(res)
                   
                else:
                    res="-- \n"
                    R.write(res)            
    R.write("Para Excel===== \n")
    for j in range (0,120):
        res1=str(ARCHIVO[j])
        if  "SIMPLE" in res1:    
            if t[j] > 0:
                res=str(E[j]/t[j])+"\n"
                R.write(res)
               
            else:
                res="--"
                R.write(res)   
        
    R.write("\n ")
    R.write("\n ")
    R.write("======================================================== \n")  
    
    R.close()
    l.close()
    print("*** FIN ***")
   
      
#******************************************************************************************************


      
#----------------------------------------------
main() 

    
#----------------------------------------------