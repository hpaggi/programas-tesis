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
  lista_subcampos=[]
  ccons=numpy.zeros(N_campos, dtype=int)
  S[X,Y,id_msg,id_campo]=S[X,Y,id_msg,id_campo]+1
  
#  print("S es",str( S[X,Y,id_msg,id_campo]), "X es ", str(X), "Y es ",str(Y))
  if (Y,id_msg,id_campo) not in   largo_cola:
    largo_cola[Y,id_msg,id_campo] = 1
  else:   
    largo_cola[Y,id_msg,id_campo]=largo_cola[Y,id_msg,id_campo]+1
 
  
  # nro de campos por los que consulto ************************************************************
  ncons=0
  
  # veo los subcampos que hay
  tot=0
  lista_subcampos=[]
  for i in range (1,N_campos):
    if formado_por[id_campo,i]== 1:
      lista_subcampos.append(i)
      tot=tot+1
  #++++++++++++++++++++ Agregado para testing para simplificar. habria que sacarlo luego+++
  if tot> 3:
    tot = 3
  #+++++++++++++++++++++fin agregado +++++++++++++
  
 # print("campo "+str(id_campo)+" total subcampos   "+str(tot))
  rr="campo "+str(id_campo)+" total subcampos   "+str(tot)+"\n"
  Resp.write(rr)
  rr="Subcampos de"+str(id_campo)+str(lista_subcampos)+"\n"
  #Resp.write(rr) 
  
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
          
# Y consulta a otro por subcampo
    fav=0
#    print("campos a consultar  ",ccons[0:20])
    rr="campos a consultar  "+str(ccons[0:20])+"\n"
#    Resp.write(rr)
    # ncons dice hasta cuantos campos consulto, kk dice cuantos subcampos consulto realmente
    if kk>0: 
     #   print("voy a ver subcampos")
        k=0
        while k < kk:
          if restantes[Y] > 0:
            favor=[]
            p=1
            arma_lista_fav(Y,ccons[k],favor,N_favoritos,N_agentes)
            print("fav  para Y ******",Y, "campo",ccons[k],"  ", favor)
           # print("EXITOS FAV PARA ", Y, "=" )
          #  for x in range (1, N_agentes):
           #   print(FAVORITOS[Y,x ,ccons[k]], " ");
            rr="fav *****"+str(favor[0:10])+"\n"
  #          Resp.write(rr)
            
            p=1
    
            while  p < N_favoritos:  # en realidad habria que distinguir su ya se determinaron los favoritos y sino usar muchos como fin de loop
              Z= favor[p-1]
              Qz=0.0 # ojo. poner 0.0 a todas las calidades como valor inicial
              if not Z == X:
                nivel=nivel+1
                niveles[Y,Z,id_msg, ccons[k]]=nivel
                if not (X,Y,id_msg, ccons[k]) in S:
                  S[X,Y,id_msg, ccons[k]] = 1
                  largo_cola[Y, id_msg, ccons[k]] = 1
                else:
                  S[X,Y,id_msg, ccons[k]] = S[Y,id_msg, ccons[k]] +1
                  
                largo_cola[Y, id_msg, ccons[k]]=largo_cola[Y, id_msg, ccons[k]]+1
               # S[Y,id_msg, ccons[k]] = S[Y,id_msg, ccons[k]] +1 
                
                Qx[Y,Z,id_msg, ccons[k]]=niveles[Y,Z,id_msg, ccons[k]]/(1+H[Y,ccons[k]])*(1/ niveles[Y,Z,id_msg, ccons[k]])**(PESO_NIVEL + 1)  # +++++ en realidad seria la calidad propia de Y para ese campo ++++++
                
                
                rr="Genero consulta de Y =" +str(Y)+"a Z ="+str(Z)+ " msg "+str(id_msg)+ " campo  "+ str(ccons[k]) + " cola  "+str(largo_cola[Y, id_msg, ccons[k]])+"Qx"+str(Qx[Y,Z,id_msg,ccons[k]])+"\n"
           #     Resp.write(rr)
           #     print("Genero consulta de Y =" +str(Y)+"a Z ="+str(Z)+ " msg "+str(id_msg)+ " campo  "+ str(ccons[k]) + " cola  "+str(largo_cola[Y, id_msg, ccons[k]])+"Qx"+str(Qx[Y,Z,id_msg,ccons[k]]) )
           # print("Genero Consulta de " +str(Y)+"a X "+str(X)+ " msg "+str(id_msg)+ " campo  "+ str(ccons[k]) + " cola  "+str(largo_cola[Y, id_msg, ccons[k]]) )
            
            
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
      devuelvo_resp(Y,X,id_msg,id_campo,nivel,Qy)
 #     print("devuelvo respuesta ",Y,X,id_msg,id_campo,str(nivel),str(Qy))
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
      
      if Qy > Qx1:
        # devolver respuesta // poner en la cola de mens de entrada de Y un mens de resp con hora 100 mas que t
