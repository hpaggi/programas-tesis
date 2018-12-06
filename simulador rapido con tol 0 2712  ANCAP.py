# principal del sim-ulador

def CONSULTAR(X,Y,id_campo,nivel,Qx1,Qy):
     import random
     import numpy
     
# el agente X consulta al Y por el campo id_campo

     global id_msg
     global t_entrada
     global muchos
     global largo_cola
     global a
     global tipo_mens
     global t_generac
     global N_agentes
     global formado_por
     global Qx
     global N_campos
     global pendientes
     global niveles     
     global N_favoritos
     global MENSAJES_ITER
     global pregunte
     global m

     global SALTO   # el salto que da t para pasar al futuro
     SALTO=999

#  rr="Estoy en CONSULTAR  campo "+" X "+str(X)+" Y "+str(Y)+" MSg " + str(m) +" campo "+str(id_campo) + " nivel " +str(nivel)+ " Qx1"+str(Qx1)
     # rr=rr+"\n"

     # print(rr)
     #Resp.write(rr)  
     
     # 
     # si en la fila Y hay un 1 para ese mens y campo, ignorar cons
    
     
     if restantes[X]>0 or X==1: # and MODO == "I" or MODO=="S":
          # generar estructuras de que X consulta a Y +++++++++++++++++++++
          #
          #
     
     
          # print("genere la consulta X Y")           
          espera=int(random.random()*TIMEOUT)
          MENSAJES_ITER=MENSAJES_ITER+1
          tipo_mens[a+espera,X,Y,m,id_campo]=1
       #   print("TIPO en 48",X,Y,m,id_campo )
          t_generac[X,Y,m,id_campo,a+espera]=a
          t_entrada[X,Y,m,id_campo, a]= a+espera
          f=id_campo
          if (Y, m,f ) in largo_cola:
               largo_cola[Y, m, f]= largo_cola[Y, m, f] +1
          else:
               largo_cola[X, m, id_campo]= 1
          niveles[X, Y,m, id_campo]=nivel
          restantes[X]=restantes[X]-1  
     
          a=a+1          
          lista_subcampos=[]
          ccons=numpy.zeros(N_campos, dtype=int)
          if (X,Y,m,id_campo) not in S:
               S[X,Y,m,id_campo] = 0
          S[X,Y,m,id_campo]=S[X,Y,m,id_campo]+1

     # print("S es",str( S[X,Y,m,id_campo]), "X es ", str(X), "Y es ",str(Y))
          if (Y,m,id_campo) not in   largo_cola:
               largo_cola[Y,m,id_campo] = 1
          else:   
               largo_cola[Y,m,id_campo]=largo_cola[Y,m,id_campo]+1


          # nro de campos por los que consulto ************************************************************
          ncons=0

          # veo los subcampos que hay
          tot=0
          lista_subcampos=[]
          if restantes[Y] >0 :  # and MODO == "I" or MODO=="S":
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
                         if (X,Y,m,k) in Qx:
                              prob=Qx[X,Y,m,k]
                         else:
                              prob=0.5
                         if s > prob : 
                              # aniadir k a la lista de campos a consultar

                              if k not in ccons:
                                   ccons[kk]=k
                                   kk=kk+1
                                   if not (Y,m,id_campo) in pendientes:
                                        pendientes[Y,m,id_campo]=0
                                   pendientes[Y,m,id_campo]=pendientes[Y,m,id_campo] + 1   



                   
                    # Y consulta a otro por subcampo
                    fav=0
          #   print(" Y  consulta a Z. campos a consultar  ",ccons[0:20])
                    #    rr="campos a consultar  "+str(ccons[0:20])+"\n"
                    #    Resp.write(rr)
                              # ncons dice hasta cuantos campos consulto, kk dice cuantos subcampos consulto realmente
                    if kk>0: 
                         #   print("voy a ver subcampos")
                         k=0
                         while k < kk:
                              if restantes[Y] > 0  : #and MODO == "I" or MODO=="S":
                                   favor=[]
                                   p=1

                                   favor=arma_lista_fav(Y,ccons[k],favor,N_favoritos,N_agentes)
                              #  print("fav  para Y ******",Y, "campo",ccons[k],"  ", favor)
                              #  print("EXITOS FAV PARA ", Y, "=" )
                              #  for x in range (1, N_agentes):
                              #  print(FAVORITOS[Y,x ,ccons[k]], " ");
                                   rr="fav *****"+str(favor[0:10])+"\n"
          #          Resp.write(rr)

                                   p=1

                                   while  p < len(favor):  # en realidad habria que distinguir su ya se determinaron los favoritos y sino usar muchos como fin de loop
                                        Z= favor[p-1]
                                        Qz=0.0 # ojo. poner 0.0 a todas las calidades como valor inicial
                                        if restantes[Y]>0  : # and MODO == "I" or MODO=="S":
                                             if not Z == X:
                                                  nivel=nivel+1
                                                  niveles[Y,Z,m, ccons[k]]=nivel
                                                  if not (X,Y,m, ccons[k]) in S:
                                                       S[X,Y,m, ccons[k]] = 1
                                                       largo_cola[Y, m, ccons[k]] = 1
                                                  else:
                                                       S[X,Y,m, ccons[k]] = S[X,Y,m, ccons[k]] +1

                                                  largo_cola[Y, m, ccons[k]]=largo_cola[Y, m, ccons[k]]+1
                                             # S[Y,id_msg, ccons[k]] = S[Y,id_msg, ccons[k]] +1 

                                                  Qx[Y,Z,m, ccons[k]]=niveles[Y,Z,m, ccons[k]]/(1+H[Y,ccons[k]])*(1/ niveles[Y,Z,m, ccons[k]])**(PESO_NIVEL + 1)  # +++++ en realidad seria la calidad propia de Y para ese campo ++++++


                                                  rr="Genero consulta de Y =" +str(Y)+"a Z ="+str(Z)+ " msg "+str(m)+ " campo  "+ str(ccons[k]) + " cola  "+str(largo_cola[Y, m, ccons[k]])+"Qx"+str(Qx[Y,Z,m,ccons[k]])+"\n"

                                                  espera=int(random.random()*TIMEOUT) + espera

                                                  tipo_mens[a+espera,Y,Z,m,id_campo]=1
                                        #          print("TIPO en 161",Y,Z,m,id_campo )
                                                  t_generac[Y,Z,m,id_campo,a+espera]=a
                                                  MENSAJES_ITER=MENSAJES_ITER+1
                                                  t_entrada[Y,Z,m,id_campo, a]= a+espera
                                                  f=ccons[k]
                                                  if (Z, m,f ) in largo_cola:
                                                       largo_cola[Z, m, ccons[k]]= largo_cola[Z, m, ccons[k]] +1
                                                  else:
                                                       largo_cola[Z, m, ccons[k]]= 1
                                                  niveles[Y, Z,m, ccons[k]]=nivel
                                                  restantes[Y]=restantes[Y]-1
                                                  a=a+1
                                        p=p+1
                              k=k+1         
                    else:
                    #      print("no hay subcampos. Contesto")

                         # calcular Q propia usando nivel, error, etc
                         #n=niveles[X,Y,id_msg,id_campo]
                         #   CALCULO_Qy_SIMPLE(Y, id_msg, id_campo, Qy)
                         Qy=1/(1+H[Y,id_campo])
                         Qx[X,Y,m,id_campo]=Qy
                         if Qy > Qx1 and restantes[Y]>0   and MODO == "I" or MODO=="S" and restantes[Y]>0 or Qy > Qx1 and Y ==1 :

                              Qy=devuelvo_resp(Y,X,id_campo,nivel,Qy)
                    #   print("devuelvo respuesta ",Y,X,id_msg,id_campo,str(nivel),str(Qy))
                              rr="devuelvo respuesta "+"Y "+ str(Y)+"X "+str(X)+" msg "+str(m)+"campo "+str(id_campo)+ "nivel "+str(nivel)+" Qy "+str(Qy)+"\n"    
                              # Resp.write(rr)   

               else:          
                    # calcular Qy usando nivel, error, etc 
                    # CALCULO_Qy(X,Y,id_msg,id_campo,Qy)
                    #  Qyy=1
                    #  CALCULO_Qy_SIMPLE(Y,id_msg,id_campo,Qyy)
                    #  Qy=Qyy
                    Qy=1/(1+H[Y,id_campo])
                    Qx[X,Y,m,id_campo]=Qy
                    #  +++++++
                    if not Y == X:
                         nivel=nivel+ 1

               if Qy > Qx1 and restantes[Y]>0  and MODO == "I" or MODO=="S" and restantes[Y]>0 or Qy > Qx1 and Y ==1:
                    # devolver respuesta // poner en la cola de mens de entrada de Y un mens de resp con hora 100 mas que t
          #        print("VOY A devuelvo respuesta ",Y,X,id_msg,id_campo,str(nivel),str(Qy))
                    # print("voy a devolver resp Qy",Qy)
                    Qy=devuelvo_resp(Y,X,id_campo,nivel,Qy)
                    Qx[X,Y,m,id_campo]=Qy # tomo la calidad y no me fijo si es un T O 
          #   print  ("devuelvo resp por ncons =0", "X",X,"Y",Y,"campo",id_campo,"Qy",Qy)
                    rr="devuelvo respuesta "+str(Y)+str(X)+str(m)+str(id_campo)+str(nivel)+str(Qy)+"\n"        
               #  Resp.write(rr)
     else: 
          return(Qy)

     return(Qy)
   
     
