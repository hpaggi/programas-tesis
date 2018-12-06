# principal del simulador
  
def CONSULTAR(X,Y,id_campo, id_msg, nivel,Qx1,Qy,pendientes, N_campos, restantes):
  import random
  import numpy
# el agente X consulta al Y por el campo id_campo

  global t_entrada
  global muchos
  global largo_cola
  global t
  global tipo_mens
  global N_agentes
  global formado_por
  global Qx
  
  global niveles     
  global N_favoritos
  global SALTO   # el salto que da t para pasar al futuro
  SALTO=999
  
  rr="Estoy en CONSULTAR  campo "+" X "+str(X)+" Y "+str(Y)+" MSg " + str(id_msg) +" campo "+str(id_campo) + " nivel " +str(nivel)+ " Qx1"+str(Qx1)
  rr=rr+"\n"
 
  print(rr)
  #Resp.write(rr)  
  if restantes[X]>0 and MODO == "I" or MODO=="S":
      lista_subcampos=[]
      ccons=numpy.zeros(N_campos, dtype=int)
      if (X,Y,id_msg,id_campo) not in S:
        S[X,Y,id_msg,id_campo] = 0
      S[X,Y,id_msg,id_campo]=S[X,Y,id_msg,id_campo]+1
      
      print("S es",str( S[X,Y,id_msg,id_campo]), "X es ", str(X), "Y es ",str(Y))
      if (Y,id_msg,id_campo) not in   largo_cola:
        largo_cola[Y,id_msg,id_campo] = 1
      else:   
        largo_cola[Y,id_msg,id_campo]=largo_cola[Y,id_msg,id_campo]+1
     
      
      # nro de campos por los que consulto ************************************************************
      ncons=0
      
      # veo los subcampos que hay
      tot=0
      lista_subcampos=[]
      if restantes[Y] >0  and MODO == "I" or MODO=="S":
        for i in range (1,N_campos):
          if formado_por[id_campo,i]== 1:
            lista_subcampos.append(i)
            tot=tot+1
                   
          # ***********************************************************************************************
        aleat= random.random()*tot
        ncons=int(aleat)
        k=0
        Z=0
          # si no tiene subcampos tot esta en 0 y ncons=0. Si no tiene subcampos asumo que Y no consulta.
        if ncons> 0 and not X == Y:
              
            kk=0
            for k in range(0,ncons):
              s=random.random()
              if (X,Y,id_msg,k) in Qx:
                prob=Qx[X,Y,id_msg,k]
              else:
                prob=0.5
              if s > prob : 
                # aniadir k a la lista de campos a consultar
                     
                if lista_subcampos[k] not in ccons:
                  ccons[kk]=lista_subcampos[k]
                  kk=kk+1
                  if not (Y,id_msg,id_campo) in pendientes:
                    pendientes[Y,id_msg,id_campo]=0
                  pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo] + 1   
                  
                  
                  
          # generar estructuras de que X consulta a Y +++++++++++++++++++++
          #
          #
            espera=int(random.random()*100)
            tipo_mens[X,Y,id_msg,id_campo,t+espera]=1
            t_generac[X,Y,id_msg,id_campo,t+espera]=t
            t_entrada[X,Y,id_msg,id_campo, t]= t+espera
            f=id_campo
            if (Y, id_msg,f ) in largo_cola:
              largo_cola[Y, id_msg, f]= largo_cola[Y, id_msg, f] +1
            else:
              largo_cola[X, id_msg, ccons[k]]= 1
            niveles[X, Y,id_msg, ccons[k]]=nivel
            restantes[X]=restantes[X]-1  
            print("genere la consulta X Y")      
            # Y consulta a otro por subcampo
            fav=0
            print(" Y  consulta a Z. campos a consultar  ",ccons[0:20])
            #    rr="campos a consultar  "+str(ccons[0:20])+"\n"
            #    Resp.write(rr)
                # ncons dice hasta cuantos campos consulto, kk dice cuantos subcampos consulto realmente
            if kk>0: 
                   #   print("voy a ver subcampos")
                      k=0
                      while k < kk:
                        if restantes[Y] > 0  and MODO == "I" or MODO=="S":
                          favor=[]
                          p=1
                                               
                          favor=arma_lista_fav(Y,ccons[k],favor,N_favoritos,N_agentes)
                          print("fav  para Y ******",Y, "campo",ccons[k],"  ", favor)
                          print("EXITOS FAV PARA ", Y, "=" )
                        #  for x in range (1, N_agentes):
                        #  print(FAVORITOS[Y,x ,ccons[k]], " ");
                          rr="fav *****"+str(favor[0:10])+"\n"
                #          Resp.write(rr)
                          
                          p=1
                  
                          while  p < len(favor):  # en realidad habria que distinguir su ya se determinaron los favoritos y sino usar muchos como fin de loop
                            Z= favor[p-1]
                            Qz=0.0 # ojo. poner 0.0 a todas las calidades como valor inicial
                            if restantes[Y]>0  and MODO == "I" or MODO=="S":
                                if not Z == X:
                                  nivel=nivel+1
                                  niveles[Y,Z,id_msg, ccons[k]]=nivel
                                  if not (X,Y,id_msg, ccons[k]) in S:
                                    S[X,Y,id_msg, ccons[k]] = 1
                                    largo_cola[Y, id_msg, ccons[k]] = 1
                                  else:
                                    S[X,Y,id_msg, ccons[k]] = S[X,Y,id_msg, ccons[k]] +1
                                    
                                  largo_cola[Y, id_msg, ccons[k]]=largo_cola[Y, id_msg, ccons[k]]+1
                                 # S[Y,id_msg, ccons[k]] = S[Y,id_msg, ccons[k]] +1 
                                  
                                  Qx[Y,Z,id_msg, ccons[k]]=niveles[Y,Z,id_msg, ccons[k]]/(1+H[Y,ccons[k]])*(1/ niveles[Y,Z,id_msg, ccons[k]])**(PESO_NIVEL + 1)  # +++++ en realidad seria la calidad propia de Y para ese campo ++++++
                                  
                                  
                                  rr="Genero consulta de Y =" +str(Y)+"a Z ="+str(Z)+ " msg "+str(id_msg)+ " campo  "+ str(ccons[k]) + " cola  "+str(largo_cola[Y, id_msg, ccons[k]])+"Qx"+str(Qx[Y,Z,id_msg,ccons[k]])+"\n"
                            
                                  espera=int(random.random()*100) + espera
                                  
                                  tipo_mens[X,Y,id_msg,id_campo,t+espera]=1
                                  t_generac[X,Y,id_msg,id_campo,t+espera]=t
                                  t_entrada[X,Y,id_msg,id_campo, t]= t+espera
                                  f=ccons[k]
                                  if (Z, id_msg,f ) in largo_cola:
                                    largo_cola[Z, id_msg, ccons[k]]= largo_cola[Z, id_msg, ccons[k]] +1
                                  else:
                                    largo_cola[Z, id_msg, ccons[k]]= 1
                                  niveles[Y, Z,id_msg, ccons[k]]=nivel
                                  restantes[Y]=restantes[Y]-1
                            p=p+1
                        k=k+1         
            else:
            #      print("no hay subcampos. Contesto")
                  
                  # calcular Q propia usando nivel, error, etc
                  #n=niveles[X,Y,id_msg,id_campo]
               #   CALCULO_Qy_SIMPLE(Y, id_msg, id_campo, Qy)
                  Qy=1/(1+H[Y,id_campo])
                  Qx[X,Y,id_msg,id_campo]=Qy
                  if Qy > Qx1 and restantes[Y]>0  and MODO == "I" or MODO=="S":
                   Qy=devuelvo_resp(Y,X,id_msg,id_campo,nivel,Qy)
                 #   print("devuelvo respuesta ",Y,X,id_msg,id_campo,str(nivel),str(Qy))
                   rr="devuelvo respuesta "+"Y "+ str(Y)+"X "+str(X)+" msg "+str(id_msg)+"campo "+str(id_campo)+ "nivel "+str(nivel)+" Qy "+str(Qy)+"\n"    
                   # Resp.write(rr)   
                  
        else:          
              # calcular Qy usando nivel, error, etc 
              # CALCULO_Qy(X,Y,id_msg,id_campo,Qy)
            #  Qyy=1
            #  CALCULO_Qy_SIMPLE(Y,id_msg,id_campo,Qyy)
            #  Qy=Qyy
                Qy=1/(1+H[Y,id_campo])
                Qx[X,Y,id_msg,id_campo]=Qy
                #  +++++++
                if not Y == X:
                  nivel=nivel+ 1
                
        if Qy > Qx1 and restantes[Y]>0  and MODO == "I" or MODO=="S":
          # devolver respuesta // poner en la cola de mens de entrada de Y un mens de resp con hora 100 mas que t
       #        print("VOY A devuelvo respuesta ",Y,X,id_msg,id_campo,str(nivel),str(Qy))
         # print("voy a devolver resp Qy",Qy)
          Qy=devuelvo_resp(Y,X,id_msg,id_campo,nivel,Qy)
          Qx[X,Y,id_msg,id_campo]=Qy # tomo la calidad y no me fijo si es un T O 
          print  ("devuelvo resp por ncons =0", "X",X,"Y",Y,"campo",id_campo,"Qy",Qy)
          rr="devuelvo respuesta "+str(Y)+str(X)+str(id_msg)+str(id_campo)+str(nivel)+str(Qy)+"\n"        
       #  Resp.write(rr)
  else: 
    return(Qy)
              
  return(Qy)