#        print("VOY A devuelvo respuesta ",Y,X,id_msg,id_campo,str(nivel),str(Qy))
        devuelvo_resp(Y,X,id_msg,id_campo,nivel,Qy)
        Qx[X,Y,id_msg,id_campo]=Qy # tomo la calidad y no me fijo si es un T O 
       
        rr="devuelvo respuesta "+str(Y)+str(X)+str(id_msg)+str(id_campo)+str(nivel)+str(Qy)+"\n"        
   #     Resp.write(rr)
      
  return

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
  R=T[X,Y,id_msg,id_campo]**2/S[X,Y,id_msg,id_campo]
  # X responde a Y
  Qtecho=1/(1+H[Y,id_campo])
  if R==0:
  #  n=niveles[X,Y,id_msg,id_campo]
    Qy=1/(1+H[Y,id_campo])
    Qx[X,Y,id_msg,id_campo]=Qy
    
    Q[X,Y,id_msg,id_campo]=Qy
    
    return
  Qy=max(Qtecho,q)**((PESO_NIVEL+1)/R)
  Q[X,Y,id_msg,id_campo]=Qy
# cuando el que recibe es OMEGA ya calculo si es un exito  
  if Y == 1 :
    if T[Y,X,id_msg,id_campo]==0:  #X responde a Y o sea Y consulta a X
      TIMEOUTS=TIMEOUTS+1
    else:  
      if Qy > Qx[X,Y,id_msg,id_campo]:
       ES_EXITO_E=1
      #EXITOS_E=EXITOS_E+1
      else:
        if Qy == Qx[X,Y,id_msg,id_campo]:
          ES_EXITO_A=1
        # EXITOS_A=EXITOS_A+1      
 # print("Calculo Qy="+str(Qy)+ " id msg "+" msg "+str(id_msg)+ " id campo " + str(id_campo))
  return
#************************************************************************************
def CALCULO_Qy_SIMPLE(Y,id_msg,id_campo,Qy):
  import numpy
  
  # calidad  de Y cuando Y NO CONSULTA A NADIE MAS
  
  # Max=numpy.amax(Q,axis=1)
 
  global EXITOS_E
  global EXITOS_A
  
  
  global TIMEOUTS
        
  # print("calculo Q. cal simple")
  
  # n=niveles[X,Y,id_msg,id_campo]
  
  Qy=1/(1+H[Y,id_campo])
  Qx[X,Y,id_msg,id_campo]=Qy 
  Q[X,Y,id_msg,id_campo]=Qy
#  print("Calculo Qy  SIMPLE ="+str(Qy)+ " id msg "+str(id_msg)+ " id campo " + str(id_campo))
  return
#****************************************************************************************************************************************

