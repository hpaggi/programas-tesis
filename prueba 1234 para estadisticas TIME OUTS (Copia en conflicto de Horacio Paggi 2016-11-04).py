#*******************************************************************************************************

#*****************************************************************************************

def analizador (sal, archivo, T_O_SIMPLE, T_O_INTELIG, T_O_S, T_O_I, NROSAG):
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
  
    try: 
        f= open(arch, 'r', encoding='ascii', errors='ignore')
        R= open(sal,'a')
    except:
        print("HUKNOINIOPNJIOPHOPINOIJ")
        return
    
    #***********************************************************
   
    line1 = "  "
    line111="  "
   
    EOF=0
    k=0
        
    line1= "   "
    line111= "    "
    EOF=0
    EOI=0
    
    k=1
    T_O=0
     
    while k < 33  and EOF==0:
        if EOF == 0:
            line111 = "  "
            line1=  "  "
            EOI=1
            i=0
      
            while not  (line111.find("INICIANDO",0,len(line1))>0):
                line1=f.readline()
                line111=line1.strip() 
                  #
                print(line1)
                if len(line1)==0:
                    cuenta=0
                    while  (len(line1) ==0) and cuenta < 100:
                        line1=f.readline()
                        line111=line1.strip()
                        print(line111)
                        if line111.find("INICIANDO",0,len(line1))>0:
                            EOI=0
                            break
                        cuenta=cuenta+1
                    else:
                        if line111.find("INICIANDO",0,len(line1))>0:
                            EOI=0
                            break
                        EOF=1
                        EOI=1
                        print("*******EOF******")
                        return
            
            while  EOF == 0 and EOI == 0 and len(line1)>0:
                line1=f.readline()
                line111=line1.strip() 
                print(line111)
                if len(line1)==0:
                    cuenta=0
                    while len(line1) ==0 and cuenta < 100:
                        line1=f.readline()
                        line111=line1.strip()
                        print(line111)
                        cuenta=cuenta+1
                    else:
                        if len(line1) == 0:
                            EOF=1
                            EOI=1
                           # print("*******EOF******")
                            break          
                 
                if EOF == 0:   
                    if line1.find("FIN DE LA",0,len(line1))>0 :
                        EOI=1
                        continue            
                                   
                    if line1.find(" SERVICO",0,len(line1))>0:
                        T_O=T_O+1
                        if "SIMPLE" in arch:
                            T_O_SIMPLE[nroag,k-1]=T_O_SIMPLE[nroag,k-1] +1


                        else:
                            T_O_INTELIG[nroag,k-1]=T_O_INTELIG[nroag,k-1] +1
       
    for i in range(1,33) :
         T_O_S[nroag]=T_O_S[nroag]+T_O_SIMPLE[nroag,i-1]
         T_O_I[nroag]=T_O_INTELIG[nroag,i-1] + T_O_I[nroag]    
                      
    print(" KHOILJPOK PO KPOJKPK KKOK")  
    
    R.write("****************************************************************\n")   
    R.write("  \n") 
    s="Archivo:" + arch+"\n"
    R.write(s)
    R.write("  \n") 
    s="TIME OUTS:  "+str(T_O)+" \n"
    R.write(s)
    s="MODO INTELIGENTE  \n"
    R.write(s)    
    for i in range (1,33):
        s="ITERACION "+str(i)+ str(T_O_INTELIG[nroag,i-1])   +"\n" 
        R.write(s)
    s="PARA EXCEL ================== \n"
    R.write(s)     
    R.write("  \n") 
    for i in range (1,33):
        s=str(T_O_INTELIG[nroag,i-1])   +"\n" 
        R.write(s)
    s="MODO SIMPLE  \n"
    R.write(s)
    
    
    for i in range (1,33):
        s="ITERACION "+str(i)+ str(T_O_SIMPLE[nroag,i-1])   +"\n" 
        R.write(s)
    s="PARA EXCEL ================== \n"
    R.write(s)     
    R.write("  \n") 
    for i in range (1,33):
        s=str(T_O_SIMPLE[nroag,i-1])   +"\n"
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
    lista='pepe para estadisticas.txt'
    #
    #*************************************************
    # El archivo de salida es  _____RESULTADOS____
    #
    s="RESULTADOS TIME_OUTS"
    R=open(s,'w')
    R.write("   \n")
    R.close    
    l = open(lista, 'r', encoding='ascii', errors='ignore')
    EOF=0
    T_O_SIMPLE=numpy.zeros((11,32), dtype=int) 
    T_O_INTELIG=numpy.zeros((11,32), dtype=int) 
    T_O_S=numpy.zeros(11, dtype=int) 
    T_O_I=numpy.zeros(11, dtype=int)  
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
        analizador(s,arch, T_O_SIMPLE, T_O_INTELIG,T_O_S, T_O_I, NROSAG)
    
    R=open(s,'a')
    R.write("\n" )
  
    
    
    R.write("\n" )
    R.write("\n" )
    R.write(" ================================================== \n")
    R.write("\n" )
    R.write(" TOTALES DE time outs PARA INTELIGENTE     \n")
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
    R.write("TOTALES DE time outs ESTRICTOS PARA SIMPLE       \n")
    R.write("\n ")
    s="NRO. DE AGS = "+str(NROSAG[j])+"  T.O.= "+str(T_O_S[j])+"\n"
    R.write(s)
    R.write("\n ")
    R.write("Para Excel===== \n")
    for j in range(0,11):
        if NROSAG[j] > 0:
            s="INTELIG -- NRO. DE AGs: "+str(NROSAG[j])+"\n"
            R.write(s)
            for k in range(0,32):
                s=str(T_O_SIMPLE[j,k])+"\n"
                R.write(s)
    R.write("\n ")   
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