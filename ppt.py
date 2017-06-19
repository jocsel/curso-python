li={1:'piedra',2:'Papel',3:'Tijera'}
op=0
a=0
cambio=0
cant= int(input('Numero de jugadores:'))
print()
print ('Elige una de los siguientes opciones disponibles:')
for op in li:
  print (op,':',li[op]) 
print()
for a in range(0,3):
  print('Ronda #',(a+1))
  print('Elecciones de los jugadores: ')
  for op in range((cant)):
    print('El jugador #',(op+1),'elige la opcion: ')
    eleccion=int(input())
    if eleccion<=0 :
      print('Opcion inavilitada, elige una de las opciones disponibles')
      print('El jugador #',(op+1),'elige la opcion: ')
      eleccion=int(input())
      if eleccion<=0 :
        print('Opcion inavilitada, elige una de las opciones disponibles')
        print('El jugador #',(op+1),'elige la opcion: ')
        eleccion=int(input())
      if eleccion<=0 :
        print('Opcion inavilitada, elige una de las opciones disponibles')
        print('El jugador #',(op+1),'elige la opcion: ')
        eleccion=int(input())
      if eleccion<=0 :
        print('Este jugador perdio esta ronda...!')
    if eleccion>3:
      print('Opcion inavilitada, elige una de las opciones disponibles')
      print('El jugador #',(op+1),'elige la opcion: ')
      eleccion=int(input())
      if eleccion>3 :
        print('Opcion inavilitada, elige una de las opciones disponibles')
        print('El jugador #',(op+1),'elige la opcion: ')
        eleccion=int(input())
        if eleccion>3 :
          print('Opcion inavilitada, elige una de las opciones disponibles')
          print('El jugador #',(op+1),'elige la opcion: ')
          eleccion=int(input())
        if eleccion>3 :
          print('Opcion inavilitada, elige una de las opciones disponibles')
          print('El jugador #',(op+1),'elige la opcion: ')
          eleccion=int(input())
        if eleccion>3 :
          print('Este jugador perdio esta ronda...!')
    if eleccion >=1 & eleccion<= 3:
      cambio=0
      c=0
      c=op+1
      cambio+=1
      li={1:'piedra',2:'Papel',3:'Tijera'}
      empate=0
      jugador1=0
      jugador2=0
      ################## POSIBLE EMPATES
      if op==1 & 1 in li:
        if op==2 & 1 in li:
           empate+=1
      if op==1 & 2 in li:
        if op==2 & 2 in li:
           empate+=1
      if op==1 & 3 in li:
        if op==2 & 3 in li:
           empate+=1
      ################ POSIBLES GANADAS DEL JUGADOR 1
      if op==1 & 1 in li:
        if op==2 & 3 in li:
           jugador1+=1
      if op==1 & 2 in li:
        if op==2 & 1 in li:
          jugador1+=1
      if op==1 & 3 in li:
        if op==2 & 2 in li:
           jugador1+=1
      ################ POSIBLES GANADAS DEL JUGADOR 2
      if op==2 & 1 in li:
        if op==1 & 3 in li:
           jugador2+=1
      if op==2 & 2 in li:
        if op==1 & 1 in li:
           jugador2+=1
      if op==2 & 3 in li:
        if op==1 & 2 in li:
           jugador2+=1
    ##########################################
      if eleccion<=3:
        print('**********************')
      if c==2:
        print('Ronda #',(a+1),'completada')
        
print('El total de empates ocurrido durante el juego fue de: ' ,empate)
print('Ganadas del jugador 1: ',jugador1)
print('Ganadas del jugador 2: ',jugador2)
if jugador1>jugador2:
  print('El ganador fue el jugador 1')
elif jugador2>jugador1:
  print('El ganador fue el jugador 1')