def BUSCOPADRES(Y, id_msg, id_campo, lista): # Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
  global tipo_mens
  lista=[]
  if Y==1:
    lista={1}
   # print ("busco padres de OMEGA")
    return
  for ag in range (1,N_agentes):
    if ((ag,Y,id_msg,id_campo) in   tipo_mens) and tipo_mens[ag,Y,id_msg,id_campo]=="1":
      lista.append(ag)
  # print("Busco padres"+ "Y"+ str(Y)+" msg" +str(id_msg)+ " campo "+str(id_campo)+"lista:")
  # print(lista)
  return
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
    
  #  print("estoy en devuelvo resp  X="+str(X)+" Y= " +str(Y)+" id_campo "+str(id_campo))
    espera=int(100*random.random())
    if espera < SALTO:
      SALTO=espera    
    t_entrada[X, Y, id_msg, id_campo,t]= t +  espera
    t_generac[X, Y, id_msg, id_campo, t+espera]= t 
  
    tipo_mens[X,Y, id_msg, id_campo,t+espera]=2
    if not (Y, id_msg, id_campo) in largo_cola:
      largo_cola[Y, id_msg, id_campo]=0
    largo_cola[Y, id_msg, id_campo]= largo_cola[Y, id_msg, id_campo] +1
    niveles[X,Y,id_msg, id_campo]=nivel+1
  
    Qx[X,Y,id_msg, id_campo]=Qy   # la respuesta de la cons de X a Y es Qx   
    pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo] - 1
    
    restantes[X]=restantes[X]-1
    if pendientes[Y,id_msg,id_campo] < 1 or ES_TO(Y,id_msg,id_campo):
      
      # Y debe devolver la respuesta a quien lo consulto
      #  Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres
      BUSCOPADRES(Y,id_msg,id_campo, lista)
      #   genera una respuesta a partir de todas las calidades recibidas    Esa respuesta es Qy1

      # Tomo todos los pesos iguales, asi que solo hago el promedio de calidades de las respuestas
      Qy1=0
      cuenta=0
      for i in range (1,N_agentes):
        Qy1=Q[i,Y,id_msg,id_campo] + Qy1
        cuenta=cuenta+1
      Qy1=Qy1/cuenta
      Q[X,Y,id_msg,id_campo]=Qy1
      
      print(Qy,Qy1)
      
      # Qy1=0.967890         
      # genera un mensaje para cada padre de Respuesta
      RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy1,nivel)
      RESPONDE_OMEGA=0 
      if Y == 1:
  #      print("**** respuesta de OMEGA al msg ", str(id_msg), " valor =", str(respuestas[X,Y,id_msg,id_campo]), "calidad",str(Qy))
        RESPUESTA_OMEGA (1,1,id_msg,decision,Qx,Qy,N_agentes,tipo_mens,MODO, restantes)
        
        RESPONDE_OMEGA=1
        
 #   print("Responde "+str(X) + " a " +str (Y)+ " msg "+str(id_msg)+" campo "+str(id_campo)+ " calidad "+ str(Qy))
    rr="Responde "+str(X) + " a " +str (Y)+ " msg "+str(id_msg)+" campo "+str(id_campo)+ " calidad "+ str(Qy)
#    Resp.write(rr)
    return
#************************************************************************************
def ES_TO(Y,id_msg,id_campo):
  
  # ES T O si ninguno de los consultados por Y para id_msg e id_campo contesto
  maxt=0
  for i in range (1,N_agentes):
    for j in range(0,t):
      if  tipo_mens[i,Y,id_msg,id_campo,j] == 2 and t_generac[i,Y,id_msg,id_campo,j] + TIMEOUT > t_entrada[i,Y,id_msg,id_campo, t_generac[i,Y,id_msg,decision,j]] :
        return False
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
    aux=aux+respuestas[X,j,id_msg,id_campo]
    p=p+1
  aux=int(aux/p)
 
 # CALCULO_Qy(X,Y,id_msg,id_campo,Qy)
  CALCULO_Qy(1,1,id_msg,id_campo,Qy)

   
  if   (X,Y,id_msg,id_campo) not in Qx:
    Qx[X,Y,id_msg,id_campo]=Qy
  Qx1=Qx[X,Y,id_msg,id_campo]
  Q[X,Y,id_msg,id_campo]=Qx1
  
  # es time out si ningun mensaje llega a omega a tiempo. O sea si el t_entrada mayor + TIMEOUT < t
  ymax=1
  maxt=0
  for i in range (1,N_agentes):
    
    for j in range(0,t):
      if (i,1,id_msg,id_campo,j) in t_entrada:
        if  t_entrada [i,1,id_msg,id_campo,j] > maxt and tipo_mens[i,1,id_msg,id_campo,j] == 2:
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
    devuelvo_resp(Y,lista[i],id_msg,id_campo,nivel,Qy1)
    
  return
  
  

