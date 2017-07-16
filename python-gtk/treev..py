import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	"""docstring for MiVentana"""
	def __init__(self, *args,**kwargs):
		super(MiVentana, self).__init__(*args,**kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()
		self.agregar_entrada()
		self.agregar_boton()
		self.agregar_lista()
		self.agregar_label()
		self.salir()

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid() #interfaz
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry() #textbox
		self.entrada_monto = Gtk.Entry() #NUEVO TEXT
		self.contenedor.attach(self.entrada,0,0,2,1)
		self.contenedor.attach_next_to(self.entrada_monto,self.entrada,Gtk.PositionType.RIGHT,1,1) # EL 1 INDICA POSICION EN LA INTERFAZ Y Q ESTARAN A LA PAR en ese orden
		

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(self.boton,self.entrada,Gtk.PositionType.BOTTOM,3,1)#2=ancho del boton, 1=largo del boton

	def agregar_label(self):
		self.label= Gtk.Label('BIENVENIDO')

		self.contenedor.attach(self.label,0,3,3,1)#1=columna,#2=fila,3=margen derecho,#4=nro de filas a usar
	def salir(self):
		self.salir=Gtk.Button('Salir')
		self.contenedor.attach(self.salir,0,7,3,2)
		self.salir.connect('clicked',Gtk.main_quit)


	def agregar_lista(self):

		'''crear un treeview
      	1-crea el model de datos Gtk.ListStore(type..type..)
      	2-crear el widget q contiene o muestra los datos de modelo TreeView(<model>)
      	3-Definir las columnas y su contenido
      	3.1-crear celda para cada columna de la fila.
      	los CellRenderer son widgets q sirven para mostrar contenido dentro de otros
      	widgets dependiendo de su tipo
      	3.2-crear columnas(TreeViewColumn) del TreeView q mostraran los datos usando
      	CellRenderer widgets como elementos hijos
      	args:(Titulo, cellRenderer, posicion del modelo de la info a mostrar)
      	3.3-agregar cada TreeViewColumn al TreeView widget'''
		
		self.modelo = Gtk.ListStore(str,float)   #AGREGA EN LISTSTORE
		self.lista_activos = Gtk.TreeView(self.modelo) #AGREGA LOS VALORES DENTRO DEL LISTSTORE
		descripcion = Gtk.CellRendererText() #para agregar columna de descripcion
		columna_descripcion = Gtk.TreeViewColumn('Descripcion', descripcion,text=0) #para egregar columna dentro del treeview en la posicion 0
		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto',monto,text=1)
		self.lista_activos.append_column(columna_descripcion) #activa la columna
		self.lista_activos.append_column(columna_monto)
		self.contenedor.attach_next_to(self.lista_activos,self.boton,Gtk.PositionType.BOTTOM,3,1)  #1=ancho de la lista,self.boton indica q esta lista va bajo este boton
		self.boton.connect('clicked',self.agregar_fila)  #AGREGA LOS VALORES A LA FILA



   	def agregar_fila(self,btn):
   		texto = self.entrada.get_text() #get agarra
   		monto=self.entrada_monto.get_text() # NUEVA ENTRADA DE VALOR

   		
   		if texto.isalpha() and monto.isdigit() :    #isalpha=solo letreas, isdigit=solo num isalnum=alphanum
   			self.modelo.append([texto,float(monto)])
   			self.label.set_text('VALORES AGREGADOS CORRECTAMENTE')

   		else : 
   			
   			self.label.set_text('POR FAVOR INGRESAR LOS VALORES CORRECTAMENTE...!')


   		
   		'''try:

   			self.modelo.append([texto,float(monto)]) #para egragar los valores en al treeview
   		
   		except (TypeError, ValueError) as e:
   			if isinstance(e, TypeError):
   				print 'es un TypeError'
   			if isinstance(e, ValueError):
   				print 'es un value error'


   			print 'Este es el error', e'''

   		
   		self.entrada.set_text('') #set introduce  //PARA LIMPIAR VALORES
   		self.entrada_monto.set_text('')

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()