#************************************************************************************

def CALCULO_Qy(X,Y,id_msg,id_campo,Qy):
  import numpy
  
  # calidad  de Y cuando X responde a Y
  # Max=numpy.amax(Q,axis=1)
  Max=0
  Min=0
  global EXITOS_E
  global EXITOS_A
  global TIMEOUTS
    
  for i in range (1, N_agentes):
 #  print(niveles)
    if (i,Y,id_msg,id_campo) in niveles:
      pass
    else:
      niveles[i,Y,id_msg,id_campo]=1
    if (i,Y,id_msg,id_campo) not in Q:  
      Q[i,Y,id_msg,id_campo]=0
    if Q[i,Y,id_msg,id_campo]/(niveles[i,Y,id_msg,id_campo]**PESO_NIVEL) > Max:
      
      Max= Q[i,Y,id_msg,id_campo]/(niveles[i,Y,id_msg,id_campo]**PESO_NIVEL)
 # print("calculo Q. cal max recibida=",Max)
  
  for i in range (1, N_agentes):
    if Q[i,Y,id_msg,id_campo]/(niveles[i,Y,id_msg,id_campo]**PESO_NIVEL) < Min:
      Min = Q[i,Y,id_msg,id_campo]/(niveles[i,Y,id_msg,id_campo]**PESO_NIVEL)     
      
  #print("calculo Q. cal MIN recibida=",Min)
  #n=niveles[X,Y,id_msg,id_campo]
  #Qx[X,Y,id_msg,id_campo]=1/(1+H[Y,id_campo])*(1/n**PESO_NIVEL) 
  #Qx[X,Y,id_msg,id_campo]= CALCULO_Qy(X, id_msg, id_campo, Qx1) # hay que calcular la calidad de X recursivamente
  V=Max-Min
  q=1/(1+V)*Max
  if X== 1:
    S[X,Y,id_msg,id_campo]=1  
  if (Y,X,id_msg,id_campo) not in T:
    T[Y,X,id_msg,id_campo]=1
  R=T[Y,X,id_msg,id_campo]**2/S[X,Y,id_msg,id_campo]
  
  Qtecho=1/(1+H[Y,id_campo])
  if R==0:
  #  n=niveles[X,Y,id_msg,id_campo]
    Qy=1/(1+H[Y,id_campo])
    Qx[X,Y,id_msg,id_campo]=Qy
    
    Q[X,Y,id_msg,id_campo]=Qy
    
    return(Qy)
  Qy=max(Qtecho,q)**((PESO_NIVEL+1)/R)
  Q[X,Y,id_msg,id_campo]=Qy
# cuando el que recibe es OMEGA ya calculo si es un exito  
  if Y == 1 :
    if T[Y,X,id_msg,id_campo]==0:  #X responde a Y o sea Y consulta a X
      TIMEOUTS=TIMEOUTS+1
    else:  
      if (X,Y,id_msg,id_campo) not in Qx:
        Qx[X,Y,id_msg,id_campo]=0
      if Qy > Qx[X,Y,id_msg,id_campo]:
        ES_EXITO_E=1
      #EXITOS_E=EXITOS_E+1
      else:
        if Qy == Qx[X,Y,id_msg,id_campo]:
          ES_EXITO_A=1
        # EXITOS_A=EXITOS_A+1      
 # print("Calculo Qy="+str(Qy)+ " id msg "+" msg "+str(id_msg)+ " id campo " + str(id_campo))
  return(Qy)
#************************************************************************************
def CALCULO_Qy_SIMPLE(Y,id_msg,id_campo,Qy):
  import numpy
  
  # calidad  de Y cuando Y NO CONSULTA A NADIE MAS
  
  # Max=numpy.amax(Q,axis=1)
 
  global EXITOS_E
  global EXITOS_A
  
  
  global TIMEOUTS
        
  print("calculo Q. cal simple")
  
  # n=niveles[X,Y,id_msg,id_campo]
  
  Qy=1/(1+H[Y,id_campo])
  Qx[X,Y,id_msg,id_campo]=Qy 
  Q[X,Y,id_msg,id_campo]=Qy
#  print("Calculo Qy  SIMPLE ="+str(Qy)+ " id msg "+str(id_msg)+ " id campo " + str(id_campo))
  return(Qy)
#****************************************************************************************************************************************

def BUSCOPADRES(Y, id_msg, id_campo, lista): # Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
  global tipo_mens
  lista=[]
  if Y==1:
    lista=lista.append(1)
   # print ("busco padres de OMEGA")
    return
  for ag in range (1,N_agentes):
    if ((ag,Y,id_msg,id_campo) in   tipo_mens) and tipo_mens[ag,Y,id_msg,id_campo]=="1":
      lista.append(ag)
  print("Busco padres"+ "Y"+ str(Y)+" msg" +str(id_msg)+ " campo "+str(id_campo)+"lista:")
  print(lista)
  return(lista)
#*************************************************************************************


def devuelvo_resp(X,Y,id_msg,id_campo,nivel,Qy):
  # X devuelve respuesta a Y
    import random
    lista=[]
    global SALTO
    global Resp
    global RESPONDE_OMEGA
    global respuestas
    global MODO
    global RESTANTES_ANT_REG
    global iteracion
  #  print("estoy en devuelvo resp  X="+str(X)+" Y= " +str(Y)+" id_campo "+str(id_campo))
    espera=int(100*random.random())
    if restantes[X]>0  and MODO == "I" or MODO=="S":
        if espera < SALTO:
          SALTO=espera    
        t_entrada[X, Y, id_msg, id_campo,t]= t +  espera
        t_generac[X, Y, id_msg, id_campo, t+espera]= t 
      
        tipo_mens[X,Y, id_msg, id_campo,t+espera]=2
        if not (Y, id_msg, id_campo) in largo_cola:
          largo_cola[Y, id_msg, id_campo]=0
        largo_cola[Y, id_msg, id_campo]= largo_cola[Y, id_msg, id_campo] +1
        niveles[X,Y,id_msg, id_campo]=nivel+1
      
        Q[X,Y,id_msg, id_campo]=Qx[X,Y,id_msg, id_campo]=Qy   # la respuesta de la cons de X a Y es Qx   
        pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo] - 1
        
        restantes[X]=restantes[X]-1
        
        if pendientes[Y,id_msg,id_campo] < 1 or ES_TO(Y,id_msg,id_campo):
          
          # Y debe devolver la respuesta a quien lo consulto
          #  Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres
          lista=[]
          lista=BUSCOPADRES(Y,id_msg,id_campo, lista)
          #   genera una respuesta a partir de todas las calidades recibidas    Esa respuesta es Qy1
    
          # Tomo todos los pesos iguales, asi que solo hago el promedio de calidades de las respuestas
          Qy1=0
          cuenta=0
          for i in range (1,N_agentes):
            if (i,Y,id_msg,id_campo) in Q:
              if Q[i,Y,id_msg,id_campo] > 0:
                Qy1=Q[i,Y,id_msg,id_campo] + Qy1
                cuenta=cuenta+1
          if cuenta == 0:
            Qy1=0
          else:
            Qy1=Qy1/cuenta
          Q[X,Y,id_msg,id_campo]=Qy1
          suma=0
          for i in range (0,N_agentes):
            suma=suma+restantes[i]      
          if Y == 1:
            TABLA_CALIDADES_FREC[iteracion,int(Qy1*100)]=TABLA_CALIDADES_FREC[iteracion,int(Qy1*100)]+1
            TABLA_CALIDADES_MENS[iteracion,int(Qy1*100)]=  RESTANTES_ANT_REG -suma
            RESTANTES_ANT_REG= suma     
            print(TABLA_CALIDADES_MENS[iteracion,int(Qy1*100)])
            
         #   print(TABLA_CALIDADES[iteracion,int(Qy1*100)], Qy1)
          print("devuelvo resp promedio a los padres",Qy1)
         
       
          # Qy1=0.967890         
          # genera un mensaje para cada padre de Respuesta
          
          
          RESPONDE_OMEGA=0 
          if Y == 1:
           
            RESPUESTA_OMEGA (1,1,id_msg,decision,Qx,Qy,N_agentes,tipo_mens,MODO, restantes)
            print("**** respuesta de OMEGA al msg ", str(id_msg), "calidad",str(Qy))
            RESPONDE_OMEGA=1
          else:
            RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy1,nivel)
     #   print("Responde "+str(X) + " a " +str (Y)+ " msg "+str(id_msg)+" campo "+str(id_campo)+ " calidad "+ str(Qy))
        rr="Responde "+str(X) + " a " +str (Y)+ " msg "+str(id_msg)+" campo "+str(id_campo)+ " calidad "+ str(Qy)
    #    Resp.write(rr)
    return(Qy)
