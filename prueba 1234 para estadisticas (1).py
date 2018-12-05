def analizador (archivo, TOTSIMPLE, TOTINTELIG, NROSAG, TOTSIMPLEAG, TOTINTELIGAG):
    import datetime
    now = datetime.datetime.now()
    s=str(now.year)+str(now.month)+str(now.date)   
  #  print(s)
    import numpy
    import io
    # -*- coding: Windows-1252 -*-
    import codecs
    
    
    arch=archivo
    nroag=int(arch[0:arch.find("ag")-1])
    nroag=NROSAG.index(nroag)
  
   # print(s)
   
    #***********************************************************
    s="RESULTADOS"
    try: 
        f= open(arch, 'r', encoding='ascii', errors='ignore')
        R= open(s,'a')
    except:
        return
    
    #***********************************************************
    ESTRICTOS=0
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
    
    T_O=0
    while not(line1 == ""):
        line1=f.readline()
        line111=line1.strip()
       # print(line111)
        if "SERVICO NO LLEG A ESPERAR" in line111:
            T_O=T_O+1
    g=f.close()  
    f= open(arch, 'r', encoding='ascii', errors='ignore')
    
    
    line1= "   "
    line111= "    "
    EOF=0
    EOI=0
    while not (line1.find("INICIANDO",0,len(line1))>0)   :
        line1=f.readline()
        line111=line1.strip()    
    for k in range(1,33): 
        EOI=0
        i=0
        Qi=[]
        Qf=[]
        for i in range(1,33): 
            Qi.append(0.00)  
            Qf.append(0.00)    
    
        while  EOF== 0 and EOI == 0 :
            if  line1.find("INICIANDO",0,len(line1))>0   :
                IT=IT+1
                line1=f.readline()
                line111=line1.strip()
            #    print("espero",line111)
    
            if line1.find("FIN DE LA",0,len(line1))>0 :
                EOF=1
                EOI=1
                continue            
    
            if EOI == 1 :
                continue
    
            if line1.find(" Yo Agente OMEGA tengo mensajes para responder. Mi nivel: 1. Mi calidad: ",0,len(line1))>0:                                                                                          
              #  print("suksdns2")
                c =line111.find("nro:") + 5
                m = int(line111[c:c+2])
                c=line111.find("calidad:")+9
                g=line111.find(". Calidad llamador:") -1 
                calidadactual=float(line111[c:g])  
    
            #   print("calidad actual",calidadactual)
                if  Qi[m-1] == 0.0 :
                    Qi[m-1]=calidadactual
    
            else:
                if line1.find("Yo Agente OMEGA. Mi calidad:",0,len(line1))>0 and line1.find("mensajes. Devuelvo el mensaje=",0,len(line1))>0 or line1.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0, len(line1))>0:    
                    c =line1.find("nro:") + 5
                    m = int(line1[c:c+2])                    
                    c=line1.find("calidad:") + 9 
                    g=line111.find(". Me") -1 
                    if line111.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0,len(line111))>0 :
                        g=line111.find(". Calidad llamador") -1 
    
                    calidadO=float(line111[c:g])               
                    if  Qf[m-1] == 0.0 :
                        Qf[m-1]= calidadO
                    if  line1.find("Yo Agente OMEGA no tengo mensajes para responder. Mi nivel: 1. Mi calidad:",0,len(line1))>0:
                        if  Qi[m-1] == 0.0 :
                            Qi[m-1]= calidadO 
                           
            line1=f.readline()   
            line111=line1.strip()
        #    print (line111)
            if line111 == "" :
                i=0
                while line111 == "" and i < 100:
                    line1=f.readline()   
                    line111=line1.strip()
                    i=i+1
            if i==100 :
                EOF=1
    
                continue
            if line111.find("ITERACIN",0,len(line111))>0  and line111.find("INICIO",0,len(line111))>0 :
                c=line111.find("ITERACIN") + 9  
                nro=int(line111[c:c+1]) 
                IT=nro
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
                if "SIMPLE" in arch:
                    TOTSIMPLEAG[nroag,IT]=TOTSIMPLEAG[nroag,IT] + 1
                    print("SIMPLE -- agentes ",  nroag,"iteracion ", IT,"TOT ",  str(TOTSIMPLEAG[nroag,k]), "mens ", i )
                else:
                    TOTINTELIGAG[nroag,IT]=TOTINTELIGAG[nroag,IT] + 1
                    print("INTELIG -- agentes ",  nroag,"iteracion ", IT,"TOT ", TOTINTELIGAG[nroag, IT], "mens", i )
            else :
                if Qf[i-1] == Qi[i-1] and Qf[i-1]> 0:
                    AMPLIOS = AMPLIOS +1
    R.write("****************************************************************\n")   
    
    
    s="Archivo:" + arch+"\n"
    R.write(s)
    R.write("***************************************************************\n")
    s=" ESTRICTOS = "+ str(ESTRICTOS) + " AMPLIOS = " + str(AMPLIOS) +"\n"
    R.write (s)
    R.write("  \n")
    s=" TIME OUTS =  " + str(T_O)+"\n"
    R.write(s)
    R.write("   \n")
    f.close()
    
    import numpy
    
    f= open(arch, 'r', encoding='ascii', errors='ignore')
    
    i=0
    
    line1 = "  "
    line111="  "
    IT=0
    EOF=0
    k=0
    
    #*************************************************
    CM=numpy.zeros((32,32), dtype=int) # cantidad de mensajes que quedan luego de responder al mens nro x en la iteracion y
    
    QQ=numpy.zeros((32,32), dtype=float) # calidad con que se respondio al mensaje nro x en la iteracion y
    
    T=numpy.zeros((32,32), dtype=int) # cantidad de mensajes usados pra responder el mensaje nro x en la iteracion y
    
    TC=numpy.zeros((32,32), dtype=int) #Total de mensajes usados para la calidad x en la iteracion y 
    P=numpy.zeros((11,32), dtype=float) # promedio de mensajes usados para la calidad x en la iteracion y
    N=numpy.zeros((11,32), dtype=int) # cantidad de veces que se respondio con la calidad x en la iteracion y
    
    PP=numpy.zeros(11, dtype=float) # promedio de promedios de mensajes usados para la calidad x en todas las iteraciones
    NN=numpy.zeros(11, dtype=int) # cantidad de veces que se respondio con la calidad x en  todas las iteraciones
  #  TOTSIMPLE=numpy(11, dtype=int)
  #  TOTINTELIG=numpy(11, dtype=int)
     
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
        #while posicion: 
            #line1=f.readline()
            #line111=line1.strip()  
            #print(line111)
            #if line1 == ""  and not( k < 32 ) :
                #EOF=1
                #posicion = False
                #break
            #else:
                ## print(line111)
                #if not line1 == "" :
        for line1 in f :
            line111=line1.strip() 
            if line1.find(ITERACION, 0, len(line1))>0:
                        posicion = False
                        break
            continue
        if posicion :
            EOF = 1
        
        if EOF == 1:
            continue
    
        EOI=0
        while EOF == 0 and EOI == 0:
            line1=f.readline()
            line111=line1.strip()    
      #      print(line111)
            if line1 == "" and not( k < 32 ) :
                EOI=1
                EOF=1
                continue
            if line111.find("FIN DE LA EJECUCIN", 0, len(line111)) > 0:
                EOI=1
                continue
            if line1.find(" Yo Agente OMEGA. Mi calidad:", 0, len(line1)) > 0 and line1.find("mensajes. Devuelvo el mensaje= ", 0, len(line1)) >0 :
                c =line111.find("nro:") + 5
                m = int(line111[c:c+2])
                c=line111.find("calidad:") + 9 
                g=line111.find(". Me")-1
                calidadO =float(line111[c:g] )             
                QQ[m-1,k-1]=calidadO
                N[int(calidadO*10),k-1]=N[int(calidadO*10),k-1]+1
                if "SIMPLE" in arch:
                    
                    TOTSIMPLE[int(calidadO*10),k-1]=TOTSIMPLE[int(calidadO*10), k-1]+1
                else:
                    TOTINTELIG[int(calidadO*10), k-1]=TOTINTELIG[int(calidadO*10), k-1]+1
    
                
                
         #       print ("calidad O es",calidadO,"NN es", N[int(calidadO*10),k-1], "K es", k)
                continue
            else:
                continue
            #     print ('mensaje', m,  QQ[m-1,k-1])
        EOI=0
        k= k+1
            
            
    f.close()
    EOF=0
    EOI=0
    f= open(arch, 'r', encoding='ascii', errors='ignore')
    EOI=0
    k=1  
    for j in range(0,11):
        PP[j-1]=0
        NN[j-1]=0     
    
    while k < 33 and EOF==0:
        EOI=0
        while EOF == 0 and EOI == 0:
            line1=f.readline()
            line111=line1.strip()                    
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
    
        for j in range(1,33):
            aux= int(QQ[j-1, k-1]*10)
            TC[aux, k-1]=T[j-1,k-1]+TC[aux, k-1]
        #  print('reg',j,'iterac',k,'indice calidad',aux,'mens usados para ese reg',T[j-1,k-1],'total mens para cal.',TC[aux, k-1]) 
        # print('reg',j, 'aux',aux, N[aux,k-1])
        #    print ("TC[aux]",TC[aux],"T",T[j-1,k-1])
     
        k=k+1    

    
    k=1
    
    while k < 33 :       
        for j in range(1,12) :
            for k in range (1,33):
                if N[j-1,k-1] > 0:
                    P[j-1,k-1]=TC[j-1, k-1]/N[j-1,k-1]
        
                else:
                   # P[j-1,k-1]=TC[j-1, k-1]
                    P[j-1,k-1]=0
            for k in range (1,33):
                PP[j-1]= P[j-1,k-1]+ PP[j-1]
                if P[j-1,k-1] > 0 :
                    NN[j-1]= 1 + NN[j-1]
         #       print("PP[j-1]",'j-1', j,PP[j-1],"NN[j-1]",NN[j-1])
                      
            if NN[j-1]>0:
                PP[j-1]=PP[j-1]/NN[j-1]
            else:
                PP[j-1]=0
        #    print(j-1, N[j-1])
                
        k=k+1
  
        
    #************************************************
    R.write ("PROMEDIOS DE MENSAJES POR CALIDAD   \n")
    num=0
    for j in range (0,11):
        s="Calidad : "+ str(j/10)+" promedio : "+str(PP[j])+"\n"
        num=num+NN[j]
        R.write (s)
    R.write("  \n")
    R.write("Para Excel:  \n")
    R.write("   \n")
    aux1 = 0.0
    
    for j in range (0,11):
        s=str(PP[j])+"\n"
        R.write(s)
    R.write("   \n")
  #  print("num",num)
    R.write("FRECUENCIAS DE CADA CALIDAD  \n")    
    for j in range (1,12):    
        if num > 0:
            aux1=(NN[j-1]*100/num)
  #          print("NN",NN[j-1],"j-1",j-1, "PP", PP[j-1])
        else:
            aux1=0
        s=str(aux1)+"  \n"         
        R.write(s)
    