# ***********************************************************************************
def RESPONDER(X,Y,id_msg,id_campo,Qx,Qy,N_agentes,tipo_mens,MODO, restantes,hora):

  # X envia respuesta a Y
  
  global SALTO
  global t_entrada
    
  #for i in range (1,largo_cola[X, id_msg, id_campo]):
  if (X,Y,id_msg,id_campo,t) in tipo_mens:
      if tipo_mens[X,Y,id_msg,id_campo,hora]==2 and t_entrada [X,Y,id_msg,id_campo,hora] == t or tipo_mens[X,Y,id_msg,id_campo,hora]==1 and t_entrada [X,Y,id_msg,id_campo,hora] > t_generac[Y,X,id_msg,id_campo,hora] + TIMEOUT:
  #      if pendientes[X,id_msg,id_campo]== 0:
          # hacer fusion de todas las respuestas
          # LAS respuestas estan en respuestas[]
          
          # Supongo que en respuess[X,X] esta la respuesta propia
          
          # Calcular respuesta propia
                    
          partes = line111.split(',') 
          
          R=partes[72] # en R va la respuesta del juego de datos
              
          aux=random()
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
            aux=aux+respuestas[X,j,id_msg,id_campo]
            p=p+1
          aux=int(aux/p)
          
          #s=S[X,id_msg,id_campo]
          #nt=T[X,id_msg,id_campo]
          # Qx1=nivel/(1+0.05)*(1/(nivel **  PESO_NIVEL))
          #Calculo Q  
       
                
          a = restantes [X]
          
          if a > 0 :
            if Qx1 > Qy:  # cuando la calidad es mayor que la del que consulta, responde
              espera=int(random()*100)
              if espera < SALTO:
                SALTO=espera
                
              
              Qx[X,Y,id_msg,id_campo]=Qx1
              T[Y,id_msg, id_campo]=T[Y,id_msg, id_campo]+1
              t_entrada[X,Y,id_msg,id_campo,t]=t+espera 
              t_generac[X,Y,id_msg,id_campo,t+espera]=t
              tipo_mens[X,Y,id_msg,id_campo,t+espera]=2 
              niveles[X,Y,id_msg,id_campo]=niveles[X,Y,id_msg,id_campo]+1
              if t_generac[X,Y,id_msg,id_campo,t] + TIMEOUT > t_entrada[u,1,id_msg,decision, t_generac[u,1,id_msg,decision,tiempo]] : # no es t o
                
                
                largo_cola[Y,id_msg,id_campo]=largo_cola[Y,id_msg,id_campo]-1
                pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo]-1
                FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
              
              if pendientes[Y,id_msg,id_campo] < 1:
                    # Y debe devolver la respuesta a quien lo consulto
                    # a- BUSCOPADRES(Y,id_msg,id_campo, lista) Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres
                    
                         
                BUSCOPADRES(Y,id_msg,id_campo, lista)
                # b- genera una respuesta a partir de todas las calidades recibidas ++++
                # X manda resp a Y entonces para calcular calidad de Y deben haber respondido todos o ser time out de la consulta de Y a X
            
                if pendientes[Y,id_msg,id_campo]<1 or TIMEOUT < espera :      
                                                      
        #          print(" voy a calcular Qy compleja")
                  CALCULO_Qy(X,Y,id_msg,id_campo,Qy)   # OJO CALCULAR QY solo cuando haya pasado el timeout de Y o cuando respondieron todos
         #         print(" Qy compleja es ", Qy)                                
                
                GENERO_RESP(Y,id_msg,id_campo, lista, Qy)
                # c- genera un mensaje para cada padre de Respuesta ++++ 
                # para cada elem i de lista:
                #    genero mens de resp de Y a i para ese id_msg, id_campo y Qy
                
                print("QYYYYY",Qy)
                RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy,nivel)
                
                restantes[Y]=restantes[Y]-1
              
              if  t_generac[Y,X,id_msg,id_campo,t] + TIMEOUT > t_entrada[Y,X,id_msg,id_campo, t_generac[Y,X,id_msg,id_campo,t]]:
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
                  a=random()
                  if a > PTEMPLE:
                    espera=random()*100
                    if espera < SALTO:
                      SALTO=espera
                    T[Y,id_msg, id_campo]=T[Y,id_msg, id_campo]+1
                    t_entrada[X,Y,id_msg,id_campo,t]=t+espera
                    t_generac[X,Y,id_msg,id_campo,t+espera]=t
                    tipo_mens[X,Y,id_msg,id_campo,t+espera]=2
                    niveles[X,Y,id_msg,id_campo]=niveles[X,Y,id_msg,id_campo]+1
                    largo_cola[Y,id_msg, id_campo]=largo_cola[Y,id_msg, id_campo]+1
                    FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
                    pendientes[Y,id_msg,id_campo]=pendientes[Y,id_msg,id_campo]-1
                    if pendientes[Y,id_msg,id_campo] < 1:
                          # Y debe devolver la respuesta a quien lo consulto
                          BUSCOPADRES(Y,id_msg,id_campo, lista) #Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
                          # b- genera una respuesta a partir de todas las calidades recibidas 
                          # c- genera un mensaje para cada padre de Respuesta 
                          RESPONDO_PADRES(Y,id_msg,id_campo, lista, Qy,nivel)
            if t_generac[X,Y,id_msg,id_campo,t] + TIMEOUT > t_entrada[X,Y,id_msg,id_campo, t_generac[X,Y,id_msg,id_campo,t]]:
                      # actualizar favoritos de Y
                    FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                    rr="++++++++++++++++++++++++++++++++++respondo   ++++++++++++++++++++++++++++++++++++++  "  
             #       print("+++++++++++++++++++++++++++++++++++++++++++       respondo   ++++++++++++++++++++++++++  ")
             #      Resp.write(rr)
             
    
  return