#************************************************************************************

def CALCULO_Qy(X,Y,m,id_campo,Qy):
     import numpy
     global id_msg


     # calidad  de Y cuando X responde a Y
     # Max=numpy.amax(Q,axis=1)
     Max=0
     Min=0
     global EXITOS_E
     global EXITOS_A
     global TIMEOUTS

     for i in range (1, N_agentes):
          #  print(niveles)
          if (i,Y,m,id_campo) in niveles:
               pass
          else:
               niveles[i,Y,m,id_campo]=1
          if (i,Y,m,id_campo) not in Q:  
               Q[i,Y,m,id_campo]=0
          if Q[i,Y,m,id_campo]/(niveles[i,Y,m,id_campo]**PESO_NIVEL) > Max:

               Max= Q[i,Y,m,id_campo]/(niveles[i,Y,m,id_campo]**PESO_NIVEL)
     # print("calculo Q. cal max recibida=",Max)

     for i in range (1, N_agentes):
          if Q[i,Y,m,id_campo]/(niveles[i,Y,m,id_campo]**PESO_NIVEL) < Min:
               Min = Q[i,Y,m,id_campo]/(niveles[i,Y,m,id_campo]**PESO_NIVEL)     

     #print("calculo Q. cal MIN recibida=",Min)
     #n=niveles[X,Y,id_msg,id_campo]
     #Qx[X,Y,id_msg,id_campo]=1/(1+H[Y,id_campo])*(1/n**PESO_NIVEL) 
     #Qx[X,Y,id_msg,id_campo]= CALCULO_Qy(X, id_msg, id_campo, Qx1) # hay que calcular la calidad de X recursivamente
     V=Max-Min
     q=1/(1+V)*Max
     if X== 1:
          S[X,Y,m,id_campo]=1  
     if (Y,X,m,id_campo) not in T:
          T[Y,X,m,id_campo]=1
     R=T[Y,X,m,id_campo]**2/S[X,Y,m,id_campo]

     Qtecho=1/(1+H[Y,id_campo])
     if R==0:
     #  n=niveles[X,Y,id_msg,id_campo]
          Qy1=1/(1+H[Y,id_campo])
          Qx[X,Y,m,id_campo]=Qy1

          Q[X,Y,m,id_campo]=Qy1

          return(Qy1)
     Qy1=max(Qtecho,q)**((PESO_NIVEL+1)/R)
     Q[X,Y,m,id_campo]=Qy1
# cuando el que recibe es OMEGA ya calculo si es un exito  
     if Y == 1 :
          if T[Y,X,m,id_campo]==0:  #X responde a Y o sea Y consulta a X
               TIMEOUTS=TIMEOUTS+1
          else:  
               if (X,Y,m,id_campo) not in Qx:
                    Qx[X,Y,m,id_campo]=0
               if Qy1 > Qx[X,Y,m,id_campo]:
                    ES_EXITO_E=1
               #EXITOS_E=EXITOS_E+1
               else:
                    if Qy1 == Qx[X,Y,m,id_campo]:
                         ES_EXITO_A=1
                    # EXITOS_A=EXITOS_A+1      
     # print("Calculo Qy="+str(Qy)+ " id msg "+" msg "+str(id_msg)+ " id campo " + str(id_campo))
     return(Qy1)
#************************************************************************************
def CALCULO_Qy_SIMPLE(Y,m,id_campo,Qy):
     import numpy
     global id_msg
     # calidad  de Y cuando Y NO CONSULTA A NADIE MAS

     # Max=numpy.amax(Q,axis=1)

     global EXITOS_E
     global EXITOS_A


     global TIMEOUTS

     # print("calculo Q. cal simple")

     # n=niveles[X,Y,id_msg,id_campo]

     Qy=1/(1+H[Y,id_campo])
     Qx[X,Y,m,id_campo]=Qy 
     Q[X,Y,m,id_campo]=Qy
#  print("Calculo Qy  SIMPLE ="+str(Qy)+ " id msg "+str(id_msg)+ " id campo " + str(id_campo))
     return(Qy)
#****************************************************************************************************************************************

def BUSCOPADRES(Y, m, id_campo, lista): # Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
     global tipo_mens
     global id_msg
     lista=[]
     if Y==1:
          lista=lista.append(1)
     # print ("busco padres de OMEGA")
          return(lista)
     for ag in range (1,N_agentes):
          if ((a,ag,Y,m,id_campo) in   tipo_mens) and tipo_mens[a,ag,Y,m,id_campo]=="1":
               lista.append(ag)
#  print("Busco padres"+ "Y"+ str(Y)+" msg" +str(m)+ " campo "+str(id_campo)+"lista:")
#  print(lista)
     return(lista)
#*************************************************************************************


def devuelvo_resp(X,Y, id_campo,nivel,Qy2):
     # X devuelve respuesta a Y
     import random
     global id_msg,a
     Qy=0
     lista=[]
     global SALTO
     global Resp
     global RESPONDE_OMEGA
     global respuestas
     global MODO
     global m
     global RESTANTES_ANT_REG, RESTANTES_ANT
     global iteracion
     global t_entrada, t_generac, tipo_mens, largo_cola, niveles, pendientes, restantes, MENSAJES_ITER
     #  print("estoy en devuelvo resp  X="+str(X)+" Y= " +str(Y)+" id_campo "+str(id_campo))
     espera=int(100*random.random())
     if restantes[X]>0 or X == 1 : #  and MODO == "I" or MODO=="S":
          if espera < SALTO:
               SALTO=espera    
          t_entrada[X, Y, m, id_campo,a]= a +  espera
          t_generac[X, Y, m, id_campo, a+espera]= a 
          MENSAJES_ITER+MENSAJES_ITER+1

          tipo_mens[a+espera,X,Y, m, id_campo]=2
      #    print("TIPO en 355",X,Y,m,id_campo )
          if not (Y, m, id_campo) in largo_cola:
               largo_cola[Y, m, id_campo]=0
          largo_cola[Y, m, id_campo]= largo_cola[Y, m, id_campo] +1
          niveles[X,Y,m, id_campo]=nivel+1

          Q[X,Y,m, id_campo]=Qx[X,Y,m, id_campo]=Qy2   # la respuesta de la cons de X a Y es Qx   
          pendientes[Y,m,id_campo]=pendientes[Y,m,id_campo] - 1

          restantes[X]=restantes[X]-1
          a=a+1

          if pendientes[Y,m,id_campo] < 1 or ES_TO(Y,m,id_campo):

               # Y debe devolver la respuesta a quien lo consulto
               #  Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres
               lista=[]
               lista=BUSCOPADRES(Y,m, id_campo, lista)
               #   genera una respuesta a partir de todas las calidades recibidas    Esa respuesta es Qy1

               # Tomo todos los pesos iguales, asi que solo hago el promedio de calidades de las respuestas
               Qy1=0
               cuenta=0
               for i in range (1,N_agentes):
                    if (i,Y,m,id_campo) in Q:
                         if Q[i,Y,m,id_campo] > 0:
                              Qy1=Q[i,Y,m,id_campo] + Qy1
                              cuenta=cuenta+1
               if cuenta == 0:
                    Qy1=0
               else:
                    Qy1=Qy1/cuenta
               Q[X,Y,m,id_campo]=Qy1
               suma=0
               for i in range (0,N_agentes):
                    suma=suma+restantes[i]      
               if Y == 1:
                    TABLA_CALIDADES_FREC[iteracion,int(Qy1*100)]=TABLA_CALIDADES_FREC[iteracion,int(Qy1*100)]+1
                    TABLA_CALIDADES_MENS[iteracion,int(Qy1*100)]=  RESTANTES_ANT_REG -suma
                    RESTANTES_ANT_REG= suma     
               #  print(TABLA_CALIDADES_MENS[iteracion,int(Qy1*100)])

          #   print(TABLA_CALIDADES[iteracion,int(Qy1*100)], Qy1)
     #   print("devuelvo resp promedio a los padres",Qy1)


               # Qy1=0.967890         
               # genera un mensaje para cada padre de Respuesta


               RESPONDE_OMEGA=0 
               if Y == 1:

                    Qy1=RESPUESTA_OMEGA (1,1,m, decision,Qx,Qy,N_agentes,MODO)
               # print("**** respuesta de OMEGA al msg ", str(m), "calidad",str(Qy1))
                    RESPONDE_OMEGA=1
               else:
                    RESPONDO_PADRES(Y,m,id_campo, lista, Qy1,nivel)
     #   print("Responde "+str(X) + " a " +str (Y)+ " msg "+str(id_msg)+" campo "+str(id_campo)+ " calidad "+ str(Qy))
          rr="Responde "+str(X) + " a " +str (Y)+ " msg "+str(m)+" campo "+str(id_campo)+ " calidad "+ str(Qy1)
     #    Resp.write(rr)
     return(Qy1)
