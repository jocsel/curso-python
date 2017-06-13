cuenta=0
cadenatxt= '"esto es una prueba"'
for ciclo in cadenatxt:
  if ciclo =='e':
    cuenta=cuenta+1;
    
print( 'El texto: ', cadenatxt,' contiene: ',cuenta, 'letras "e"' )
print (cadenatxt.upper())
print('La frase anterior esta compuesta por: ',len(cadenatxt),' letras.')
print(cadenatxt.replace('o','0'), 'reemplazamos la letra o por el 0.')