#*************************************************************************************
def arma_lista_fav(x,c,lista,N_favoritos,N_agentes):
  global Resp
  # arma la lista de los favoritos en orden decreciente de exitos para el agente x y el campo c
  #global lista
  aux=0
  kk=0
  for ii in range(1,N_agentes+1):
    if FAVORITOS[x,ii,c] >0 :
      lista.append(ii)
      kk=kk+1
      
  for ii in range(0,kk):
    if ii< kk:
      for pp in range (ii+1,kk):
        if FAVORITOS[x,lista [ii],c] < FAVORITOS[x,lista [pp],c]:
          
          aux=FAVORITOS[x,lista [ii],c]
          lista[ii]=FAVORITOS[x,lista [pp],c]
          lista[pp]=aux
  xx=0
  xx=x
  rr="favoritos ag" +str(xx)+" campo "+str(c)+" -- "+str(lista[0:10])+'\n'
 # Resp.write(rr)
  #print("favoritos ag" +str(xx)+" campo "+str(c)+" -- ",lista[0:10])      
  return

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
  
  TIMEOUT=200
  
  # cantidad de favoritos que se consultan cada vez
  global N_favoritos
  N_favoritos=2
  # cantidad de veces que se recibe un mensaje antes de cambiar el favorito
  N_interacciones=1
  # cantidad de agentes en el sistema
  
  global N_agentes
  
  global SALTO
  SALTO= 999

  
  N_agentes=9 # para simplificar
  
  # cantidad de campos en el mensaje
  
  global N_campos
  N_campos=73
  # campo de decision = cual es el nro de campo que significa lo decidido
  global decision
  
  decision = 72 # campo 73, 72 empezando desde 0
  
  
  # MAXMENS cant max de mensajes por agente
  MAXMENS = 15
  
  # MAXentradas es el nro de mensajes de entradas que puede tener un ag
  MAXentradas=1000
  
  # cant reg a prcesar por OMEGA en el archivo
  MAXREGS= 40          # 40 es el numero real 
  
  # general es cuantos se consultan cuando todavia no hay favoritos
  general = 100
  
  # cuantos instantes de tiempo corre la simulacion
  maxt=5000
 
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
  # ESTRUCTURAS
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
  
  global line111
  
  FAVORITOS=numpy.zeros((N_agentes+1,N_agentes+1,N_campos), dtype=int)
                        
  # error de cada agente en cada campo
  H=numpy.zeros((N_agentes,N_campos), dtype=float)
  
  # hora a la que se leyo el reg = a la que omega inicia la consulta
  hora_mens=numpy.zeros(MAXREGS, dtype=int)
  
  
  global restantes
  restantes = []
  restantes=numpy.zeros(N_agentes, dtype=int)
  restantes.fill(MAXMENS)
  
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
  largo_cola=numpy.zeros((N_agentes,MAXREGS, N_campos), dtype=int)
  # pendientes de respuesta
  global pendientes
  pendientes=numpy.zeros((N_agentes,MAXREGS, N_campos), dtype=int)
  
  # respuestas recibidas supongo que no hay ds respuestas para el mismo campo y mens desde el mismo agente
 # respuestas=numpy.zeros((N_agentes,N_agentes, MAXREGS333933,N_campos, maxt), dtype=int) tiene sentido que respuestas dependan de t?? +++
  global respuestas
  respuestas=numpy.zeros((N_agentes,N_agentes, MAXREGS,N_campos), dtype=int)
  # formado por
  formado_por=numpy.zeros((N_campos, N_campos), dtype=int)
  
  # aca se carga esa matriz de estructura...
  #

  # formado_por=pandas.read_csv("dependencias.csv", delimiter=',') 
  #formado_por = numpy.genfromtxt(dependencias.csv,delimiter=',',dtype=None, names=True)
  formado_por = numpy.loadtxt(open("dependencias.csv", "rb"), delimiter=",", skiprows=0)
  # nivel alcanzado en una consulta
  global niveles  
  niveles=numpy.zeros((N_agentes, N_agentes, MAXREGS, N_campos), dtype=int)
  
  # cuantos consultar cuando no hay favoritos aun
  global muchos  
  muchos = 7
   
  
  # calidad propia de Y de la respuesta del Y al X
  global Qx
  #Qx=numpy.zeros((N_agentes,N_agentes, MAXREGS,N_campos), dtype=float)
  Qx={}
  
  # Cantidad de agentes que responden en cada caso 
  T=numpy.zeros((N_agentes,MAXREGS,N_campos), dtype=float)
   
  global Q
  # calidad de Y al responderle a X luego de considerar las otras respuestas
    # Q  tiene la calidad que devuelve cada agente 
  Q=numpy.zeros((N_agentes,N_agentes,MAXREGS, N_campos), dtype=float)
  
  # S cantidad de agentes consultados cuando X consulta a Y
  S=numpy.zeros((N_agentes, N_agentes, MAXREGS,N_campos), dtype=int)
  
  # T cantidad de agentes que responden
  T=numpy.zeros((N_agentes, N_agentes, MAXREGS,N_campos), dtype=int)
  
  # los errores 
  MIN_CONF=0.5
  MAX_CONF=0.999
  for i in range(1,N_agentes):
    for j in range(0,N_campos):
      H[i,j]=1- min(random.random()+MIN_CONF, MAX_CONF)
      
  # lista de favoritos ordenada 
  #lista=numpy.zeros(100, dtype=int)
  # global lista
  lista=[]
  # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
  #s="datosOMEGA.csv"
 # s="datosOMEGA 8 reg.csv"
 
  s="datosOMEGA - 59 regs.csv"
  
  # * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * 
  try:
    # f= open(s, 'r', encoding='ascii', errors='ignore')
    f= open(s, 'r')
    
  except:
    print(s+"  ***** ARCHIVO INEXISTENTE *****" )
    return
  
  # al principio los favoritos de los agentes son todos los demas, luego cada agente consulta los N_favoritos mejores
  
  for i in range (1,N_agentes):
    for j in range (1,N_agentes):
      for campo in range (1,N_campos):
        if not i==j:
          FAVORITOS[i,j,campo]=1
                  
  # los id de agentes empiezan en 1, OMEGA es el 1                   
  
  # el primer reg es de cabezales
  line1=f.readline()
  line111=line1.strip() 
  
  # leo registros
  line1=f.readline()
  line111=line1.strip() 
      #
      #print(line1)
  # t es el tiempo que va pasando
  
  t=0
  id_msg= 1
  llave=0
  
  # nro de exitos
  global EXITOS_E
  global EXITOS_A
  global ES_EXITO_A
  global ES_EXITO_B
  EXITOS_E=0
  EXITOS_A=0
  
  cuenta_e=0
  cuenta_a=0
  
  # nro de NO timeouts
  NO_TO=0
  
  global TIMEOUTS
  TIMEOUTS =0  
  
  
  taux=t
  
  #***********************************
  cuenta_to=0
  
  #***********************************  
  
  while len(line1) > 0:
    
    
    # GENERO LAS CONSULTAS DE OMEGA ****************************************
    
    
    nivel = 1
