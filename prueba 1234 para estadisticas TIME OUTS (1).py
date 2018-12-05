#*******************************************************************************************************

#*****************************************************************************************

def analizador (sal, archivo, T_O_SIMPLE, T_O_INTELIG,T_O_SIMPLE_MENS, T_O_INTELIG_MENS, T_O_S, T_O_I, T_O_S_MENS, T_O_I_MENS ,NROSAG, NROSMENS, ERR):
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
  
    try: 
        f= open(arch, 'r', encoding='ascii', errors='ignore')
        R= open(sal,'a')
    except:
        print("*** ARCHIVO INEXISTENTE ****")
        ERR=ERR+1
        return
    
    #***********************************************************
   
    line1 = "  "
    line111="  "
   
    EOF=0
    k=0
        
    line1= "   "
    line111= "    "
    EOF=0
    k=1
    T_O=0
    T_O_A=numpy.zeros(32, dtype=int)
    mens=numpy.zeros(34, dtype=int)
    line111 = "  "
    line1=  "  "
    EOI=1
    i=0    
    while k < 33  and EOF==0:
        while  EOF==0:
            line1=f.readline()
            line111=line1.strip()
            if len(line1)==0:
                EOF=1
                break                
            if line111.find("INICIANDO",0,len(line1))>0:
                EOI=0
                mens.fill(0)
                break            
        if EOF==1:
            break
                  
        while  EOI == 0:
            o=1
            line1=f.readline()
            line111=line1.strip() 
            
            if len(line1)==1: 
                continue         
            if len(line1)==0:
                EOF=1
                EOI=1
                k=k+1
                break          
                        
            if line111.find("FIN DE LA",0,len(line111))>0 :
                EOI=1
                k=k+1
                continue            
                           
            if line111.find(" SERVICO",0,len(line111))>0:
                while not ("@@@ Duracin entre entrada y salida de mensaje" in line111):
                    line1=f.readline()
                    line111=line1.strip()                     
                if "@@@ Duracin entre entrada y salida de mensaje" in line111:
                    try:  
                        c =line1.find("mero") + 4
                        g=line111.find(":")  
                        m=int(line111[c:g])
              #      print("m",m)
                    except:
                        continue
                    
                    if mens[m]==0 :
                        T_O=T_O+1
                        T_O_A[k-1]=T_O_A[k-1]+1
                        if "SIMPLE" in arch:
                            T_O_SIMPLE[nroag,k-1]=T_O_SIMPLE[nroag,k-1] +1
                            T_O_S[nroag]=T_O_S[nroag]+1
                            T_O_SIMPLE_MENS[nromens,k-1]=T_O_SIMPLE_MENS[nromens,k-1] +1
                            T_O_S_MENS[nromens]=T_O_S_MENS[nromens]+1                            
                            
                        else:
                            T_O_INTELIG[nroag,k-1]=T_O_INTELIG[nroag,k-1] +1
                            T_O_I[nroag]= 1 + T_O_I[nroag] 
                            T_O_INTELIG_MENS[nromens,k-1]=T_O_INTELIG_MENS[nromens,k-1] +1
                            T_O_I_MENS[nromens]= 1 + T_O_I_MENS[nromens]                            
                    if mens[m]==0:
                        mens[m]=1                        
                
    R.write("****************************************************************\n")   
    R.write("  \n") 
    s="Archivo:" + arch+"\n"
    R.write(s)
    R.write("  \n") 
    s="TIME OUTS:  "+str(T_O)+" \n"
    R.write(s)
    if not ("SIMPLE"in arch):
        s="MODO INTELIGENTE  \n"
        R.write(s)    
        for i in range (1,33):
            s="ITERACION: "+str(i)+" T.O.= " +str(T_O_A[i-1])   +"\n" 
            R.write(s)
        s="PARA EXCEL ================== \n"
        R.write(s)     
        R.write("  \n") 
        for i in range (1,33):
            s=str(T_O_A[i-1])   +"\n" 
            R.write(s)
    if ("SIMPLE"in arch):
        s="MODO SIMPLE  \n"
        R.write(s)
        
        
        for i in range (1,33):
            s="ITERACION :"+str(i)+" T.O.= " +str(T_O_A[i-1])   +"\n" 
            R.write(s)
        s="PARA EXCEL ================== \n"
        R.write(s)     
        R.write("  \n") 
        for i in range (1,33):
            s=str(T_O_A[i-1])   +"\n"
            R.write(s)    
    R.write("***************************************************************\n")
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
    # El archivo de salida es  RESULTADOS TIME_OUTS xxxxxx
    #
    import datetime
   
    now = datetime.datetime.now() 
    s1=str(now)
    s1=s1.replace(':','-')
    s1=s1[1:16]
    s="RESULTADOS TIME_OUTS "+s1
    R=open(s,'w')
    R.write(" ")
    R.close     
    
    l = open(lista, 'r', encoding='ascii', errors='ignore')
    EOF=0
    T_O_SIMPLE=numpy.zeros((11,32), dtype=int) 
    T_O_INTELIG=numpy.zeros((11,32), dtype=int) 
    T_O_SIMPLE_MENS=numpy.zeros((11,32), dtype=int) 
    T_O_INTELIG_MENS=numpy.zeros((11,32), dtype=int)     
    T_O_S=numpy.zeros(11, dtype=int) 
    T_O_I=numpy.zeros(11, dtype=int)  
    T_O_S_MENS=numpy.zeros(11, dtype=int) 
    T_O_I_MENS=numpy.zeros(11, dtype=int)      
    
    NROSAG=[5,10,15,20,30,100,300,600,0,0,0]
    NROSMENS=[5,10,15,20,30,100,1000,0,0,0,0]
    ERR=0
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
        analizador(s,arch, T_O_SIMPLE, T_O_INTELIG,T_O_SIMPLE_MENS, T_O_INTELIG_MENS,T_O_S, T_O_I,T_O_S_MENS, T_O_I_MENS, NROSAG, NROSMENS, ERR)
    
    R=open(s,'a')
    R.write("\n" )
  
    
    
    R.write("\n" )
    R.write("\n" )
    R.write(" ================================================== \n")
    R.write("\n" )
    
    R.write(" TOTALES DE time outs POR AGENTES PARA INTELIGENTE     \n")
       # print(TOTINTELIG)
    R.write("\n ")
    for j in range (0,11):
        if NROSAG[j] > 0:
            s="NRO. DE AGs = "+str(NROSAG[j])+"  T.O.=   "+str(T_O_I[j])+"\n"
            R.write(s)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSAG[j] > 0:
            s="INTELIG -- NRO. DE AGs: "+str(NROSAG[j])+"\n"
            R.write(s)
            for k in range(0,32):
                s=str(T_O_INTELIG[j,k])+"\n"
                R.write(s)
    
    R.write("\n ")
    R.write("TOTALES DE time outs POR AGENTES  PARA SIMPLE       \n")
    R.write("\n ")
    for j in range (0,11):
        if NROSAG[j] > 0:    
            s="NRO. DE AGS = "+str(NROSAG[j])+"  T.O.= "+str(T_O_S[j])+"\n"
            R.write(s)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSAG[j] > 0:
            s="SIMPLE -- NRO. DE AGs: "+str(NROSAG[j])+"\n"
            R.write(s)
            for k in range(0,32):
                s=str(T_O_SIMPLE[j,k])+"\n"
                R.write(s)
    R.write("\n ")
    R.write(" ================================================== \n")
    R.write("\n" )
    
    R.write(" TOTALES DE time outs POR MENSAJES PARA INTELIGENTE     \n")
       # print(TOTINTELIG)
    R.write("\n ")
    for j in range (0,11):
        if NROSMENS[j] > 0:
            s="NRO. DE AGs = "+str(NROSMENS[j])+"  T.O.=   "+str(T_O_I_MENS[j])+"\n"
            R.write(s)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSMENS[j] > 0:
            s="INTELIG -- NRO. DE AGs: "+str(NROSMENS[j])+"\n"
            R.write(s)
            for k in range(0,32):
                s=str(T_O_INTELIG_MENS[j,k])+"\n"
                R.write(s)
    
    R.write("\n ")
    R.write("TOTALES DE time outs POR MENSAJES  PARA SIMPLE       \n")
    R.write("\n ")
    for j in range (0,11):
        if NROSMENS[j] > 0:    
            s="NRO. DE MENS = "+str(NROSMENS[j])+"  T.O.= "+str(T_O_S_MENS[j])+"\n"
            R.write(s)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSAG[j] > 0:
            s="SIMPLE -- NRO. DE MENS: "+str(NROSMENS[j])+"\n"
            R.write(s)
            for k in range(0,32):
                s=str(T_O_SIMPLE[j,k])+"\n"
                R.write(s)
    R.write("\n ")       
    R.write("\n ")
   
    R.write("\n ")
    R.write("======================================================== \n")  
    R.write("======================================================== \n")
    R.write("\n" )
    
    R.write(" TOTALES DE time outs POR MENSAJES PARA INTELIGENTE     \n")
       # print(TOTINTELIG)
    R.write("\n ")
    for j in range (0,11):
        if NROSMENS[j] > 0:
            s="NRO. DE MENS = "+str(NROSMENS[j])+"  T.O.=   "+str(T_O_I[j])+"\n"
            R.write(s)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSMENS[j] > 0:
            s="INTELIG -- NRO. DE MENS: "+str(NROSMENS[j])+"\n"
            R.write(s)
            for k in range(0,32):
                s=str(T_O_INTELIG_MENS[j,k])+"\n"
                R.write(s)
    
    R.write("\n ")
    R.write("TOTALES DE time outs POR MENSAJES  PARA SIMPLE       \n")
    R.write("\n ")
    for j in range (0,11):
        if NROSMENS[j] > 0:    
            s="NRO. DE MENS = "+str(NROSMENS[j])+"  T.O.= "+str(T_O_S_MENS[j])+"\n"
            R.write(s)
            R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSMENS[j] > 0:
            s="SIMPLE -- NRO. DE MENS: "+str(NROSMENS[j])+"\n"
            R.write(s)
            for k in range(0,32):
                s=str(T_O_SIMPLE_MENS[j,k])+"\n"
                R.write(s)
    if ERR == 0:
        R.write("**** NO HUBO ERRORES ****")
        print("**** NO HUBO ERRORES ****")
    else:
        R.write("***** ERRORES : "+str(ERR))
        print("***** ERRORES : "+str(ERR))
    
    R.write("\n ")       
    R.close()
    l.close()
    print("*** FIN ***")
       
      
#******************************************************************************************************


      
#----------------------------------------------
main() 

    
#----------------------------------------------