#************************************************************************************
def ES_TO(Y,id_campo):
     global id_msg
     global t_entrada, t_generac, tipo_mens, largo_cola, niveles, pendientes, restantes
     # ES T O si ninguno de los consultados por Y para id_msg e id_campo contesto
     maxt=0
     for i in range (1,N_agentes):
          for j in range(0,t):
               if  tipo_mens[j,i,Y,m,id_campo] == 2 and t_generac[i,Y,m,id_campo,j] + TIMEOUT > t_entrada[i,Y,m,id_campo, t_generac[i,Y,m,decision,j]] :
                    return False
               else:
                    if t_generac[i,Y,m,id_campo,j] + TIMEOUT < t_entrada[i,Y,m,id_campo, t_generac[i,Y,m,decision,j]] :
                         TO_MSG[i,Y]=TO_MSG[i,Y]+1

     return True

#***************************************************************************************
def RESPUESTA_OMEGA(X,Y,m,id_campo,Qx,Qy,N_agentes, MODO):
     global id_msg

     global SALTO
     global t_entrada
     global line111
     global TIMEOUTS
     global line111
     global t_entrada, t_generac, tipo_mens, largo_cola, niveles, pendientes, restantes
                         # hacer fusion de todas las respuestas
                         # LAS respuestas estan en respuestas[]

                         # Supongo que en respuess[X,X] esta la respuesta propia

                         # Calcular respuesta propia
     import random

     partes = line111.split(';') 
     Qy1=0
     R=partes[72] # en R va la respuesta del juego de datos

     aux=random.random()
     if aux>0.95:
          if R == "Yes":
               respuestas[X,Y,m,id_campo]= 1
          else:
               respuestas[X,Y,m,id_campo]= 0

     else:
          if R == "Yes":
               # pongo valores cruzados el 5% de las veces
               respuestas[X,Y,m,id_campo]= 0
          else:
               respuestas[X,Y,m,id_campo]= 1

     # fusion de los resultados
     aux=0
     p=0
     for j in range(1,N_agentes):
          if (X,j,m,id_campo) in respuestas:
               aux=aux+respuestas[X,j,m,id_campo]
               p=p+1
     aux=int(aux/p)

     # CALCULO_Qy(X,Y,id_msg,id_campo,Qy)
     Qy1=CALCULO_Qy(1,1,m,id_campo,Qy)


     if   (X,Y,m,id_campo) not in Qx:
          Qx[X,Y,m,id_campo]=Qy1
     Qx1=Qx[X,Y,m,id_campo]
     Q[X,Y,m,id_campo]=Qx1

     # es time out si ningun mensaje llega a omega a tiempo. O sea si el t_entrada mayor + TIMEOUT < t
     ymax=1
     maxt=0

     p=1 

     for (j,i,p,m,id_campo) in tipo_mens:
          if p==1:
               if  t_entrada [i,1,m,id_campo,t_generac[i,1,m,id_campo,j]] > maxt and tipo_mens[j,i,1,m,id_campo] == 2:
     #     print(t_entrada,"t es", str(t))
                    maxt= t_entrada [i,1,m,id_campo,t_generac[i,1,m,id_campo,j]]
                    ymax= i # que hora le pongo??????+++++++++ ojo, que considero tooodas las horas

     # if t_generac[ymax,1,id_msg,decision,maxt] + TIMEOUT < t_entrada[ymax,1,id_msg,decision, t_generac[ymax,1,id_msg,decision,maxt]]:
     #   TIMEOUTS=TIMEOUTS+1
     # else:
     #   FAVORITOS[ymax,1, id_campo]=FAVORITOS[ymax, 1, id_campo]+1

     return(Qy1)
#*****************************************************************************************************************************************
def RESPONDO_PADRES(Y,m,id_campo, lista, Qy1,nivel):
     # print ("****Respondo a los padres de Y "+str(Y)+ " campo "+ str(id_campo)+" calidad "+ str(Qy1))
     
     global id_msg
     
     for i in range(0,len(lista)):
          Qy1=devuelvo_resp(Y,lista[i],id_campo,nivel,Qy1)



     return(Qy1)