#************************************************************************************
def ES_TO(Y,id_msg,id_campo):
  
  # ES T O si ninguno de los consultados por Y para id_msg e id_campo contesto
  maxt=0
  for i in range (1,N_agentes):
    for j in range(0,t):
      if  tipo_mens[i,Y,id_msg,id_campo,j] == 2 and t_generac[i,Y,id_msg,id_campo,j] + TIMEOUT > t_entrada[i,Y,id_msg,id_campo, t_generac[i,Y,id_msg,decision,j]] :
        return False
      else:
        if t_generac[i,Y,id_msg,id_campo,j] + TIMEOUT < t_entrada[i,Y,id_msg,id_campo, t_generac[i,Y,id_msg,decision,j]] :
          TO_MSG[i,Y]=TO_MSG[i,Y]+1
  
  return True
  
#***************************************************************************************
def RESPUESTA_OMEGA(X,Y,id_msg,id_campo,Qx,Qy,N_agentes,tipo_mens, MODO, restantes):
 
  global SALTO
  global t_entrada
  global line111
  global TIMEOUTS
  
          # hacer fusion de todas las respuestas
          # LAS respuestas estan en respuestas[]
          
          # Supongo que en respuess[X,X] esta la respuesta propia
          
          # Calcular respuesta propia
  import random
  
  partes = line111.split(';') 
  
  R=partes[72] # en R va la respuesta del juego de datos
           
  aux=random.random()
  if aux>0.95:
    if R == "Yes":
      respuestas[X,Y,id_msg,id_campo]= 1
    else:
      respuestas[X,Y,id_msg,id_campo]= 0
     
  else:
    if R == "Yes":
      # pongo valores cruzados el 5% de las veces
      respuestas[X,Y,id_msg,id_campo]= 0
    else:
      respuestas[X,Y,id_msg,id_campo]= 1
      
  # fusion de los resultados
  aux=0
  p=0
  for j in range(1,N_agentes):
    if (X,j,id_msg,id_campo) in respuestas:
      aux=aux+respuestas[X,j,id_msg,id_campo]
      p=p+1
  aux=int(aux/p)
 
 # CALCULO_Qy(X,Y,id_msg,id_campo,Qy)
  Qy=CALCULO_Qy(1,1,id_msg,id_campo,Qy)

   
  if   (X,Y,id_msg,id_campo) not in Qx:
    Qx[X,Y,id_msg,id_campo]=Qy
  Qx1=Qx[X,Y,id_msg,id_campo]
  Q[X,Y,id_msg,id_campo]=Qx1
  
  # es time out si ningun mensaje llega a omega a tiempo. O sea si el t_entrada mayor + TIMEOUT < t
  ymax=1
  maxt=0
  
  p=1 
  
  for i,p,id_msg,id_campo,j in t_entrada:
    if p==1:
      if  t_entrada [i,1,id_msg,id_campo,j] > maxt and tipo_mens[i,1,id_msg,id_campo,t_entrada [i,1,id_msg,id_campo,j]] == 2:
   #     print(t_entrada,"t es", str(t))
        maxt=t_entrada [i,1,id_msg,id_campo,j]
        ymax= i # que hora le pongo??????+++++++++ ojo, que considero tooodas las horas
    
 # if t_generac[ymax,1,id_msg,decision,maxt] + TIMEOUT < t_entrada[ymax,1,id_msg,decision, t_generac[ymax,1,id_msg,decision,maxt]]:
 #   TIMEOUTS=TIMEOUTS+1
 # else:
 #   FAVORITOS[ymax,1, id_campo]=FAVORITOS[ymax, 1, id_campo]+1
 
  return
#*****************************************************************************************************************************************
def RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy1,nivel):
 # print ("****Respondo a los padres de Y "+str(Y)+ " campo "+ str(id_campo)+" calidad "+ str(Qy1))
  for i in range(0,len(lista)-1):
    
   Qy1=devuelvo_resp(Y,lista[i],id_msg,id_campo,nivel,Qy1)
    
  return
  
  

