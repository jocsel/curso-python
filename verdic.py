import argparse

if __name__=='__main__':
	parser= argparse.ArgumentParser()
	parser.add_argument('nombre')
	args=parser.parse_args()
	nombres={'nombre':'juan'}

	for llave,valor in nombres.iteritems():

		if args.nombre in nombres:
		  print('Este nombre existe en el diccionario como llave')
		else:
		  print('El diccionario no contiene esta llave')