# ***********************************************************************************
def RESPONDER(X,Y,id_campo,Qy,N_agentes,MODO, hora):
     global id_msg,a
     # X envia respuesta a Y
     global t_entrada, t_generac, tipo_mens, largo_cola, niveles, pendientes, restantes, MENSAJES_ITER, MAXMENS
     global SALTO
     global t_entrada
     import random 
     global Qx
     global m
     #for i in range (1,largo_cola[X, id_msg, id_campo]):
     if (X,Y,m,id_campo,hora) in tipo_mens:
      #    if tipo_mens[hora,X,Y,m,id_campo]==2 and t_entrada [X,Y,m,id_campo,t_generac[Y,X,m,id_campo,hora] ] == hora or tipo_mens[hora,X,Y,m,id_campo]==1 and t_entrada [X,Y,m,id_campo,t_generac[Y,X,m,id_campo,hora] ] > t_generac[Y,X,m,id_campo,hora] + TIMEOUT:
          if tipo_mens[hora,X,Y,m,id_campo]==2 and t_entrada [X,Y,m,id_campo,t_generac[X,Y,m,id_campo,hora] ] == hora or tipo_mens[hora,X,Y,m,id_campo]==1 and t_entrada [X,Y,m,id_campo,t_generac[X,Y,m,id_campo,hora] ] > t_generac[X,Y,m,id_campo,hora] + TIMEOUT:
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
                         respuestas[X,Y,m,id_campo]= 1
                    else:
                         respuestas[X,Y,m,id_campo]= 0

               else:
                    if R == "Yes":
                         # pongo valores cruzados el 5% de las veces
                         respuestas[X,Y,m,id_campo]= 0
                    else:
                         respuestas[X,Y,m,id_campo]= 1

               # fusion de los resultados

               aux=0
               p=0
     #    print("RESPONDER  valor de entrADA ",R, " resp ", str(respuestas[X,Y,m,id_campo]))

               for j in range(1,N_agentes):
                    if (X,j,m,id_campo) in respuestas:
                         aux=aux+respuestas[X,j,m,id_campo]
                         p=p+1
               aux=round(aux/p) # aux tiene la respuesta fusionada

               #s=S[X,id_msg,id_campo]
               #nt=T[Y,X,id_msg,id_campo]
               # Qx1=nivel/(1+0.05)*(1/(nivel **  PESO_NIVEL))
               #Calculo Q  

               Qx1= 1/(1+H[X,id_campo])      
               a = restantes [X]

     #   if a > 0   and MODO == "I" or MODO=="S":
               if a > 0:  # responde si teiene mensajes, en cualquiera de los dos modos
                    if Qx1 > Qy and MODO == "I" or MODO == "S" :  # cuando la calidad es mayor que la del que consulta, responde
                         espera=int(random.random()*TIMEOUT)
                         if espera < SALTO:
                              SALTO=espera


                         Qx[X,Y,m,id_campo]=Qx1
                         if (Y,X,m, id_campo) in T:
                              T[Y,X,m, id_campo]=T[Y,X,m, id_campo]+1
                         else:
                              T[Y,X,m, id_campo]=1
                         t_entrada[X,Y,m,id_campo,a]=a+espera 
                         MENSAJES_ITER=MENSAJES_ITER+1
                         t_generac[X,Y,m,id_campo,a+espera]=a
                      #   tipo_mens[a+espera,X,Y,m,id_campo]=2 
                    #     print("TIPO en 594",X,Y,m,id_campo )
                         nivel=niveles[X,Y,m, id_campo]=niveles[X,Y,m,id_campo]+1
                         a=a+1
                         if t_generac[X,Y,m,id_campo,hora] + TIMEOUT > t_entrada[X,Y,m,decision, t_generac[X,Y,m,decision,hora]] : # no es t o


                              largo_cola[Y,m,id_campo]=largo_cola[Y,m,id_campo]-1
                              pendientes[Y,m,id_campo]=pendientes[Y,m,id_campo]-1
                              FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1

                         else:
                              TO_MSG[X,Y]= TO_MSG[X,Y]+1
                         if pendientes[Y,m,id_campo] < 1:
                                        # Y debe devolver la respuesta a quien lo consulto
                                        # a- BUSCOPADRES(Y,id_msg,id_campo, lista) Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres

                              lista=[]        
                              lista1=BUSCOPADRES(Y,m,id_campo, lista)
                              if len(lista1)==0:
                                   lista=[1]   
                              else:
                                   lista=lista1
                              # b- genera una respuesta a partir de todas las calidades recibidas ++++
                              # X manda resp a Y entonces para calcular calidad de Y deben haber respondido todos o ser time out de la consulta de Y a X

                              if pendientes[Y,m,id_campo]<1 or TIMEOUT < espera :      

          #          print(" voy a calcular Qy compleja")
                                   Qy=CALCULO_Qy(X,Y,m,id_campo,Qy)   # OJO CALCULAR QY solo cuando haya pasado el timeout de Y o cuando respondieron todos
          #         print(" Qy compleja es ", Qy)                                

                              z=0
                    #   GENERO_RESP(Y,id_msg,id_campo, lista, Qy)
                              for z in lista:
                                   if restantes[Y]>0 or Y == 1:
                                        espera=int(random.random()*TIMEOUT)
                                        t_entrada[Y,z,m,id_campo,a]=a+espera
                                        MENSAJES_ITER=MENSAJES_ITER+1
                                        t_generac[Y,z,m,id_campo,a+espera]=a
                                        tipo_mens[a+espera,Y,z,m,id_campo]=2
                                 #       print("TIPO en 633",Y,z,m,id_campo )
                                        a=a+1
                                        largo_cola[z,m, id_campo]=largo_cola[z,m, id_campo]-1
                                        FAVORITOS[Y,z,id_campo]=FAVORITOS[Y,z,id_campo]+1
                                        pendientes[z,m,id_campo]=pendientes[z,m,id_campo]-1   
                                        Qx[z,Y,m,id_campo]=Qy
                                        Q[z,Y,m,id_campo]=Qy
                                        restantes[Y]=restantes[Y-1]                
                              # c- genera un mensaje para cada padre de Respuesta ++++ 
                              # para cada elem i de lista:
                              #    genero mens de resp de Y a i para ese id_msg, id_campo y Qy

                    #    print("QYYYYY",Qy)
                              RESPONDO_PADRES(Y,m,id_campo, lista, Qy,nivel)

                    #    restantes[Y]=restantes[Y]-1

                         if  t_generac[Y,X,m,id_campo,hora] + TIMEOUT > t_entrada[Y,X,m,id_campo, t_generac[Y,X,m,id_campo,hora]]:
                              # actualizar favoritos de Y 
                              FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                              pass
                         else:
                              if Y == 1 :  # T O es cuando el sistema no contesta a tiempo, cuando NADIE contesta a tiempo
                                   if max(t_generac[X,1,m,id_campo],axis=0) +TIMEOUT < a:                 
                                        TIMEOUTS = TIMEOUTS +1

                    else:
                         if MODO == "I":
                              PTEMPLE=(1-Qy)/(MAXMENS-restantes[X])
                              a1=random.random()
                              if a1 > PTEMPLE:
                                   if restantes[X]>0  or X == 1:
                                        espera=int(random.random()*TIMEOUT)
                                        if espera < SALTO:
                                             SALTO=espera
                                        if  (Y,X, m, id_campo) in T:
                                             T[Y,X, m, id_campo]=T[Y,X,m, id_campo]+1
                                        else:
                                             T[Y,X,m, id_campo]=1
                                        t_entrada[X,Y,m,id_campo,a]=a+espera
                                        t_generac[X,Y,m,id_campo,t+espera]=a
                                        print ("genero resp de X", X, "a Y",Y, "mens ", m, "campo",id_campo)
                                        MENSAJES_ITER=MENSAJES_ITER+1
                                        tipo_mens[a+espera,X,Y,m,id_campo]=2
                                  #      print("TIPO en 678",X,Y,m,id_campo )
                                        nivel=niveles[X,Y,m,id_campo]=niveles[X,Y,m,id_campo]+1
                                        largo_cola[Y,m, id_campo]=largo_cola[Y,m, id_campo]+1
                                        FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
                                        pendientes[Y,m,id_campo]=pendientes[Y,m,id_campo]-1
                                        a=a+1
                                        if pendientes[Y,m,id_campo] < 1:
                                             # Y debe devolver la respuesta a quien lo consulto
                                             lista=[]
                                             lista=BUSCOPADRES(Y,m,id_campo, lista) #Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
                                             # b- genera una respuesta a partir de todas las calidades recibidas 
                                             # c- genera un mensaje para cada padre de Respuesta 
                                             print("respondo a padres de ", Y, "por mens=",m, "campo ",id_campo)
                                             RESPONDO_PADRES(Y,m,id_campo, lista, Qy,nivel)
                         if t_generac[X,Y,m,id_campo,hora] + TIMEOUT > t_entrada[X,Y,m,id_campo, t_generac[X,Y,m,id_campo,hora]]:

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
                         respuestas[X,Y,m,id_campo]= 1
                    else:
                         respuestas[X,Y,m,id_campo]= 0

               else:
                    if R == "Yes":
                         # pongo valores cruzados el 5% de las veces
                         respuestas[X,Y,m,id_campo]= 0
                    else:
                         respuestas[X,Y,m,id_campo]= 1

               # fusion de los resultados

               aux=0
               p=0
     #       print("RESPONDER  valor de entrADA ",R, " resp ", str(respuestas[X,Y,id_msg,id_campo]))

               for j in range(1,N_agentes):
                    if (X,j,m,id_campo) in respuestas:
                         aux=aux+respuestas[X,j,m,id_campo]
                         p=p+1
               aux=int(aux/p)

               #s=S[X,id_msg,id_campo]
               #nt=T[Y,X,id_msg,id_campo]
               # Qx1=nivel/(1+0.05)*(1/(nivel **  PESO_NIVEL))
               #Calculo Q  

               Qx1= 1/(1+H[X,id_campo])      
               a = restantes [X]

          #  if a > 0   and MODO == "I" or MODO=="S":
               if a > 0 : #   and MODO == "I" or MODO=="S":   
                    if Qx1 > Qy and MODO == "I" or MODO == "S" :  # cuando la calidad es mayor que la del que consulta, responde
                         espera=int(random.random()*TIMEOUT)
                         if espera < SALTO:
                              SALTO=espera


                         Qx[X,Y,m,id_campo]=Qx1
                         T[Y,X,m, id_campo]=T[Y,X,m, id_campo]+1
                         t_entrada[X,Y,m,id_campo,a]=a+espera 
                         MENSAJES_ITER=MENSAJES_ITER+1
                         t_generac[X,Y,m,id_campo,a+espera]=a
                         tipo_mens[a+espera,X,Y,m,id_campo]=2 
                     #    print("TIPO en 763",X,Y,m,id_campo )
                         nivel=niveles[X,Y,m,id_campo]=niveles[X,Y,m,id_campo]+1
                         if t_generac[X,Y,m,id_campo,hora] + TIMEOUT > t_entrada[X,Y,m,decision, t_generac[X,Y,m,decision,hora]] : # no es t o


                              largo_cola[Y,m,id_campo]=largo_cola[Y,m,id_campo]-1
                              pendientes[Y,m,id_campo]=pendientes[Y,m,id_campo]-1
                              FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1

                         else:
                              TO_MSG[X,Y]=TO_MSG[X,Y]+1
                         if pendientes[Y,m,id_campo] < 1:
                                        # Y debe devolver la respuesta a quien lo consulto
                                        # a- BUSCOPADRES(Y,id_msg,id_campo, lista) Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres


                              lista=BUSCOPADRES(Y,m,id_campo, lista)
                              # b- genera una respuesta a partir de todas las calidades recibidas ++++
                              # X manda resp a Y entonces para calcular calidad de Y deben haber respondido todos o ser time out de la consulta de Y a X

                              if pendientes[Y,m,id_campo]<1 or TIMEOUT < espera :      

          #          print(" voy a calcular Qy compleja")
                                   Qy=CALCULO_Qy(X,Y,m,id_campo,Qy)   # OJO CALCULAR QY solo cuando haya pasado el timeout de Y o cuando respondieron todos
          #         print(" Qy compleja es ", Qy)                                

          #       GENERO_RESP(Y,id_msg,id_campo, lista, Qy)
                              for z in lista: 
                                   if restantes[Y]> 0 or Y==1:
                                        espera=int(random.random()*TIMEOUT)
                                        t_entrada[Y,z,m,id_campo,a]=a+espera
                                        t_generac[Y,z,m,id_campo,a+espera]=a
                                        MENSAJES_ITER=MENSAJES_ITER+1
                                        tipo_mens[a+espera,Y,z,m,id_campo]=2
                                      #  print("TIPO en 7978",Y,z,m,id_campo )
                                        largo_cola[z,m, id_campo]=largo_cola[z,m, id_campo]-1
                                        FAVORITOS[Y,z,id_campo]=FAVORITOS[Y,z,id_campo]+1
                                        pendientes[z,m,id_campo]=pendientes[z,m,id_campo]-1   
                                        Qx[z,Y,m,id_campo]=Qy
                                        Q[z,Y,m,id_campo]=Qy
                                        restantes[Y]=restantes[Y-1]


                              # c- genera un mensaje para cada padre de Respuesta ++++ 
                              # para cada elem i de lista:
                              #    genero mens de resp de Y a i para ese id_msg, id_campo y Qy

               #      print("RESPONDO OADRES DE Y con q ",Qy)
                              RESPONDO_PADRES(Y,m,id_campo, lista, Qy,nivel)

                    #    restantes[Y]=restantes[Y]-1

                         if  t_generac[Y,X,m,id_campo,hora] + TIMEOUT > t_entrada[Y,X,m,id_campo, t_generac[Y,X,m,id_campo,hora]]:
                              # actualizar favoritos de Y 
                              FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                              pass
                         else:
                              if Y == 1 :  # T O es cuando el sistema no contesta a tiempo, cuando NADIE contesta a tiempo
                                   if max(t_generac[X,1,m,id_campo],axis=0) +TIMEOUT < a:                 
                                        TIMEOUTS = TIMEOUTS +1
                                        TO_MSG[X,1]=TO_MSG[X,1]+1 
                    else:
                         if MODO == "I":
                              PTEMPLE=(1-Qy)*(MAXREGS-restantes[X])/100
                              a=random.random()
                              if a > PTEMPLE:
                                   if restantes[X]>0 or X == 1 :
                                        espera=int(random.random()*TIMEOUT)
                                        if espera < SALTO:
                                             SALTO=espera
                                             T[Y,X, m, id_campo]=T[Y,X,m, id_campo]+1
                                        t_entrada[X,Y,m,id_campo,a]=a+espera
                                        MENSAJES_ITER=MENSAJES_ITER+1
                                        t_generac[X,Y,m,id_campo,t+espera]=a
                                        tipo_mens[a+espera,X,Y,m,id_campo]=2
                                   #     print("TIPO en 838",X,Y,m,id_campo )
                                        nivel=niveles[X,Y,m,id_campo]=niveles[X,Y,m,id_campo]+1
                                        largo_cola[Y,m, id_campo]=largo_cola[Y,m, id_campo]+1
                                        FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
                                        pendientes[Y,m,id_campo]=pendientes[Y,m,id_campo]-1
                                        if pendientes[Y,m,id_campo] < 1:
                                             # Y debe devolver la respuesta a quien lo consulto
                                             lista=[]
                                             lista=BUSCOPADRES(Y,m,id_campo, lista) #Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
                                             # b- genera una respuesta a partir de todas las calidades recibidas 
                                             # c- genera un mensaje para cada padre de Respuesta 

                                             RESPONDO_PADRES(Y,m,id_campo, lista, Qy,nivel)
                         if t_generac[X,Y,m,id_campo,hora] + TIMEOUT > t_entrada[X,Y,m,id_campo, t_generac[X,Y,m,id_campo,hora]]:
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
                         respuestas[X,Y,m,id_campo]= 1
                    else:
                         respuestas[X,Y,m,id_campo]= 0

               else:
                    if R == "Yes":
                         # pongo valores cruzados el 5% de las veces
                         respuestas[X,Y,m,id_campo]= 0
                    else:
                         respuestas[X,Y,m,id_campo]= 1

               # fusion de los resultados

               aux=0
               p=0
     #       print("RESPONDER  valor de entrADA ",R, " resp ", str(respuestas[X,Y,id_msg,id_campo]))

               for j in range(1,N_agentes):
                    if (X,j,m,id_campo) in respuestas:
                         aux=aux+respuestas[X,j,m,id_campo]
                         p=p+1
               aux=int(aux/p)

               #s=S[X,id_msg,id_campo]
               #nt=T[Y,X,id_msg,id_campo]
               # Qx1=nivel/(1+0.05)*(1/(nivel **  PESO_NIVEL))
               #Calculo Q  

               Qx1= 1/(1+H[X,id_campo])      
               a = restantes [X]

               if a > 0  :                     # and MODO == "I" or MODO=="S":
                    if Qx1 > Qy or MODO == "S" :  # cuando la calidad es mayor que la del que consulta, responde
                         espera=int(random.random()*TIMEOUT)
                         if espera < SALTO:
                              SALTO=espera


                         Qx[X,Y,m,id_campo]=Qx1
                         T[Y,X,m, id_campo]=T[Y,X,m, id_campo]+1
                         t_entrada[X,Y,m,id_campo,a]=a+espera 
                         MeNSAJES_ITER=MENSAJES_ITER+1
                         t_generac[X,Y,m,id_campo,a+espera]=a
                         tipo_mens[a+espera,X,Y,m,id_campo]=2 
                    #     print("TIPO en 919",X,Y,m,id_campo )
                         nivel=niveles[X,Y,m,id_campo]=niveles[X,Y,m,id_campo]+1
                         if t_generac[X,Y,m,id_campo,hora] + TIMEOUT > t_entrada[X,Y,m,decision, t_generac[X,Y,m,decision,hora]] : # no es t o


                              largo_cola[Y,m,id_campo]=largo_cola[Y,m,id_campo]-1
                              pendientes[Y,m,id_campo]=pendientes[Y,m,id_campo]-1
                              FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
                         else:
                              TO_MSG[X,Y]=TO_MSG[X,Y]+1
                         if pendientes[Y,m,id_campo] < 1:
                                        # Y debe devolver la respuesta a quien lo consulto
                                        # a- BUSCOPADRES(Y,id_msg,id_campo, lista) Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres


                              lista=BUSCOPADRES(Y,m,id_campo, lista)
                              # b- genera una respuesta a partir de todas las calidades recibidas ++++
                              # X manda resp a Y entonces para calcular calidad de Y deben haber respondido todos o ser time out de la consulta de Y a X

                              if pendientes[Y,m,id_campo]<1 or TIMEOUT < espera :      

          #          print(" voy a calcular Qy compleja")
                                   Qy=CALCULO_Qy(X,Y,m,id_campo,Qy)   # OJO CALCULAR QY solo cuando haya pasado el timeout de Y o cuando respondieron todos
          #         print(" Qy compleja es ", Qy)                                

          #       GENERO_RESP(Y,id_msg,id_campo, lista, Qy)
                              # c- genera un mensaje para cada padre de Respuesta ++++ 
                              # para cada elem i de lista:
                              #    genero mens de resp de Y a i para ese id_msg, id_campo y Qy
                              for z in lista:
                                   if restantes[Y]>0 or Y == 1:
                                        espera=int(random.random()*TIMEOUT)
                                        t_entrada[Y,z,m,id_campo,a]=a+espera
                                        t_generac[Y,z,m,id_campo,a+espera]=a
                                        MENSAJES_ITER=MENSAJES_ITER+1
                                        tipo_mens[a+espera,Y,z,m,id_campo]=2
                                  #      print("TIPO en 955",X,Y,m,id_campo )
                                        largo_cola[z,m, id_campo]=largo_cola[z,m, id_campo]-1
                                        FAVORITOS[Y,z,id_campo]=FAVORITOS[Y,z,id_campo]+1
                                        pendientes[z,m,id_campo]=pendientes[z,m,id_campo]-1   
                                        Qx[z,Y,m,id_campo]=Qy
                                        Q[z,Y,m,id_campo]=Qy
                                        restantes[Y]=restantes[Y-1]                

                    #    print("RESPONDO PADRES Y CON q",Qy)
                              RESPONDO_PADRES(Y,m,id_campo, lista, Qy,nivel)

                    #    restantes[Y]=restantes[Y]-1

                         if  t_generac[Y,X,m,id_campo,hora] + TIMEOUT > t_entrada[Y,X,m,id_campo, t_generac[Y,X,m,id_campo,hora]]:
                              # actualizar favoritos de Y 
                              FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                              pass
                         else:
                              if Y == 1 :  # T O es cuando el sistema no contesta a tiempo, cuando NADIE contesta a tiempo
                                   if max(t_generac[X,1,m,id_campo],axis=0) +TIMEOUT < t:                 
                                        TIMEOUTS = TIMEOUTS +1
                                        TO_REG[X,1]=TO_REG[X,1]+1

                    else:
                         if MODO == "I":
                              PTEMPLE=(1-Qy)*(MAXREGS-restantes[X])/100
                              a=random.random()
                              if a > PTEMPLE:
                                   if restantes[X]>0  or X == 1:
                                        espera=int(random.random()*TIMEOUT)
                                        if espera < SALTO:
                                             SALTO=espera
                                             T[Y,X, m, id_campo]=T[Y,X,m, id_campo]+1
                                        t_entrada[X,Y,m,id_campo,a]=a+espera
                                        MENSAJES_ITER=MENSAJES_ITER+1
                                        t_generac[X,Y,m,id_campo,a+espera]=a
                                        tipo_mens[a+espera,X,Y,m,id_campo]=2
                                   #     print("TIPO en 991",X,Y,m,id_campo )
                                        nivel=niveles[X,Y,m,id_campo]=niveles[X,Y,m,id_campo]+1
                                        largo_cola[Y,m, id_campo]=largo_cola[Y,m, id_campo]+1
                                        FAVORITOS[Y,X,id_campo]=FAVORITOS[Y,X,id_campo]+1
                                        pendientes[Y,m,id_campo]=pendientes[Y,m,id_campo]-1
                                        if pendientes[Y,m,id_campo] < 1:
                                             # Y debe devolver la respuesta a quien lo consulto
                                             lista=[]
                                             lista=BUSCOPADRES(Y,m,id_campo, lista) #Busca en  la cola de entrada de Y un mens de C con ese id msg y id campo y en lista da la lista de padres (de ag que consultaron)
                                             # b- genera una respuesta a partir de todas las calidades recibidas 
                                             # c- genera un mensaje para cada padre de Respuesta 

                                             RESPONDO_PADRES(Y,m,id_campo, lista, Qy,nivel)
                         if t_generac[X,Y,m, id_campo,hora] + TIMEOUT > t_entrada[X,Y,m,id_campo, t_generac[X,Y,m,id_campo,hora]]:
                                   # actualizar favoritos de Y
                              FAVORITOS[Y,X, id_campo]=FAVORITOS[Y, X, id_campo]+1
                         else:
                              TO_REG[Y,X]=TO_REG[Y,X]+1
                         #rr="++++++++++++++++++++++++++++++++++respondo   ++++++++++++++++++++++++++++++++++++++  "  
                         #       print("+++++++++++++++++++++++++++++++++++++++++++       respondo   ++++++++++++++++++++++++++  ")
                         #      Resp.write(rr)

          else:
               if t_entrada [X,Y,m,id_campo,t_generac[Y,X,m,id_campo,hora] ] > t_generac[X,Y,m,id_campo,hora] + TIMEOUT:
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
     g=0
     l=[]
     if MODO=="S":
          # while kk == 0: 
          kk=int(random.random()*N_agentes)+1
          c1=list(range(1,N_agentes+1))
          l= random.sample(c1, kk)
          if x in l:
               l.remove(x)
          if 0 in l:
               l.remove(0)
          if 1 in l:
               l.remove(1)               
          l1=l
     else:
          for ii in range(2,N_agentes+1):
               if FAVORITOS[x,ii,c] >0 :

                    if TO_MSG[x,ii]>TOLERANCIA:
                         FAVORITOS[x,ii,c]=0
                    else:
                         if l==[] or ii not in l:
                              l.append(ii)
                              kk=kk+1


          for ii in range(0,kk):
               # if ii< kk:
               for pp in range (ii+1,kk):
                    if FAVORITOS[x,l[ii],c] < FAVORITOS[x,l[pp],c]:

                         aux=l[ii]
                         l[ii]=l[pp]
                         l[pp]=aux
          l1=l[0:N_favoritos]              
         
     xx=0
     xx=x
     #rr="favoritos ag" +str(xx)+" campo "+str(c)+" -- "+str(lista[0:10])+'\n'
     # Resp.write(rr)
     # print("favoritos ag" +str(xx)+" campo "+str(c)+" -- ",l[0:10])      
     
    
    # print("los favoritos para x,c son",  x,c, l1)
     return(l1)