# ***********************************************************************************
def RESPONDER(X,Y,id_msg,id_campo,Qy,N_agentes,tipo_mens,MODO, restantes,hora):

  # X envia respuesta a Y
  
  global SALTO
  global t_entrada
  import random 
  global Qx
  #for i in range (1,largo_cola[X, id_msg, id_campo]):
  if (X,Y,id_msg,id_campo,hora) in tipo_mens:
      if tipo_mens[X,Y,id_msg,id_campo,hora]==2 and t_entrada [X,Y,id_msg,id_campo,t_generac[Y,X,id_msg,id_campo,hora] ] == hora or tipo_mens[X,Y,id_msg,id_campo,hora]==1 and t_entrada [X,Y,id_msg,id_campo,t_generac[Y,X,id_msg,id_campo,hora] ] > t_generac[Y,X,id_msg,id_campo,hora] + TIMEOUT:
      
  #      if pendientes[X,id_msg,id_campo]== 0:
          # hacer fusion de todas las respuestas
          # LAS respuestas estan en respuestas[]
          
          # Supongo que en respuess[X,X] esta la respuesta propia
          
          # Calcular respuesta propia
                    
          partes = line111.split(';') 
          
          R=partes[72] # en R va la respuesta del juego de datos
              
          aux=random.random()
          if aux>0.95:
            if R == "Yes":
              respuestas[X,Y,id_msg,id_campo]= 1
            else:
              respuestas[X,Y,id_msg,id_campo]= 0
              
          else:
            if R == "Yes":
              # pongo valores cruzados el 5% de las veces
              respuestas[X,Y,id_msg,id_campo]= 0
            else:
              respuestas[X,Y,id_msg,id_campo]= 1
              
          # fusion de los resultados
          
          aux=0
          p=0
          print("RESPONDER  valor de entrADA ",R, " resp ", str(respuestas[X,Y,id_msg,id_campo]))
              
          for j in range(1,N_agentes):
            if (X,j,id_msg,id_campo) in respuestas:
              aux=aux+respuestas[X,j,id_msg,id_campo]
              p=p+1
          aux=round(aux/p)
          
          #s=S[X,id_msg,id_campo]
          #nt=T[Y,X,id_msg,id_campo]
          # Qx1=nivel/(1+0.05)*(1/(nivel **  PESO_NIVEL))
          #Calculo Q  
       
          Qx1= 1/(1+H[X,id_campo])      
          a = restantes [X]
          
          if a > 0   and MODO == "I" or MODO=="S":
            if Qx1 > Qy or MODO == "S" :  # cuando la calidad es mayor que la del que consulta, responde
              espera=int(random.random()*100)
              if espera < SALTO:
                SALTO=espera
                
              
              Qx[X,Y,id_msg,id_campo]=Qx1
              if (Y,X,id_msg, id_campo) in T:
                T[Y,X,id_msg, id_campo]=T[Y,X,id_msg, id_campo]+1
              else:
                T[Y,X,id_msg, id_campo]=1
              t_entrada[X,Y,id_msg,id_campo,t]=t+espera 
              t_generac[X,Y,id_msg,id_campo,t+espera]=t
              tipo_mens[X,Y,id_msg,id_campo,t+espera]=2 
              nivel=niveles[X,Y,id_msg,id_campo]=niveles[X,Y,id_msg,id_campo]+1
              if t_generac[X,Y,id_msg,id_campo,hora] + TIMEOUT > t_entrada[X,Y,id_msg,decision, t_generac[X,Y,id_msg,decision,hora]] : # no es t o
                
                
                largo_cola[Y,id_msg,id_campo]=largo_cola[Y,id_msg,id_campo]-1
                pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo]-1
                FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
              
              else:
                TO_MSG[X,Y]= TO_MSG[X,Y]+1
              if pendientes[Y,id_msg,id_campo] < 1:
                    # Y debe devolver la respuesta a quien lo consulto
                    # a- BUSCOPADRES(Y,id_msg,id_campo, lista) Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres
                    
                lista=[]        
                lista=BUSCOPADRES(Y,id_msg,id_campo, lista)
                if len(lista)==0:
                  lista=[1]                
                # b- genera una respuesta a partir de todas las calidades recibidas ++++
                # X manda resp a Y entonces para calcular calidad de Y deben haber respondido todos o ser time out de la consulta de Y a X
            
                if pendientes[Y,id_msg,id_campo]<1 or TIMEOUT < espera :      
                                                      
        #          print(" voy a calcular Qy compleja")
                  Qy=CALCULO_Qy(X,Y,id_msg,id_campo,Qy)   # OJO CALCULAR QY solo cuando haya pasado el timeout de Y o cuando respondieron todos
         #         print(" Qy compleja es ", Qy)                                
          
                z=0
            #   GENERO_RESP(Y,id_msg,id_campo, lista, Qy)
                for z in lista:
                  if restantes[Y]>0:
                    espera=int(random.random()*100)
                    t_entrada[Y,z,id_msg,id_campo,t]=t+espera
                    t_generac[Y,z,id_msg,id_campo,t+espera]=t
                    tipo_mens[Y,z,id_msg,id_campo,t+espera]=2
                    largo_cola[z,id_msg, id_campo]=largo_cola[z,id_msg, id_campo]-1
                    FAVORITOS[Y,z,id_campo]=FAVORITOS[Y,z,id_campo]+1
                    pendientes[z,id_msg,id_campo]=pendientes[z,id_msg,id_campo]-1   
                    Qx[z,Y,id_msg,id_campo]=Qy
                    Q[z,Y,id_msg,id_campo]=Qy
                    restantes[Y]=restantes[Y-1]                
                # c- genera un mensaje para cada padre de Respuesta ++++ 
                # para cada elem i de lista:
                #    genero mens de resp de Y a i para ese id_msg, id_campo y Qy
                
            #    print("QYYYYY",Qy)
                RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy,nivel)
                
            #    restantes[Y]=restantes[Y]-1
              
              if  t_generac[Y,X,id_msg,id_campo,hora] + TIMEOUT > t_entrada[Y,X,id_msg,id_campo, t_generac[Y,X,id_msg,id_campo,hora]]:
                # actualizar favoritos de Y 
                FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                pass
              else:
                  if Y == 1 :  # T O es cuando el sistema no contesta a tiempo, cuando NADIE contesta a tiempo
                    if max(t_generac[X,1,id_msg,id_campo],axis=0) +TIMEOUT < t:                 
                      TIMEOUTS = TIMEOUTS +1
              
            else:
                if MODO == "I":
                  PTEMPLE=(1-Qy)*(MAXREGS-restantes[X])/100
                  a=random.random()
                  if a > PTEMPLE:
                    if restantes[X]>0  :
                        espera=int(random.random()*100)
                        if espera < SALTO:
                          SALTO=espera
                        if  (Y,X, id_msg, id_campo) in T:
                          T[Y,X, id_msg, id_campo]=T[Y,X,id_msg, id_campo]+1
                        else:
                          T[Y,X,id_msg, id_campo]=1
                        t_entrada[X,Y,id_msg,id_campo,t]=t+espera
                        t_generac[X,Y,id_msg,id_campo,t+espera]=t
                        tipo_mens[X,Y,id_msg,id_campo,t+espera]=2
                        nivel=niveles[X,Y,id_msg,id_campo]=niveles[X,Y,id_msg,id_campo]+1
                        largo_cola[Y,id_msg, id_campo]=largo_cola[Y,id_msg, id_campo]+1
                        FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
                        pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo]-1
                        if pendientes[Y,id_msg,id_campo] < 1:
                              # Y debe devolver la respuesta a quien lo consulto
                              lista=[]
                              lista=BUSCOPADRES(Y,id_msg,id_campo, lista) #Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
                              # b- genera una respuesta a partir de todas las calidades recibidas 
                              # c- genera un mensaje para cada padre de Respuesta 
                              
                              RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy,nivel)
                if t_generac[X,Y,id_msg,id_campo,hora] + TIMEOUT > t_entrada[X,Y,id_msg,id_campo, t_generac[X,Y,id_msg,id_campo,hora]]:
                  
                          # actualizar favoritos de Y
                        FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                        rr="++++++++++++++++++++++++++++++++++respondo   ++++++++++++++++++++++++++++++++++++++  "  
             #       print("+++++++++++++++++++++++++++++++++++++++++++       respondo   ++++++++++++++++++++++++++  ")
             #      Resp.write(rr)
             
      
          
  #      if pendientes[X,id_msg,id_campo]== 0:
          # hacer fusion de todas las respuestas
          # LAS respuestas estan en respuestas[]
          
          # Supongo que en respuess[X,X] esta la respuesta propia
          
          # Calcular respuesta propia
                else:
                  TO_MSG[X,Y]=TO_MSG[X,Y]+1
          partes = line111.split(';') 
          
          R=partes[72] # en R va la respuesta del juego de datos
              
          aux=random.random()
          if aux>0.95:
            if R == "Yes":
              respuestas[X,Y,id_msg,id_campo]= 1
            else:
              respuestas[X,Y,id_msg,id_campo]= 0
              
          else:
            if R == "Yes":
              # pongo valores cruzados el 5% de las veces
              respuestas[X,Y,id_msg,id_campo]= 0
            else:
              respuestas[X,Y,id_msg,id_campo]= 1
              
          # fusion de los resultados
          
          aux=0
          p=0
   #       print("RESPONDER  valor de entrADA ",R, " resp ", str(respuestas[X,Y,id_msg,id_campo]))
              
          for j in range(1,N_agentes):
            if (X,j,id_msg,id_campo) in respuestas:
              aux=aux+respuestas[X,j,id_msg,id_campo]
              p=p+1
          aux=int(aux/p)
          
          #s=S[X,id_msg,id_campo]
          #nt=T[Y,X,id_msg,id_campo]
          # Qx1=nivel/(1+0.05)*(1/(nivel **  PESO_NIVEL))
          #Calculo Q  
       
          Qx1= 1/(1+H[X,id_campo])      
          a = restantes [X]
          
          if a > 0   and MODO == "I" or MODO=="S":
            if Qx1 > Qy or MODO == "S" :  # cuando la calidad es mayor que la del que consulta, responde
              espera=int(random.random()*100)
              if espera < SALTO:
                SALTO=espera
                
              
              Qx[X,Y,id_msg,id_campo]=Qx1
              T[Y,X,id_msg, id_campo]=T[Y,X,id_msg, id_campo]+1
              t_entrada[X,Y,id_msg,id_campo,t]=t+espera 
              t_generac[X,Y,id_msg,id_campo,t+espera]=t
              tipo_mens[X,Y,id_msg,id_campo,t+espera]=2 
              nivel=niveles[X,Y,id_msg,id_campo]=niveles[X,Y,id_msg,id_campo]+1
              if t_generac[X,Y,id_msg,id_campo,hora] + TIMEOUT > t_entrada[X,Y,id_msg,decision, t_generac[X,Y,id_msg,decision,hora]] : # no es t o
                
                
                largo_cola[Y,id_msg,id_campo]=largo_cola[Y,id_msg,id_campo]-1
                pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo]-1
                FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
              
              else:
                TO_MSG[Y,Y]=TO_MSG[Y,Y]+1
              if pendientes[Y,id_msg,id_campo] < 1:
                    # Y debe devolver la respuesta a quien lo consulto
                    # a- BUSCOPADRES(Y,id_msg,id_campo, lista) Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres
                    
                         
                lista=BUSCOPADRES(Y,id_msg,id_campo, lista)
                # b- genera una respuesta a partir de todas las calidades recibidas ++++
                # X manda resp a Y entonces para calcular calidad de Y deben haber respondido todos o ser time out de la consulta de Y a X
            
                if pendientes[Y,id_msg,id_campo]<1 or TIMEOUT < espera :      
                                                      
        #          print(" voy a calcular Qy compleja")
                  Qy=CALCULO_Qy(X,Y,id_msg,id_campo,Qy)   # OJO CALCULAR QY solo cuando haya pasado el timeout de Y o cuando respondieron todos
         #         print(" Qy compleja es ", Qy)                                
                
         #       GENERO_RESP(Y,id_msg,id_campo, lista, Qy)
                for z in lista: 
                  if restantes[Y]>0:
                    espera=int(random.random()*100)
                    t_entrada[Y,z,id_msg,id_campo,t]=t+espera
                    t_generac[Y,z,id_msg,id_campo,t+espera]=t
                    tipo_mens[Y,z,id_msg,id_campo,t+espera]=2
                    largo_cola[z,id_msg, id_campo]=largo_cola[z,id_msg, id_campo]-1
                    FAVORITOS[Y,z,id_campo]=FAVORITOS[Y,z,id_campo]+1
                    pendientes[z,id_msg,id_campo]=pendientes[z,id_msg,id_campo]-1   
                    Qx[z,Y,id_msg,id_campo]=Qy
                    Q[z,Y,id_msg,id_campo]=Qy
                    restantes[Y]=restantes[Y-1]
                  
                
                # c- genera un mensaje para cada padre de Respuesta ++++ 
                # para cada elem i de lista:
                #    genero mens de resp de Y a i para ese id_msg, id_campo y Qy
                
                print("RESPONDO OADRES DE Y con q ",Qy)
                RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy,nivel)
                
            #    restantes[Y]=restantes[Y]-1
              
              if  t_generac[Y,X,id_msg,id_campo,hora] + TIMEOUT > t_entrada[Y,X,id_msg,id_campo, t_generac[Y,X,id_msg,id_campo,hora]]:
                # actualizar favoritos de Y 
                FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                pass
              else:
                  if Y == 1 :  # T O es cuando el sistema no contesta a tiempo, cuando NADIE contesta a tiempo
                    if max(t_generac[X,1,id_msg,id_campo],axis=0) +TIMEOUT < t:                 
                      TIMEOUTS = TIMEOUTS +1
                      TO_MSG[X,1]=TO_MSG[X,1]+1 
            else:
                if MODO == "I":
                  PTEMPLE=(1-Qy)*(MAXREGS-restantes[X])/100
                  a=random.random()
                  if a > PTEMPLE:
                    if restantes[X]>0  :
                        espera=int(random.random()*100)
                        if espera < SALTO:
                          SALTO=espera
                          T[Y,X, id_msg, id_campo]=T[Y,X,id_msg, id_campo]+1
                        t_entrada[X,Y,id_msg,id_campo,t]=t+espera
                        t_generac[X,Y,id_msg,id_campo,t+espera]=t
                        tipo_mens[X,Y,id_msg,id_campo,t+espera]=2
                        nivel=niveles[X,Y,id_msg,id_campo]=niveles[X,Y,id_msg,id_campo]+1
                        largo_cola[Y,id_msg, id_campo]=largo_cola[Y,id_msg, id_campo]+1
                        FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
                        pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo]-1
                        if pendientes[Y,id_msg,id_campo] < 1:
                              # Y debe devolver la respuesta a quien lo consulto
                              lista=[]
                              lista=BUSCOPADRES(Y,id_msg,id_campo, lista) #Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
                              # b- genera una respuesta a partir de todas las calidades recibidas 
                              # c- genera un mensaje para cada padre de Respuesta 
                              
                              RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy,nivel)
                if t_generac[X,Y,id_msg,id_campo,hora] + TIMEOUT > t_entrada[X,Y,id_msg,id_campo, t_generac[X,Y,id_msg,id_campo,hora]]:
                          # actualizar favoritos de Y
                        FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                        rr="++++++++++++++++++++++++++++++++++respondo   ++++++++++++++++++++++++++++++++++++++  "  
             #       print("+++++++++++++++++++++++++++++++++++++++++++       respondo   ++++++++++++++++++++++++++  ")
             #      Resp.write(rr)
             
      
  #      if pendientes[X,id_msg,id_campo]== 0:
          # hacer fusion de todas las respuestas
          # LAS respuestas estan en respuestas[]
          
          # Supongo que en respuess[X,X] esta la respuesta propia
          
          # Calcular respuesta propia
                else:
                  TO_MSG[X,Y]=TO_MSG[X,Y]
          partes = line111.split(';') 
          
          R=partes[72] # en R va la respuesta del juego de datos
              
          aux=random.random()
          if aux>0.95:
            if R == "Yes":
              respuestas[X,Y,id_msg,id_campo]= 1
            else:
              respuestas[X,Y,id_msg,id_campo]= 0
              
          else:
            if R == "Yes":
              # pongo valores cruzados el 5% de las veces
              respuestas[X,Y,id_msg,id_campo]= 0
            else:
              respuestas[X,Y,id_msg,id_campo]= 1
              
          # fusion de los resultados
          
          aux=0
          p=0
   #       print("RESPONDER  valor de entrADA ",R, " resp ", str(respuestas[X,Y,id_msg,id_campo]))
              
          for j in range(1,N_agentes):
            if (X,j,id_msg,id_campo) in respuestas:
              aux=aux+respuestas[X,j,id_msg,id_campo]
              p=p+1
          aux=int(aux/p)
          
          #s=S[X,id_msg,id_campo]
          #nt=T[Y,X,id_msg,id_campo]
          # Qx1=nivel/(1+0.05)*(1/(nivel **  PESO_NIVEL))
          #Calculo Q  
       
          Qx1= 1/(1+H[X,id_campo])      
          a = restantes [X]
          
          if a > 0   and MODO == "I" or MODO=="S":
            if Qx1 > Qy or MODO == "S" :  # cuando la calidad es mayor que la del que consulta, responde
              espera=int(random.random()*100)
              if espera < SALTO:
                SALTO=espera
                
              
              Qx[X,Y,id_msg,id_campo]=Qx1
              T[Y,X,id_msg, id_campo]=T[Y,X,id_msg, id_campo]+1
              t_entrada[X,Y,id_msg,id_campo,t]=t+espera 
              t_generac[X,Y,id_msg,id_campo,t+espera]=t
              tipo_mens[X,Y,id_msg,id_campo,t+espera]=2 
              nivel=niveles[X,Y,id_msg,id_campo]=niveles[X,Y,id_msg,id_campo]+1
              if t_generac[X,Y,id_msg,id_campo,hora] + TIMEOUT > t_entrada[X,Y,id_msg,decision, t_generac[X,Y,id_msg,decision,hora]] : # no es t o
                
                
                largo_cola[Y,id_msg,id_campo]=largo_cola[Y,id_msg,id_campo]-1
                pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo]-1
                FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
              else:
                TO_MSG[X,Y]=TO_MSG[X,Y]+1
              if pendientes[Y,id_msg,id_campo] < 1:
                    # Y debe devolver la respuesta a quien lo consulto
                    # a- BUSCOPADRES(Y,id_msg,id_campo, lista) Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres
                    
                         
                lista=BUSCOPADRES(Y,id_msg,id_campo, lista)
                # b- genera una respuesta a partir de todas las calidades recibidas ++++
                # X manda resp a Y entonces para calcular calidad de Y deben haber respondido todos o ser time out de la consulta de Y a X
            
                if pendientes[Y,id_msg,id_campo]<1 or TIMEOUT < espera :      
                                                      
        #          print(" voy a calcular Qy compleja")
                  Qy=CALCULO_Qy(X,Y,id_msg,id_campo,Qy)   # OJO CALCULAR QY solo cuando haya pasado el timeout de Y o cuando respondieron todos
         #         print(" Qy compleja es ", Qy)                                
                
         #       GENERO_RESP(Y,id_msg,id_campo, lista, Qy)
                # c- genera un mensaje para cada padre de Respuesta ++++ 
                # para cada elem i de lista:
                #    genero mens de resp de Y a i para ese id_msg, id_campo y Qy
                for z in lista:
                  if restantes[Y]>0:
                    espera=int(random.random()*100)
                    t_entrada[Y,z,id_msg,id_campo,t]=t+espera
                    t_generac[Y,z,id_msg,id_campo,t+espera]=t
                    tipo_mens[Y,z,id_msg,id_campo,t+espera]=2
                    largo_cola[z,id_msg, id_campo]=largo_cola[z,id_msg, id_campo]-1
                    FAVORITOS[Y,z,id_campo]=FAVORITOS[Y,z,id_campo]+1
                    pendientes[z,id_msg,id_campo]=pendientes[z,id_msg,id_campo]-1   
                    Qx[z,Y,id_msg,id_campo]=Qy
                    Q[z,Y,id_msg,id_campo]=Qy
                    restantes[Y]=restantes[Y-1]                
                
                print("RESPONDO PADRES Y CON q",Qy)
                RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy,nivel)
                
            #    restantes[Y]=restantes[Y]-1
              
              if  t_generac[Y,X,id_msg,id_campo,hora] + TIMEOUT > t_entrada[Y,X,id_msg,id_campo, t_generac[Y,X,id_msg,id_campo,hora]]:
                # actualizar favoritos de Y 
                FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                pass
              else:
                  if Y == 1 :  # T O es cuando el sistema no contesta a tiempo, cuando NADIE contesta a tiempo
                    if max(t_generac[X,1,id_msg,id_campo],axis=0) +TIMEOUT < t:                 
                      TIMEOUTS = TIMEOUTS +1
                      TO_REG[X,1]=TO_REG[X,1]+1
              
            else:
                if MODO == "I":
                  PTEMPLE=(1-Qy)*(MAXREGS-restantes[X])/100
                  a=random.random()
                  if a > PTEMPLE:
                    if restantes[X]>0  :
                        espera=int(random.random()*100)
                        if espera < SALTO:
                          SALTO=espera
                          T[Y,X, id_msg, id_campo]=T[Y,X,id_msg, id_campo]+1
                        t_entrada[X,Y,id_msg,id_campo,t]=t+espera
                        t_generac[X,Y,id_msg,id_campo,t+espera]=t
                        tipo_mens[X,Y,id_msg,id_campo,t+espera]=2
                        nivel=niveles[X,Y,id_msg,id_campo]=niveles[X,Y,id_msg,id_campo]+1
                        largo_cola[Y,id_msg, id_campo]=largo_cola[Y,id_msg, id_campo]+1
                        FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
                        pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo]-1
                        if pendientes[Y,id_msg,id_campo] < 1:
                              # Y debe devolver la respuesta a quien lo consulto
                              lista=[]
                              lista=BUSCOPADRES(Y,id_msg,id_campo, lista) #Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
                              # b- genera una respuesta a partir de todas las calidades recibidas 
                              # c- genera un mensaje para cada padre de Respuesta 
                              
                              RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy,nivel)
                if t_generac[X,Y,id_msg,id_campo,hora] + TIMEOUT > t_entrada[X,Y,id_msg,id_campo, t_generac[X,Y,id_msg,id_campo,hora]]:
                          # actualizar favoritos de Y
                        FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                else:
                  TO_REG[Y,X]=TO_REG[Y,X]+1
              #rr="++++++++++++++++++++++++++++++++++respondo   ++++++++++++++++++++++++++++++++++++++  "  
             #       print("+++++++++++++++++++++++++++++++++++++++++++       respondo   ++++++++++++++++++++++++++  ")
             #      Resp.write(rr)
             
      else:
        if t_entrada [X,Y,id_msg,id_campo,t_generac[Y,X,id_msg,id_campo,hora] ] > t_generac[Y,X,id_msg,id_campo,hora] + TIMEOUT:
          TO_MSG[X,Y]=TO_MSG[X,Y]+1    
  return

