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

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.entrada_monto = Gtk.Entry() #NUEVO TEXT
		self.contenedor.attach(self.entrada,0,0,2,1)
		self.contenedor.attach_next_to(self.entrada_monto,self.entrada,Gtk.PositionType.RIGHT,1,1) # EL 1 INDICA POSICION EN LA VENTANA

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(self.boton,self.entrada,Gtk.PositionType.BOTTOM,3,1)

	def agregar_label(self):
		self.label= Gtk.Label('BIENVENIDO')


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
		self.modelo = Gtk.ListStore(str,float)
		
		self.lista_activos = Gtk.TreeView(self.modelo)
		descripcion = Gtk.CellRendererText() #para agregar columnas
		columna_descripcion = Gtk.TreeViewColumn('Descripcion', descripcion,text=0) #para egregar columnas
		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto',monto,text=1)
		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)
		self.contenedor.attach_next_to(self.lista_activos,self.boton,Gtk.PositionType.BOTTOM,3,1)  #POSICION EL NUM 3 EN LA VENTANA
		self.boton.connect('clicked',self.agregar_fila)



   	def agregar_fila(self,btn):
   		texto = self.entrada.get_text() #get agarra
   		monto=self.entrada_monto.get_text() # NUEVA ENTRADA DE VALOR
   		
   		try:

   			self.modelo.append([texto,float(monto)]) #para egragar los valores en al treeview
   		
   		except (TypeError, ValueError) as e:
   			if isinstance(e, TypeError):
   				print 'es un TypeError'
   			if isinstance(e, ValueError):
   				print 'es un value error'


   			print 'Este es el error', e

   		
   		self.entrada.set_text('') #set introduce
   		self.entrada_monto.set_text('')

   		if self.entrada.get_text() =='':

   				self.label=Gtk.Label('')





if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()