#*************************************************************************************
def PROCESO_ARCH():
     SALTO=999
     import numpy, random
     global id_msg, MAXMENS, MAXREGS,N_agentes,MAXIT,MIN_CONF_O,MAX_CONF_O, hora_inicial
     global a, decision,line111, RESTANTES_ANT,RESTANTES_ANT_REG
     global t_entrada, tipo_mens, t_generac, largo_cola,Q,Qx,niveles,S,T  , pendientes, restantes,cuenta_to, cuenta_e, cuenta_a, TABLA_TO, MENSAJES_ITER, pregunte
     global m
     TIMEOUTS=0
     

     hora_inicial=numpy.zeros((MAXIT+1,MAXMENS+1,N_campos+1),dtype=int)   # la hora a la que omega consulta al sistema
     #hora_inicial=numpy.zeros((34,40,74),dtype=int)   # la hora a la que omega consulta al sistema   
     
     #pregunte=numpy.zeros((N_agentes+1,N_agentes+1,MAXMENS+1, N_campos+1), dtype=int) # si ya pregunto un agente a otro por ese campo en ese mensaje. previene loops.
     pregunte={}
#  cuenta_to=0
     cuenta_e=0
     cuenta_a=0
     EXITOS_E=0
     EXITOS_A=0
     MENS_ITER=0
     # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  

     #s="datosOMEGA 1 reg.csv"

     #s="datosOMEGA - 4 regs.csv"

     # s="datosOMEGA - 59 regs.csv"

     s="datosOMEGA - 33 regs.csv"

     # * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * 
     try:
          # f= open(s, 'r', encoding='ascii', errors='ignore')
          ff= open(s, 'r')

     except:
          print(s+"  ***** ARCHIVO INEXISTENTE *****" )

     line1=ff.readline()
     line111=line1.strip()   
     t_entrada={}
     t_generac={}
     largo_cola={}
     tipo_mens={}
     pendientes=numpy.zeros((N_agentes+1,MAXREGS+1, N_campos), dtype=int)
     Q={}
     Qx={}
     T={}
     niveles={}
     TO_MSG=numpy.zeros((N_agentes+1, N_agentes+1), dtype=int)  
     
     id_msg=0
     llave=0
     a=0
     procesados={}
     while len(line111) > 0:
          tipo_mens={}
          line1=ff.readline()
          line111=line1.strip()  
       #   print("yuvbjhbkunklnl",len(line111))
       
        
        
      #    print("something")
      #    wait = input("PRESS ENTER TO CONTINUE.")
                 
          id_msg=id_msg+1  
          m = id_msg
          RESTANTES_ANT_REG=N_agentes*MAXMENS


          print(";;;;;;;;;;;;;;;;;;;;;;;;;;; lei reg ;;;;;;;;;;;;;;;;",m)
          # GENERO LAS CONSULTAS DE OMEGA ****************************************


          nivel = 1
     # Qx1 es la calidad de OMEGA     
     #    Qx1=0.95
          #Qx1=random.random()

     #  Cargo las calidades iniciales
          Qx1=min(random.random()+MIN_CONF_O, MAX_CONF_O)
          Qy=0
          taux=0
     #  rr="**************************************** proceso registro "+str(id_msg)+"\n"
     #  print("*************************************** proceso registro "+str(id_msg))
     # Resp.write(rr)
          if llave == 0 :
               tope = muchos
               llave=1
          else:
               tope = N_favoritos +1
     #llave = 1         COMENTE EL BLOQUE PARA EL DEBUGGING CON 1 SOLO REG. LLave dice si es el primer reg o no

          #tope=N_favoritos+1   # SACARLO CUANDO HAYA MAS DE UN REG

          

               #  print("Restantes de OMEGA"+str(restantes))
               # arma la lista de los n favoritos ordenados por nros de exitos a partir de la matriz FAVORITOS
          #  print("voy a armar lista fav")
          lista2=[]
          lista1=arma_lista_fav(1,decision,lista2,N_favoritos,N_agentes) 
     #    print(" favs de OMEGA para decision",lista1[1:10])
          lista2=lista1
          for i in range(0,len(lista2)):
          #     rr="OMEGA consulta a "+str(lista[i-2])+" con calidad "+str(Qx1)+"\n"
          #       Resp.write(rr)

                   
               #   print ("OMEGA consulta a "+str(lista[i-2])+" con calidad "+str(Qx1))
                         if m < MAXREGS+1:
                              niveles[1,lista2[i],m, decision]=nivel
                    #     T=t
                       #  if restantes[1] > 0  : # and MODO == "I" or MODO=="S":
                              
                              if m < MAXREGS + 1 :
                                   hora_inicial[iteracion, m,decision]=a
                                   #espera=int(random.random()*TIMEOUT)
                                   #MENSAJES_ITER=MENSAJES_ITER+1
                                   #tipo_mens[a+espera,1,lista2[i],m,decision]=1
                                   #t_generac[1,lista2[i],m,decision,a+espera]=a
                                   #t_entrada[1,lista2[i],m,decision, a]= a+espera
                                   #print ("genero entrada de cons de OMEGA para ag", lista2[i], "mens", m)
                                   #if (lista2[i], m,decision) in largo_cola:
                                        #largo_cola[lista2[i], m, decision]= largo_cola[lista2[i], m, decision] +1
                                   #else:
                                        #largo_cola[1, m, decision]= 1
                                   #niveles[1,lista2[i], m, decision]=nivel
                                   #restantes[1]=restantes[1]-1  
                                   #a=a+1                                   
                                   Qy=CONSULTAR(1, lista2[i], decision, niveles[1,lista2[i],m, decision], Qx1, Qy)  
                         #   print("calidad devuelta a OMEGA en CONSULTAR"+str(Qy) ," calidad propiade OMEGA", Qx1)
                              #   restantes[1]=restantes[1]-1
                                   taux=a



          k=0
          tmax=0 

          # PROCESO LISTA DE MENSAJES GENERADOS POR REGISTRO ***************************************************
     #  print("PROCESO LISTA DE MENSAJES GENERADOS POR REGISTRO  tipo_mens  = ", tipo_mens, "t_entrada", t_entrada)
          mm=0
          ag = 1
          hay=0
          xx=ag=campo=1
          aant=xxant=agant=mant=campoant=1
          PRIMERO=1
     #mientras haya mensajes para algun agente
          tt =0 
  #        print (sorted(tipo_mens.keys()))

          a=0
          amin=99999
          puntero=0
         # for (a,xx, ag, mm, campo) in sorted(list(tipo_mens.keys())) :
          for (a,xx, ag, mm, campo) in sorted(list(tipo_mens)) :
          #     print("proceso reg",m)               
          #    print (sorted(list(tipo_mens.keys())))
             #  if mm == m:
                    cl=sorted(list(tipo_mens.keys()))
                    cl1=cl[puntero]
                    a=cl1[0]
                    xx=cl1[1]
                    ag=cl1[2]
                    mm=cl1[3]
                    campo=cl1[4]
                    if PRIMERO == 1:
                         aant= a
                         t= a
                         xxant=xx
                         agant=ag
                         mant=mm
                         campoant=campo
                         PRIMERO =0
                    else:
        
                         cl=sorted(list(tipo_mens.keys()))
                         cl1=cl[puntero]
                         a=cl1[0]
                         xx=cl1[1]
                         ag=cl1[2]
                         mm=cl1[3]
             #            print("************************* mm ",mm)
                         campo=cl1[4]                    
                         aant= a
                         xxant=xx
                         agant=ag
                         mant=m
                         campoant=campo
                         t= a            
                    puntero=puntero+1   
                #    print("LEI  xx", xx," a", ag, "tipo", tipo_mens[a,xx,ag,mm,campo], " para m", mm, "puntero",puntero, "clave",cl1)
                #    print(sorted(list(tipo_mens)))
                   
           #         print(sorted(tipo_mens.keys()))
                    if  mm== m and not ((xx,ag,m,campo) in procesados) : 
                        
                         procesados[xx,ag,mm,campo]=1
                         if  a < amin:
                              amin =  a
                                    
                   #      print ("proceso *******",a,xx,ag,m,campo)
                #         print(t_generac)
                         if t_generac[xx, ag, m, campo, a] + TIMEOUT > a and tipo_mens[ a,xx, ag, m, campo] == 2 :  #  NO ES TO 
                              pendientes[ag,m,campo]=pendientes[ag,m,campo] - 1 
          
                         #     print("no es T O y es repuesta de",xx," a", ag, "para m", m, "puntero",puntero, "clave",cl1)
                              hay =1 
                              Qaux=Q[xx,ag,m,campo]
                              if restantes[ag]>0 or ag ==1:           # and MODO == "I" or MODO=="S":
                                   
                                   RESPONDER(ag,xx,campo,Qaux,N_agentes,MODO, a)
                                  

                                   FAVORITOS[ag,xx,campo]=FAVORITOS[ag,xx,campo]+1
                         else:  
                              if t_generac[xx, ag, m, campo, a] + TIMEOUT > amin  and tipo_mens[ a,xx, ag, m, campo] == 1 :    # 1 - consulta 2 - Respuesta :
          
                                   hay =1                         
                  #                 print("no es T O y es consulta de",xx," a", ag)   
          
          
                                   # proceso consulta
                                   if (xx,ag,m,campo) not in Q:
                                        Q[xx,ag,m,campo]=0
                                   Qaux=Q[xx,ag,m,campo]
          
                                   #S[xx,m,campo]=S[xx,m,campo]+1
                                   
                                   nadie=1
                                   for i in range(1,N_agentes):
                                        if (ag,i,m,campo ) in pregunte and pregunte[ag,i,m,campo]==1:
                                             nadie=0
                               
                               
                                   if nadie==1 and MODO == "I" or MODO=="S":
                                        pregunte[xx,ag,m,campo]=1                         
                                   if restantes[xx]>0  :     # and MODO == "I" or MODO=="S":
                                        if not ((xx,ag,m,campo) in niveles):
                                             niveles[xx,ag,m,campo]= 1
                                        CONSULTAR(xx, ag, campo,niveles[xx, ag, m, campo], Qaux,Qy)  
                                   
                              else:
                                   if t_generac[xx, ag, m, campo, a] + TIMEOUT <  a:
                                        TO_MSG[xx,ag]=TO_MSG[xx,ag]+1
          
                                   TIMEOUTS=TIMEOUTS+1
                    
                         # proceso los mensajes para OMEGA **********************************************************                      
              
     #print("proceso mensajes de OMEGA en main()") 
        
          
          
          if not (1,m,decision) in largo_cola:
               largo_cola[1,m,decision] = 0

          
         
          aporta_e=0
          aporta_a=0
          enhora=0
          u=1
          tiempo=a
          uu=0
          NO=0
        
          ESTRICTO=0
          AMPLIO=0
          conte=0               
          for (tiempo1,u,uu,m1,decision1) in sorted(list(tipo_mens.keys())): 
                    #   print (tipo_mens[tiempo,u,1,id_msg,decision],t_generac[u,1,id_msg,decision,tiempo],t_entrada[u,1,id_msg,decision, t_generac[u,1,id_msg,decision,tiempo]])
               if uu==1 :   
          #   print ("encontre", u,1,m,decision,tiempo )
                  
                    if tipo_mens[tiempo1,u,1,m1,decision1]== 2 and   hora_inicial[iteracion, m1,decision1]+ TIMEOUT > t_entrada[u,1,m1,decision1, t_generac[u,1,m1,decision1,tiempo1]]  and m1==m and decision1==decision:
               #   print("************  NO ES T O")
                         enhora=1
                         NO=1
               #   print("Q es ", Qx[u,1,m,decision]," calidad de OMEGA=",Qx1)
                         if Qx1 < Qx[u,1,m1,decision]  :
                              ESTRICTO=1
                         else:
                              if abs(Qx1- Qx[u,1,m1,decision]) < 0.01:
                                   AMPLIO=1
     
                    else:
                         if hora_inicial[iteracion, m1,decision1]+ TIMEOUT < t_entrada[u,1,m1,decision1, t_generac[u,1,m1,decision1,tiempo1]] and m1==m and decision1==decision and tiempo1>tiempo:
                              TO_MSG[u,1]=TO_MSG[u,1]+1
          
         # print("sdvsdvsdvsdv-----",len(line111))
          
         
                   #while k < largo_cola[1,id_msg,decision] + 1:
                   #while k < 100:
          taux1=a
          ES_EXITO_A=0
          ES_EXITO_E=0
          #for (a,xx, ag, m, campo) in sorted(list(tipo_mens.keys())) :
               #ES_EXITO_E=0
               #ES_EXITO_A=0
               #NO_ES_TO=0   # indica si hubo  o no T O . Si aunque sea uno solo contesta a omega a tiempo, no es TO
                   
                   
               #pant=0
               #rant=0
               #tmax=0
               #p=1
               ##   print ("veo si hay mensajes para el momento actual  t="+str(taux))
               ##   rr="veo si hay mensajes para el momento actual  t="+str(taux)+"\n"
               ##  Resp.write(rr)
     
               #p=0
               #r=1
               #tie=a
               #c=decision
               #pp=0
               #rr=r
     
                    
     
               #t=a       
                    
               #if (xx,1,m,decision,a) in list(t_entrada) and tipo_mens[ a,xx,1,m,decision]==2:
     
                    ##      print("Hay mensaje para OMEGA desde ag" + str(p)+" para mens "+ str(r))
                              #pant=p
                              #rant=r
                              #k=k+1

                         ## Qy calculada segun la form general para nivel =1 y error 0.95 es aprox 0.95
                         ## Qy=0.95  # Calidad de Omega: 0.95
                         ## Qy= random.random()  # dejo la calidad de Omega al azar
                         ##       print("---- Calidad de OMEGA ="+str(Qx1))
                              #if t_generac[xx, 1, m, decision, a] + TIMEOUT > t_entrada [xx,1,m,decision, a]: # en realidad deberia ser el t en que omega consulto al sist + TIMEOUT ++++++
                                   ## no es time out
                                   #NO_ES_TO=1
                                   #if Q[xx,1, m,decision] > Qx1  : # no importa el MODO, es estricto   
                                        #ES_EXITO_E=1
                                   ##  EXITOS_E =EXITOS_E+1
                                        #FAVORITOS[1,xx,decision]=FAVORITOS[1,xx,decision]+1

                                   ## el tiempo gastado es el max (t de la entrada  - t de generac) para las distintas respuestas. sobre que calculo el maximo?????  +++++
                                   ## if tmax < taux - t :
                                   ##   tmax=taux-t
                                   ## if pant==0:   # es la primer vez que proceso esa entrada 
                                   ##   NO_TO=NO_TO+1
                                   ##          print ("calidad Y"+str(Qy)+"calidad X "+str(Qx[1, p, r,decision]))       
                                        #FAVORITOS[1,xx,decision]= FAVORITOS[1,xx,decision] + 1           


                                   ##else:
                                        ##if abs(Q[xx,1, m,decision] - Qx1)<0.01:
                                             ##ES_EXITO_A=1
                                   ###       EXITOS_A =EXITOS_A+1


                              ##else:
                                   ##TO_MSG[xx,1]=TO_MSG[xx,1]+1

                              ##p=pant+1
     
                         
                    
                         ## no se si hacer temple simulado aca
                         ## taux=taux+1
                              #if NO_ES_TO ==0:
                                   #TIMEOUTS=TIMEOUTS+1  
                             
                         ##    print("##### t_gen","   ", t_generac)
                         ##    print ("%%%%%%%%% t_ent", " ",t_entrada)
                              #if len(t_entrada)==0:
                                   #if (iteracion,N_agentes,MAXREGS,MAXMENS) in TABLA_TO:
                                        #TABLA_TO[iteracion,N_agentes,MAXREGS,MAXMENS]= TABLA_TO[iteracion,N_agentes,MAXREGS,MAXMENS] + 1
                                   #else:
                                        #TABLA_TO[iteracion,N_agentes,MAXREGS,MAXMENS]=1      
          
          if NO == 0:
          #  print("********ESSSSS TO") 
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
     
         # print("cuenta E E ", cuenta_e)
          
        #  print("cuenta E A ", cuenta_a)          
     # print("------------------ cuenta to ---------------",cuenta_to, "  iteracion ", iteracion, "N_agentes", N_agentes,"MAXREGS",  MAXREGS)  

     TABLA_TO[iteracion,N_agentes,MAXREGS, MAXMENS]=cuenta_to

     

     TABLA_EXITOS_A[iteracion,N_agentes,MAXREGS,MAXMENS]=cuenta_a

     TABLA_EXITOS_E[iteracion,N_agentes,MAXREGS,MAXMENS]=cuenta_e  

     if ES_EXITO_A == 1:
          EXITOS_A=EXITOS_A+1

     if ES_EXITO_E ==1:
          EXITOS_E=EXITOS_E+1

     SALTO=max(SALTO,1)
     #t=t+SALTO

     RESTANTES_ANT_REG= N_agentes*MAXMENS