#*************************************************************************************
def arma_lista_fav(x,c,l,N_favoritos,N_agentes):
  global Resp, TOLERANCIA
  import random
  # arma la lista de los favoritos en orden decreciente de exitos para el agente x y el campo c
  #global lista
  aux=0
  kk=0
  l=[]
  if MODO=="S":
    kk=int(random.random()*N_agentes)
    for ii in range(1,kk):
        g=int(random.random()*kk)
        l.append(g)
           
  else:
      for ii in range(1,N_agentes+1):
        if FAVORITOS[x,ii,c] >0 :
          
          if TO_MSG[x,ii]>TOLERANCIA:
            FAVORITOS[x,ii,c]=0
          else:
            l.append(ii)
            kk=kk+1
          
      for ii in range(0,kk):
       # if ii< kk:
          for pp in range (ii+1,kk):
            if FAVORITOS[x,l[ii],c] < FAVORITOS[x,l[pp],c]:
              
              aux=l[ii]
              l[ii]=l[pp]
              l[pp]=aux
  xx=0
  xx=x
  #rr="favoritos ag" +str(xx)+" campo "+str(c)+" -- "+str(lista[0:10])+'\n'
 # Resp.write(rr)
  print("favoritos ag" +str(xx)+" campo "+str(c)+" -- ",l[0:10])      
  return(l)