# Qx1 es la calidad de OMEGA     
#    Qx1=0.95
    #Qx1=random.random()
    
    MIN_CONF_O=0.7
    MAX_CONF_O=0.999
    Qx1=min(random.random()+MIN_CONF_O, MAX_CONF_O)
    Qy=0
    taux=t
    rr="**************************************** proceso registro "+str(id_msg)+"\n"
    print("*************************************** proceso registro "+str(id_msg))
   # Resp.write(rr)
   # if llave == 0 :
   #     tope = muchos
   # else:
   #     tope = N_favoritos
   #llave = 1         COMENTE EL BLOQUE PARA EL DEBUGGING CON 1 SOLO REG. LLave dice si es el primer reg o no
    
    tope=N_favoritos+1   # SACARLO CUANDO HAYA MAS DE UN REG
     
    for i in range (1,tope):
      # si hay mensajes consulta a cada favorito
        if restantes[1] > 0:
         #   print("Restantes de OMEGA"+str(restantes))
            # arma la lista de los n favoritos ordenados por nros de exitos a partir de la matriz FAVORITOS
          #  print("voy a armar lista fav")
            lista=list()
            arma_lista_fav(1,decision,lista,N_favoritos,N_agentes)
            if not( i-1 > len(lista)):
              rr="OMEGA consulta a "+str(lista[i-2])+" con calidad "+str(Qx1)+"\n"
       #       Resp.write(rr)
      #        print ("OMEGA consulta a "+str(lista[i-2])+" con calidad "+str(Qx1))
              niveles[1,lista[i-2],id_msg, decision]=nivel
         #     T=t
              
              CONSULTAR(1, lista[i-2], decision, id_msg, niveles[1,lista[i-2],id_msg, decision], Qx1, Qy, pendientes, N_campos, restantes)
       #       print("calidad devuelta a OMEGA "+str(Qy))
              restantes[1]=restantes[1]-1
              taux=t
            
      
          
    k=0
    tmax=0 
    
    # PROCESO LISTA DE MENSAJES GENERADOS POR REGISTRO ***************************************************
    # print("tipo_mens  = ", tipo_mens, "t_entrada", t_entrada)
    m=0
    ag = 1
   #mientras haya mensajes para algun agente
    tt =0 
    while tt < 200 :
      hay = 0
      for ag in range (1,N_agentes):
        
        # veo si hay mensajes de consulta a ese ag o de respuesta que le lleguen
        for xx in range (1,N_agentes):
          
          for m in range (1,id_msg+1):
            campo=1
           
           # for campo in range (1,N_campos+1):
            for campo in range (1,73): 
              if (xx, ag, m, campo,t+tt) in tipo_mens:
                       
                if t_generac[xx, ag, m, campo,t+tt] + TIMEOUT > t+tt and tipo_mens[xx, ag, m, campo,t+tt] == 2:  # o solo > t ?? NO ES TO 
                  pendientes[ag,m,campo]=pendientes[ag,m,campo] - 1 
                else:  
                  if t_generac[xx, ag, m, campo,t+tt] + TIMEOUT > t+tt:
                    
                    if  t_entrada[xx, ag, m, campo, t] == t+tt and t_generac[xx, ag, m, campo,t+tt] + TIMEOUT > t+tt:
                      hay =1                         
                         
                      if  tipo_mens[xx, ag, m, campo,t+tt] == 1 :    # 1 - consulta 2 - Respuesta
                                  
                        # proceso consulta
                        Qaux=Q[xx,ag,m,campo]
  
                        #S[xx,m,campo]=S[xx,m,campo]+1
                        
                        CONSULTAR(xx, ag, campo, m, niveles[xx, ag, m, campo], Qaux,Qy, pendientes, N_campos, restantes)
                      else:
                        if  tipo_mens[xx, ag, m, campo, t+tt]==2 and  t_entrada[xx, ag, m, campo, t] == t+tt :
                          # prceso respuesta
                          hay =1 
                          Qaux=Q[xx,ag,m,campo]
                          RESPONDER(ag,xx,m,campo,Qy,Qaux,N_agentes,tipo_mens,MODO, restantes,t+tt)
                       
                    else:
                  
                        TIMEOUTS=TIMEOUTS+1
              campo=campo+1
      if hay ==1:
        ttt=tt+t  # ttt tiene el mayor tiempo en el que hubo mensajes
      tt=tt+1
            
      
      # para cada agente X
      # si tiene pendiente = 0 AND hay una cons para ese mens y ese campo cc y para ese agente X OR hay una consulta para un supercampo de cc y para X y ese mens
      #      X responde 
        
      
       # proceso los mensajes para OMEGA **********************************************************  
      
      
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
     
        
        while p < N_agentes+1:
         
          for r in range (1,MAXREGS+1):
            if (p,1,r,decision,t) in t_entrada and  t_entrada[p,1,r,decision,t] == t+taux and tipo_mens[p,1,r,decision,t+taux]==2:
         #     print("Hay mensaje para OMEGA desde ag" + str(p)+" para mens "+ str(r))
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
                if Q[p,1, r,decision] > Qx1:  
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
    for u in range (1,N_agentes) :
      for tiempo in range (0,t+TIMEOUT):
    
        
        if (u,1,id_msg,decision,tiempo) in tipo_mens:
       #   print (tipo_mens[u,1,id_msg,decision,tiempo],t_generac[u,1,id_msg,decision,tiempo],t_entrada[u,1,id_msg,decision, t_generac[u,1,id_msg,decision,tiempo]])
          
          
          if tipo_mens[u,1,id_msg,decision,tiempo]== 2 and  t_generac[u,1,id_msg,decision,tiempo] + TIMEOUT > t_entrada[u,1,id_msg,decision, t_generac[u,1,id_msg,decision,tiempo]] :
            print("************  NO ES T O")
            enhora=1
            print("Q es ", Qx[u,1,id_msg,decision]," calidad de OMEGA=",Qx1)
            if Qx1 < Qx[u,1,id_msg,decision]:
              ESTRICTO=1
            else:
              if Qx1- Qx[u,1,id_msg,decision] < 0.01:
                AMPLIO=1
                 
              
            NO=1
    if NO == 0:
       #   print("********ESSSSS TO") 
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
    print("*************************** leo reg ")
       
    line1=f.readline()
    line111=line1.strip() 
    id_msg=id_msg+1
  #  hora_mens[id_msg]=t
    if id_msg > MAXREGS -1 :
      break
    # cereo arreglos ******************************************************************
#    print("EXITOS A ", str(EXITOS_A),"EXITOS E ", str(EXITOS_E), "TIME OUTS ", str(TIMEOUTS))
    if id_msg < MAXREGS +1 :
      t_entrada={}
      t_generac={}
      largo_cola={}
      tipo_mens={}
      pendientes=numpy.zeros((N_agentes,MAXREGS, N_campos), dtype=int)
      Q=numpy.zeros((N_agentes,N_agentes,MAXREGS, N_campos), dtype=float)
      niveles=numpy.zeros((N_agentes, N_agentes, MAXREGS, N_campos), dtype=int)
            
    # no se cuando habria que inicializar Qx
    SALTO=999
      
      
      #  ******************************************************************************
      
  
  rr=" *****************  FIN DE EJECUCION *****************"
 # Resp.write(rr)
  print(rr)
  Resp.close() 
main()