# **************************************************************************************

def main():
    import io
    # -*- coding: Windows-1252 -*-
    import codecs
    import numpy    
    
    #*************************************************
    # archivo con la lista de logs a procesar
    #
    lista='pepe para estadisticas.txt'
    #
    #*************************************************
    # El archivo de salida es  _____RESULTADOS____
    #
    s="RESULTADOS"
    R=open(s,'w')
    R.close    
    l = open(lista, 'r', encoding='ascii', errors='ignore')
    EOF=0
    TOTSIMPLE=numpy.zeros((11,32), dtype=int)
    TOTINTELIG=numpy.zeros((11,32),  dtype=int)
    TOTSIMPLEAG=numpy.zeros((11,32), dtype=int)
    TOTINTELIGAG=numpy.zeros((11,32),  dtype=int)    
    NROSAG=numpy.zeros(11,  dtype=int)  
    NROSAG=[5,10,15,20,30,100,0,0,0,0,0]
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
        arch=line111[41:c]
        print(" ")
        print("Procesando  :", arch)
        analizador(arch, TOTSIMPLE, TOTINTELIG, NROSAG, TOTSIMPLEAG, TOTINTELIGAG)
    R.close()
    R=open(s,'a')
    R.write("\n" )
    R.write("\n" )
    R.write(" ************************************************** \n")
    R.write("\n" )
    R.write(" TOTALES DE MENSAJES PARA INTELIGENTE     \n")
       # print(TOTINTELIG)
    R.write("\n ")
    for j in range (0,11):
        res=str(TOTINTELIG[j])+"\n"
        R.write(res)
        R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        res="INTELIG -- Calidad ="+str(j)+"\n"
        R.write(res)
        for k in range(0,32):
            res=str(TOTINTELIG[j,k])+"\n"
            R.write(res)
    R.write("\n ")    
    R.write("TOTALES DE MENSAJES PARA SIMPLE       \n")
    R.write("\n ")
    for j in range (0,11):
        res=str(TOTSIMPLE[j])+"\n"
        R.write(res)
    R.write("\n")
    R.write("Para Excel===== \n")
    for j in range (0,11):
        res="SIMPLE -- Calidad ="+str(j)+"\n"
        R.write(res)
        for k in range(0,32):
            res=str(TOTSIMPLE[j,k])+"\n"
            R.write(res)
    R.write("\n ")
    R.write("*************************************************** \n")
    
    
    R.write("\n" )
    R.write("\n" )
    R.write(" ================================================== \n")
    R.write("\n" )
    R.write(" TOTALES DE EXITOS ESTRICTOS PARA INTELIGENTE     \n")
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
    R.write("TOTALES DE EXITOS ESTRICTOS PARA SIMPLE       \n")
    R.write("\n ")
    for j in range (0,11):
        if NROSAG[j] > 0:
            res=str(TOTSIMPLEAG[j])+"\n"
            R.write(res)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSAG[j] > 0:
            res="INTELIG -- NRO. DE AGs: "+str(NROSAG[j])+"\n"
            R.write(res)
            for k in range(0,32):
                res=str(TOTSIMPLEAG[j,k])+"\n"
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