#*************************************************************************************

def main():

  import asyncio
  import random
#  import pandas
  import numpy
  import io
  import csv
  global Resp
  
  s="LOG DE SIMULADOR.txt"
  Resp=open(s,'w')
  
  #***********************************************************
  #      Parametros
  #***********************************************************
  # tiempo de time out
  global TIMEOUT
  
  #TIMEOUT= 1000
  
  TIMEOUT=1000
  
  # cantidad de mens restantes en el sistema
  
  global RESTANTES_ANT, RESTANTES_ANT_REG
  # cantidad de favoritos que se consultan cada vez
  global N_favoritos
  N_favoritos=2
  # cantidad de veces que se recibe un mensaje antes de cambiar el favorito
  N_interacciones=1
  # cantidad de agentes en el sistema
  
  global N_agentes
  
  global SALTO
  SALTO= 999

    # cantidad de campos en el mensaje
  
  global N_campos
  N_campos=73
  # campo de decision = cual es el nro de campo que significa lo decidido
  global decision
  
  decision = 72 # campo 73, 72 empezando desde 0
  
    
  # MAXentradas es el nro de mensajes de entradas que puede tener un ag
  MAXentradas=1000
  
  # cant reg a prcesar por OMEGA en el archivo
  global MAXREGS
  MAXREGS= 5       # 40 es el numero real 
  
  # general es cuantos se consultan cuando todavia no hay favoritos
  general = 100
  
  # cuantos instantes de tiempo corre la simulacion
  maxt=15000
 
  #com en que caracter del registro comienza el campo de decision
  com=150   # PUSE CUALQUIER COSA ++++++++++++++++++++++++++++++
  #fin  idem, pero fin****
  final=155
  
  global PESO_NIVEL
  PESO_NIVEL=0
  
  # MODO inteligente o simple
  global MODO
  MODO="I"
  

  
  global ncons
  #**************************************************************************************************
  # ESTRUCTURAS-
  #***************************************************************************************************
  import random
  global t
  global FAVORITOS
  global t_entrada
  global t_generac
  global largo_cola
  global tipo_mens
  global S
  global formado_por
  global H
  global Q
  global T
  global hora_mens
  

  ############################################# T A B L A S    ESTADISTICAS #####################################################
  global TABLA_EXITOS_E
  global TABLA_EXITOS_A
  global TABLA_MENS
  TABLA_EXITOS_E={}
  # cada fila tiene (iteracion,N_agentes,MAXREGS+1,MAXMENS), cada fila es una iterac
  TABLA_EXITOS_A={}
  # cada fila tiene (iteracion,N_agentes,MAXREGS+1,MAXMENS), cuenta EA cada fila es una iterac
  TABLA_MENS={}
    # cada fila tiene (iteracion,N_agentes,MAXREGS+1,MAXMENS), mensajes usados,  cada fila es una iterac
  global TABLA_CALIDADES_MENS
  global TABLA_CALIDADES_FREC
  TABLA_CALIDADES_MENS=numpy.zeros((40,101),dtype=int)
  TABLA_CALIDADES_FREC=numpy.zeros((40,101),dtype=int)
  # cada fila tiene cuantos mensajes se usaron para tener esa calidad final Q en la salida de OMEGA, cada fila es una iteracion 
  
  global TABLA_TO
  
  TABLA_TO={}
  
  # cantidad de T O que se produjeron por iteracion para una cierta cantidad de agentes y un cierto registro
  ##############################################################################################################
  global line111, line1
  global iteracion
  global TOLERANCIA
  global t
  global restantes
  TOLERANCIA=3 # cuantas veces se admite un to desde un favorito antes de borrarlo de la lista de favoritos
  MAXIT=2     # 32
 # for N_agentes in [10]:
#  for N_agentes in (10,20,30,40,50,100,200,300,600):
  for N_agentes in (10):
    # los errores  y los topes de confianza
    MIN_CONF=0.4
    MAX_CONF=0.95
    MIN_CONF_O=0.6
    MAX_CONF_O=0.87 
    
    # error de cada agente en cada campo
    H=numpy.zeros((N_agentes,N_campos), dtype=float)  
    for i in range(1,N_agentes):
      for j in range(0,N_campos):
        H[i,j]=1- min(random.random()+MIN_CONF, MAX_CONF)      
  # for MAXMENS in [1000]:
  #  for MAXMENS in (50,100,200,300,500,1000):   
    for MAXMENS in (100): 
      for MODO in ("I","S"):
      #for MODO in ["S"]:
        
            print(" ))))))))))))))))))))))))))))  MODO "+MODO+" (((((((((((((((((((((((((((((((((")
            if MODO=="I"  or MODO=="S":
              global restantes
              restantes=numpy.zeros(N_agentes, dtype=int)
              restantes.fill(MAXMENS)            
            
        
            for iteracion in range(1,MAXIT+1):
                RESTANTES_ANT=N_agentes*MAXMENS
                                  
                t=0  
                id_msg=0
                TIMEOUTS=0
                cuenta_to=0
                cuenta_a=0
                cuenta_e=0              
                print("######################### iteracion nro ##################", iteracion)
                RESTANTES_ANT= N_agentes*MAXMENS
                RESTANTES_ANT_REG= N_agentes*MAXMENS
                FAVORITOS=numpy.zeros((N_agentes+1,N_agentes+1,N_campos), dtype=int)
                for i in range (1,N_agentes+1) :
                  for j in range (1,N_agentes+1):
                    if i != j :
                      FAVORITOS[i,j]=1
                global TO_MSG
                TO_MSG=numpy.zeros((N_agentes+1, N_agentes+1), dtype=int) 
               
                
                # hora a la que se leyo el reg = a la que omega inicia la consulta
                hora_mens=numpy.zeros(MAXREGS+1, dtype=int)
                                  
                # nro de mensajes en la cola de un ag
                entradas=numpy.zeros(N_agentes, dtype=int)
                # t_entrada es el tiempo en el que llego ese mensaje a la entrada para un agente y un id mensaje
                # hora a la que llego un mensaje a la cola de un agente
              #  t_entrada=numpy.zeros((N_agentes,N_agentes, MAXREGS, N_campos,maxt), dtype=int)
                t_entrada={} 
                
                # t_gerac es el tiempo en que se genero el mensaje
                # t_generac=numpy.zeros((N_agentes,N_agentes, MAXREGS, N_campos,), dtype=int)
                t_generac={}
              
                
                # tipo del mensaje (consulta o respuesta)
               # tipo_mens=numpy.zeros((N_agentes,N_agentes, MAXREGS, N_campos,maxt), dtype=int)
              #  tipo_mens=numpy.array((N_agentes,N_agentes, MAXREGS, N_campos, maxt), dtype=int)
                tipo_mens={}
                
                # largo de cola de mens
               # largo_cola=numpy.zeros((N_agentes,MAXREGS, N_campos,maxt), dtype=int)
                largo_cola={}
                # pendientes de respuesta
                global pendientes
                pendientes=numpy.zeros((N_agentes,MAXREGS+1, N_campos), dtype=int)
                
                # respuestas recibidas supongo que no hay ds respuestas para el mismo campo y mens desde el mismo agente
               # respuestas=numpy.zeros((N_agentes,N_agentes, MAXREGS,N_campos, maxt), dtype=int) tiene sentido que respuestas dependan de t?? +++
                global respuestas
                respuestas={}
                # formado por
                formado_por=numpy.zeros((N_campos, N_campos), dtype=int)
                
                # aca se carga esa matriz de estructura...
                #
              
                # formado_por=pandas.read_csv("dependencias.csv", delimiter=',') 
                #formado_por = numpy.genfromtxt(dependencias.csv,delimiter=',',dtype=None, names=True)
                formado_por = numpy.loadtxt(open("dependencias.csv", "rb"), delimiter=",", skiprows=0)
                # nivel alcanzado en una consulta
                global niveles  
                niveles={}
                
                # cuantos consultar cuando no hay favoritos aun
                global muchos  
                muchos = 7
                 
                
                # calidad propia de Y de la respuesta del Y al X
                global Qx
                #Qx=numpy.zeros((N_agentes,N_agentes, MAXREGS,N_campos), dtype=float)
                Qx={}
                
                # Cantidad de agentes que responden en cada caso 
                T=numpy.zeros((N_agentes,MAXREGS+1,N_campos), dtype=int)
                 
                global Q
                # calidad de Y al responderle a X luego de considerar las otras respuestas
                  # Q  tiene la calidad que devuelve cada agente 
                Q={}
                
                # S cantidad de agentes consultados cuando X consulta a Y
                S={}
                
                # T cantidad de agentes que responden
                T={}
                
               
                    
                # lista de favoritos ordenada 
                #lista=numpy.zeros(100, dtype=int)
                # global lista
                lista=[]
                # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
                
                #s="datosOMEGA 1 reg.csv"
                s="datosOMEGA - 4 regs.csv"
               
                #s="datosOMEGA - 59 regs.csv"
                
                # * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * 
                try:
                  # f= open(s, 'r', encoding='ascii', errors='ignore')
                  f= open(s, 'r')
                  
                except:
                  print(s+"  ***** ARCHIVO INEXISTENTE *****" )
                 
                line1=f.readline()
                line111=line1.strip()   
                t_entrada={}
                t_generac={}
                largo_cola={}
                tipo_mens={}
                pendientes=numpy.zeros((N_agentes,MAXREGS+1, N_campos), dtype=int)
                Q={}
                Qx={}
                T={}
                niveles={}
                TO_MSG=numpy.zeros((N_agentes+1, N_agentes+1), dtype=int)                    
                
                llave=0
                 
                while len(line111) > 0:
                  line1=f.readline()
                  line111=line1.strip()                     
                  id_msg=id_msg+1  
                  
                  RESTANTES_ANT_REG=N_agentes*MAXMENS
                  
                  
                  print(";;;;;;;;;;;;;;;;;;;;;;;;;;; lei reg ;;;;;;;;;;;;;;;;",id_msg)
                  # GENERO LAS CONSULTAS DE OMEGA ****************************************
                  
                  
                  nivel = 1
              # Qx1 es la calidad de OMEGA     
              #    Qx1=0.95
                  #Qx1=random.random()
                  
                #  Cargo las calidades iniciales
                  Qx1=min(random.random()+MIN_CONF_O, MAX_CONF_O)
                  Qy=0
                  taux=t
                  rr="**************************************** proceso registro "+str(id_msg)+"\n"
                  print("*************************************** proceso registro "+str(id_msg))
                 # Resp.write(rr)
                  if llave == 0 :
                      tope = muchos
                      llave=1
                  else:
                      tope = N_favoritos +1
                 #llave = 1         COMENTE EL BLOQUE PARA EL DEBUGGING CON 1 SOLO REG. LLave dice si es el primer reg o no
                  
                  #tope=N_favoritos+1   # SACARLO CUANDO HAYA MAS DE UN REG
                   
                  for i in range (1,tope):
                    # si hay mensajes consulta a cada favorito
                      
                      #  print("Restantes de OMEGA"+str(restantes))
                          # arma la lista de los n favoritos ordenados por nros de exitos a partir de la matriz FAVORITOS
                          print("voy a armar lista fav")
                          lista=[]
                          lista=arma_lista_fav(1,decision,lista,N_favoritos,N_agentes)
                          print(" favs de OMEGA para decision",lista[1:10])
                          if not( i-1 > len(lista)):
                         #     rr="OMEGA consulta a "+str(lista[i-2])+" con calidad "+str(Qx1)+"\n"
                     #       Resp.write(rr)

                            if i> 2:
                              print ("OMEGA consulta a "+str(lista[i-2])+" con calidad "+str(Qx1))
                              if id_msg < MAXREGS+1:
                                niveles[1,lista[i-2],id_msg, decision]=nivel
                         #     T=t
                              if restantes[1] > 0  and MODO == "I" or MODO=="S":
                                  if i> 2 and id_msg < MAXREGS + 1 :
                                    Qy=CONSULTAR(1, lista[i-2], decision, id_msg, niveles[1,lista[i-2],id_msg, decision], Qx1, Qy, pendientes, N_campos, restantes)
                                    print("calidad devuelta a OMEGA en CONSULTAR"+str(Qy) ," calidad propiade OMEGA", Qx1)
                                 #   restantes[1]=restantes[1]-1
                                    taux=t
                                
                    
                        
                  k=0
                  tmax=0 
                  
                  # PROCESO LISTA DE MENSAJES GENERADOS POR REGISTRO ***************************************************
                #  print("PROCESO LISTA DE MENSAJES GENERADOS POR REGISTRO  tipo_mens  = ", tipo_mens, "t_entrada", t_entrada)
                  m=0
                  ag = 1
                  hay=0
                  xx=ag=m=campo=1
                 #mientras haya mensajes para algun agente
                  tt =0 
                  while tt < 200 :
                    hay = 0
                    a=t+tt
                    for xx, ag, m, campo,a in list(tipo_mens):
                              a=t+tt  
                              if (xx, ag, m, campo,a) in list(tipo_mens):
                                     
                                if t_generac[xx, ag, m, campo,a] + TIMEOUT > t+tt and tipo_mens[xx, ag, m, campo,a] == 2 and t_entrada[xx, ag, m, campo,t_generac[xx, ag, m, campo,a]] == t:  # o solo > t ?? NO ES TO 
                                  pendientes[ag,m,campo]=pendientes[ag,m,campo] - 1 
                                  
                                  print("no es T O y es repuesta de",xx," a", ag)
                                  hay =1 
                                  Qaux=Q[xx,ag,m,campo]
                                  if restantes[ag]>0  and MODO == "I" or MODO=="S":
                                    RESPONDER(ag,xx,m,campo,Qaux,N_agentes,tipo_mens,MODO, restantes,a)
                                    FAVORITOS[ag,xx,campo]=FAVORITOS[ag,xx,campo]+1
                                else:  
                                  if t_generac[xx, ag, m, campo,t+tt] + TIMEOUT > t+tt and t_entrada[xx, ag, m, campo, t_generac[xx, ag, m, campo,t+tt]] == t+tt and tipo_mens[xx, ag, m, campo,a] == 1 :    # 1 - consulta 2 - Respuesta :
                                  
                                      hay =1                         
                                      print("no es T O y es consulta de",xx," a", ag)   
                                      
                                                  
                                      # proceso consulta
                                      if (xx,ag,m,campo) not in Q:
                                        Q[xx,ag,m,campo]=0
                                      Qaux=Q[xx,ag,m,campo]
                
                                      #S[xx,m,campo]=S[xx,m,campo]+1
                                      if restantes[xx]>0  and MODO == "I" or MODO=="S":
                                        CONSULTAR(xx, ag, campo, m, niveles[xx, ag, m, campo], Qaux,Qy, pendientes, N_campos, restantes)        
                                  else:
                                    if t_generac[xx, ag, m, campo,a] + TIMEOUT < a:
                                      TO_MSG[xx,ag]=TO_MSG[xx,ag]+1
                                      
                                      TIMEOUTS=TIMEOUTS+1
                             
                    if hay ==1:
                      ttt=a  # ttt tiene el mayor tiempo en el que hubo mensajes a= t+tt
                      a=tt+t
                    tt=tt+1
                          
                    
                    # para cada agente X
                    # si tiene pendiente = 0 AND hay una cons para ese mens y ese campo cc y para ese agente X OR hay una consulta para un supercampo de cc y para X y ese mens
                    #      X responde 
                      
                    
                     # proceso los mensajes para OMEGA **********************************************************  
                    
              #    print("proceso mensajes de OMEGA en main()") 
                  if not (1,id_msg,decision) in largo_cola:
                    largo_cola[1,id_msg,decision] = 0
                  
                  #while k < largo_cola[1,id_msg,decision] + 1:
                  #while k < 100:
                  taux1=t
                  ES_EXITO_E=0
                  ES_EXITO_A=0
                  NO_ES_TO=0   # indica si hubo  o no T O . Si aunque sea uno solo contesta a omega a tiempo, no es TO
                  while taux<200:
                   # if RESPONDE_OMEGA==1:
                     # break
                     
                    #else:
                      pant=0
                      rant=0
                      tmax=0
                      p=1
                   #   print ("veo si hay mensajes para el momento actual  t="+str(taux))
                   #   rr="veo si hay mensajes para el momento actual  t="+str(taux)+"\n"
                   #  Resp.write(rr)
                   
                      p=0
                      r=1
                      tie=t
                      c=decision
                      pp=0
                      rr=r
                      while p < N_agentes+1:
                       
                        for r in range (1,MAXREGS+1):
                     #  for p,pp,rr,decision,tie in list(t_entrada) and pp==1 and tie==t:
                          if (p,1,r,decision,t) in t_entrada and  t_entrada[p,1,r,decision,t] == t+taux and tipo_mens[p,1,r,decision,t+taux]==2:
                            print("Hay mensaje para OMEGA desde ag" + str(p)+" para mens "+ str(r))
                            pant=p
                            rant=r
                            k=k+1
                            
                           # Qy calculada segun la form general para nivel =1 y error 0.95 es aprox 0.95
                           # Qy=0.95  # Calidad de Omega: 0.95
                           # Qy= random.random()  # dejo la calidad de Omega al azar
                     #       print("---- Calidad de OMEGA ="+str(Qx1))
                            if t_generac[p, 1, r, decision,t+taux] + TIMEOUT <= t_entrada [p,1,r,decision,t]:
                              # no es time out
                              NO_ES_TO=1
                              if Q[p,1, r,decision] > Qx1  : # no importa el MODO, es estricto   
                                ES_EXITO_E=1
                              #  EXITOS_E =EXITOS_E+1
                                FAVORITOS[1,p,decision]=FAVORITOS[1,p,decision]+1
                                               
                            # el tiempo gastado es el max (t de la entrada  - t de generac) para las distintas respuestas. sobre que calculo el maximo?????  +++++
                               # if tmax < taux - t :
                               #   tmax=taux-t
                               # if pant==0:   # es la primer vez que proceso esa entrada 
                               #   NO_TO=NO_TO+1
                      #          print ("calidad Y"+str(Qy)+"calidad X "+str(Qx[1, p, r,decision]))       
                                FAVORITOS[1,p,decision]= FAVORITOS[1,p,decision] + 1           
                                             
                                       
                              else:
                                if abs(Q[p,1, id_msg,decision] - Qx1)<0.0001:
                                  ES_EXITO_A=1
                             #       EXITOS_A =EXITOS_A+1
                  
                                
                            p=pant+1
                        
                        p=p+1  
                        k=k+1
                        
                      
                      taux=taux+1
                      
                  # no se si hacer temple simulado aca
                  # taux=taux+1
                  if NO_ES_TO ==0:
                    TIMEOUTS=TIMEOUTS+1  
                  NO=0 
                  ESTRICTO=0
                  AMPLIO=0
                  conte=0
                  print("##### t_gen","   ", t_generac)
                  print ("%%%%%%%%% t_ent", " ",t_entrada)
                  print(" &&&&& tipo_mens", tipo_mens)  
                  aporta_e=0
                  aporta_a=0
                  enhora=0
                  u=1
                  tiempo=t