#  hora_mens[id_msg]=t
#  if id_msg > MAXREGS -1 :
#    continue

     # cereo arreglos ******************************************************************
     #    print("EXITOS A ", str(EXITOS_A),"EXITOS E ", str(EXITOS_E), "TIME OUTS ", str(TIMEOUTS))



     SALTO=999


               #  ******************************************************************************


     # rr=" *****************  FIN DE EJECUCION DE ITERACION*****************"
     # Resp.write(rr)
     # print(rr)

#***********************************************************************************************************************************************

def main():

     import asyncio 
     import random
#  import pandas
     import numpy
     import io
     import csv
     global Resp
     global id_msg
     global MAXMENS,N_agentes, MAXIT,MAXREGS,MIN_CONF_O,MAX_CONF_O,N_campos, hora_inical, MAXIT
     global t_entrada, t_generac, tipo_mens, largo_cola, niveles, pendientes, restantes, MENSAJES_ITER,a, pregunte
     

    
  #   import py_compile
  #   aq=1
  #Qwww=py_compile.compile("C:/Users/hpaggi/Dropbox/docs tesis/prototipo/cuarto negocio/simuladorrapido.py", cfile="C:/Users/hpaggi/Dropbox/docs tesis/prototipo/cuarto negocio/rapidito")
  #   print(Qwww)
 #    aq=2    
     
     MENSAJES_ITER=0
     s="LOG DE SIMULADOR.txt"
     Resp=open(s,'w')

     #***********************************************************
     #      Parametros
     #***********************************************************
     # tiempo de time out
     global TIMEOUT

     #TIMEOUT= 1000

     TIMEOUT=300

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
     global a
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

     MAXIT=32
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
     TABLA_CALIDADES_MENS=numpy.zeros((MAXIT+1,101),dtype=int)
     TABLA_CALIDADES_FREC=numpy.zeros((MAXIT+1,101),dtype=int)
     # cada fila tiene cuantos mensajes se usaron para tener esa calidad final Q en la salida de OMEGA, cada fila es una iteracion 

     global TABLA_TO

     TABLA_TO={}

     # cantidad de T O que se produjeron por iteracion para una cierta cantidad de agentes y un cierto registro
     ##############################################################################################################
     global line111, line1
     global iteracion
     global TOLERANCIA
     global a
     global restantes
     
     
     
     TOLERANCIA=1 # cuantas veces se admite un to desde un favorito antes de borrarlo de la lista de favoritos
     # cant reg a prcesar por OMEGA en el archivo
     global MAXREGS
     MAXREGS= 32 

     #for N_agentes in (10,40):
     for N_agentes in (600,201):

          # los errores  y los topes de confianza
          MIN_CONF=0.4
          MAX_CONF=0.95
          MIN_CONF_O=0.6
          MAX_CONF_O=0.87 

               # error de cada agente en cada campo
          H=numpy.zeros((N_agentes+1,N_campos), dtype=float)
          
          s="H"+str(N_agentes)
          F= open(s, 'r', encoding='ascii', errors='ignore')          
          for i in range(1,N_agentes):
               for j in range(0,N_campos):
                    h=F.readline()
                    H[i,j]=float(h)
                    print(H[i,j])
                    
                    
          # for MAXMENS in [1000]:
          for MAXMENS in (50, 100,200,500,1000):   
          #for MAXMENS in (10,20):
     #  for MAXMENS in [100]: 
               for MODO in ("I","S"):
          # for MODO in ["S"]:

                    print(" ))))))))))))))))))  MODO "+MODO+" (((((((((((((((((((((__"+str(N_agentes)+"__"+str(MAXMENS))

                    MAXIT=32
                    for iteracion in range(1,MAXIT+1): # cada iteracion son los 50 regs
                         RESTANTES_ANT=N_agentes*MAXMENS

                         global restantes
                         restantes=numpy.zeros(N_agentes+1, dtype=int)
                         restantes.fill(MAXMENS)            

                         t=0  
                         id_msg=0
                         TIMEOUTS=0
                         global cuenta_to, cuenta_e, cuenta_o,cuenta_a
                         cuenta_to=0
                         cuenta_a=0
                         cuenta_e=0              
                         print("######################### iteracion nro ##################   ", iteracion)
                         MENSAJES_ITER=0
                         RESTANTES_ANT= N_agentes*MAXMENS
                         RESTANTES_ANT_REG= N_agentes*MAXMENS
                         FAVORITOS=numpy.zeros((N_agentes+1,N_agentes+1,N_campos), dtype=int)
                         for i in range (1,N_agentes+1) :
                              for j in range (1,N_agentes+1):
                                   if i != j and j != 1:
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
                         muchos = 20                       # antes era 7


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
                         
                         

                         #**************************************************************** 
                         res=PROCESO_ARCH()
                   #      print(MENSAJES_ITER)
                         #****************************************************************      

                         #TABLA_EXITOS_A.append(iteracion,N_agentes,MAXREGS,MAXMENS)
                         TABLA_EXITOS_A[iteracion,N_agentes,MAXREGS,MAXMENS]=cuenta_a
                    # TABLA_EXITOS_E.append(iteracion,N_agentes,MAXREGS,MAXMENS)
                         TABLA_EXITOS_E[iteracion,N_agentes,MAXREGS,MAXMENS]=cuenta_e  
     #       TABLA_TO[iteracion,N_agentes,MAXREGS,MAXMENS]=cuenta_to

                         r=0
                         for i in range (1,N_agentes):
                              r=r+restantes[i]
                    # TABLA_MENS.append(iteracion,N_agentes,MAXREGS,MAXMENS)
                         TABLA_MENS[iteracion,N_agentes,MAXREGS,MAXMENS]=MENSAJES_ITER   
                    #    print(TABLA_MENS[iteracion,N_agentes,MAXREGS,MAXMENS])


                         # RESTANTES_ANT=r 

                    print("\/\/\/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/\/          fin         \/\/////////////////////////////////\/\/\/")

                    s="RESULTADOS_"+str(N_agentes)+"_"+str(MAXMENS)+"_"+MODO+"_"+str(MAXIT)+"_"+str(MAXREGS)+"_"+str(N_favoritos)+"XXXXXX  00000"+" 200 it.txt"

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
                              s=str(TABLA_TO[i,N_agentes,MAXREGS,MAXMENS])+"\n"
                              R.write(s)
                    R.write("  \n")  

                    R.write("************************* FREC DE CALIDADES  ***************************************\n")   
                    R.write("  \n")         
                    #for j in range (1,MAXIT+1):
                         #for i in range (0,100):
                              #s=str(TABLA_CALIDADES_FREC[j,i])+","
                              #R.write(s)
                         #R.write("  \n") 
                    for j in range (1,MAXIT+1):
                         for i in range (0,100):
                              s=str(TABLA_CALIDADES_FREC[j,i])+"\n"
                              R.write(s)
                    R.write("  \n")             
                    R.write("************************* MENS por CALIDADES  ***************************************\n")   
                    R.write("  \n")         
                    #for j in range (1,MAXIT+1):
                         #for i in range (0,100):
                              #s=str(TABLA_CALIDADES_MENS[j,i])+","
                              #R.write(s)
                    R.write("  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    promedios de mensajes por calidad  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  \n")
                   
                    for i in range (0,100):
                         calidad_aux=0
                         cuenta_aux=0
                         for j in range (1,MAXIT+1):
                              if TABLA_CALIDADES_MENS[j,i] > 0:
                                   cuenta_aux=cuenta_aux+1
                                   calidad_aux=calidad_aux+TABLA_CALIDADES_MENS[j,i]
                         if cuenta_aux > 0:
                              prom=calidad_aux/cuenta_aux
                              s=str(prom)+"\n"
                              R.write(s)                              
                         else:
                              s=" "+"\n"
                              R.write(s)
                         
                         
                       
                    R.write("  \n")                   


                    s="************************* MENS TOTALES POR ITERACION   ***************************************\n"
                    R.write(s)
                    R.write("  \n") 

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
                    R.write("  \n") 
                    for i in range (1,MAXIT+1):
                         if (i,N_agentes,MAXREGS,MAXMENS) in TABLA_EXITOS_A:
                              s=str(TABLA_EXITOS_A[i,N_agentes,MAXREGS,MAXMENS])+"\n"
                              R.write(s)
                    R.write("  \n")    
                    R.close()
main()