#                  for u in range (1,N_agentes) :
#                   for tiempo in range (0,t+TIMEOUT):
                  uu=0
                      
                  for u,uu,id_msg,decision,tiempo in list(tipo_mens): 
                     #   print (tipo_mens[u,1,id_msg,decision,tiempo],t_generac[u,1,id_msg,decision,tiempo],t_entrada[u,1,id_msg,decision, t_generac[u,1,id_msg,decision,tiempo]])
                    if uu==1 and tiempo > t :   
                        print ("encontre", u,1,id_msg,decision,tiempo )
                        if tipo_mens[u,1,id_msg,decision,tiempo]== 2 and  t_generac[u,1,id_msg,decision,tiempo] + TIMEOUT > t_entrada[u,1,id_msg,decision, t_generac[u,1,id_msg,decision,tiempo]] :
                          print("************  NO ES T O")
                          enhora=1
                          print("Q es ", Qx[u,1,id_msg,decision]," calidad de OMEGA=",Qx1)
                          if Qx1 < Qx[u,1,id_msg,decision]  :
                            ESTRICTO=1
                          else:
                            if abs(Qx1- Qx[u,1,id_msg,decision]) < 0.01:
                              AMPLIO=1
                            
                            
                          NO=1
                        else:
                          if t_generac[u,1,id_msg,decision,tiempo] + TIMEOUT < t_entrada[u,1,id_msg,decision, t_generac[u,1,id_msg,decision,tiempo]] :
                            TO_MSG[u,1]=TO_MSG[u,1]+1
                  if NO == 0:
                        print("********ESSSSS TO") 
                        cuenta_to=cuenta_to+1
                  if ESTRICTO == 1:
                        aporta_e=1
                        cuenta_e=cuenta_e+1
                  else:
                    if AMPLIO == 1 and conte == 0:
                          aporta_a=1
                          cuenta_a=cuenta_a+1
                          conte=1
                  if enhora == 1 and aporta_e == 0 and aporta_a == 0: # viene unmensaje pero la calidad no sirve
                    cuenta_to=cuenta_to+1
                    
                    
                  print("------------------ cuenta to ---------------",cuenta_to)  
                  
                  print("cuenta E E ", cuenta_e)
                  print("cuenta E A ", cuenta_a)
                  
                  
                  
                  
                  if ES_EXITO_A == 1:
                    EXITOS_A=EXITOS_A+1
        
                  if ES_EXITO_E ==1:
                    EXITOS_E=EXITOS_E+1
                           
                  SALTO=max(SALTO,1)
                  t=t+SALTO
                 
                  RESTANTES_ANT_REG= N_agentes*MAXMENS
                  
                #  hora_mens[id_msg]=t
                #  if id_msg > MAXREGS -1 :
                #    continue
                
                  # cereo arreglos ******************************************************************
                  #    print("EXITOS A ", str(EXITOS_A),"EXITOS E ", str(EXITOS_E), "TIME OUTS ", str(TIMEOUTS))
                
                        
                  
                  SALTO=999
                    
                    
                    #  ******************************************************************************
                    
                
                rr=" *****************  FIN DE EJECUCION DE ITERACION*****************"
               # Resp.write(rr)
             #   print(rr)
                
                #TABLA_EXITOS_A.append(iteracion,N_agentes,MAXREGS,MAXMENS)
                TABLA_EXITOS_A[iteracion,N_agentes,MAXREGS,MAXMENS]=cuenta_a
               # TABLA_EXITOS_E.append(iteracion,N_agentes,MAXREGS,MAXMENS)
                TABLA_EXITOS_E[iteracion,N_agentes,MAXREGS,MAXMENS]=cuenta_e  
                TABLA_TO[iteracion,N_agentes,MAXREGS]=cuenta_to
                
                r=0
                for i in range (1,N_agentes):
                  r=r+restantes[i]
               # TABLA_MENS.append(iteracion,N_agentes,MAXREGS,MAXMENS)
                TABLA_MENS[iteracion,N_agentes,MAXREGS,MAXMENS]=RESTANTES_ANT-r   
            #    print(TABLA_MENS[iteracion,N_agentes,MAXREGS,MAXMENS])
            
               
                RESTANTES_ANT=r 
                      
            print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\          fin     /////////////////////////////////////")
            
            s="RESULTADOS"+str(N_agentes)+"_"+str(MAXMENS)+"_"+MODO+"_"+str(MAXIT)+".txt"
            
            R= open(s, 'w', encoding='ascii', errors='ignore')
            R.write("************************* PARAMS ***************************************\n")   
            R.write("  \n") 
            s="################# Modo = "+ MODO+ "  ####################################\n"
            R.write(s)
            R.write("  \n")   
            s="N_agentes =" + str(N_agentes)+"\n"
            R.write(s)
            R.write("  \n") 
            s="Max mens =" + str(MAXMENS)+"\n"
            R.write(s)
            R.write("  \n") 
            s="Iteraciones =" + str(MAXIT)+"\n"
            R.write(s)
            R.write("  \n")   
            R.write("************************* TIME  OUTS ***************************************\n") 
            for i in range (1,MAXIT+1):
              if (i,N_agentes,MAXREGS,MAXMENS) in TABLA_TO:
                s=str(TABLA_TO[i,N_agentes,MAXREGS])+"\n"
                R.write(s)
            R.write("  \n")  
           
            R.write("************************* FREC DE CALIDADES  ***************************************\n")   
            R.write("  \n")         
            for j in range (1,MAXIT+1):
              for i in range (0,100):
                s=str(TABLA_CALIDADES_FREC[j,i])+","
                R.write(s)
              R.write("  \n")  
              for i in range (0,100):
                s=str(TABLA_CALIDADES_FREC[j,i])+"\n"
                R.write(s)
              R.write("  \n")             
            R.write("************************* MENS por CALIDADES  ***************************************\n")   
            R.write("  \n")         
            for j in range (1,MAXIT+1):
              for i in range (0,100):
                s=str(TABLA_CALIDADES_MENS[j,i])+","
                R.write(s)
              R.write("  \n")      
              for i in range (0,100):
                s=str(TABLA_CALIDADES_MENS[j,i])+"\n"
                R.write(s)
              R.write("  \n")                   
              
           
            s="************************* MENS TOTALES POR ITERACION   ***************************************\n"
            R.write(s)
            for i in range (1,MAXIT+1):
              if (i,N_agentes,MAXREGS,MAXMENS) in TABLA_MENS:
                s=str(TABLA_MENS[i,N_agentes,MAXREGS,MAXMENS])+"\n"
                R.write(s)
            R.write("  \n")      
            s="************************* EXITOS ESTR TOTALES POR ITERACION   ***************************************\n"
            R.write(s) 
            for i in range (1,MAXIT+1):
              if (i,N_agentes,MAXREGS,MAXMENS) in TABLA_EXITOS_E:
                s=str(TABLA_EXITOS_E[i,N_agentes,MAXREGS,MAXMENS])+"\n"
                R.write(s)
            R.write("  \n")   
            s="************************* EXITOS AMPLIOS TOTALES POR ITERACION   ***************************************\n"
            R.write(s) 
            for i in range (1,MAXIT+1):
              if (i,N_agentes,MAXREGS,MAXMENS) in TABLA_EXITOS_A:
                s=str(TABLA_EXITOS_A[i,N_agentes,MAXREGS,MAXMENS])+"\n"
                R.write(s)
            R.write("  \n")    
            R.close()
main()