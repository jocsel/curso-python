import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	"""docstring for MiVentana"""
	def __init__(self, *args,**kwargs):
		super(MiVentana, self).__init__(*args,**kwargs)
		self.set_default_size(500,600)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()
		self.lblactivos()
		self.agregar_entrada()
		self.agregar_boton()
		self.agregar_label()
		self.agregar_lista()
		#####################

		self.lblvacio()
		self.lblpasivos()
		self.agregar_entrada2()
		self.agregar_boton2()
		self.agregar_label2()
		self.agregar_lista2()
		self.salir()

	def lblactivos(self):
		self.lblact = Gtk.Label('Lista de activos')
		self.contenedor.attach(self.lblact,0,0,3,1)

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid() 
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.entrada_monto = Gtk.Entry() 
		self.contenedor.attach(self.entrada,0,10,2,1)
		self.contenedor.attach_next_to(self.entrada_monto,self.entrada,Gtk.PositionType.RIGHT,1,1)

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(self.boton,self.entrada,Gtk.PositionType.BOTTOM,3,1)
	def agregar_label(self):
		self.label= Gtk.Label('Estado....')
		self.contenedor.attach_next_to(self.label,self.boton,Gtk.PositionType.BOTTOM,3,1)

	def salir(self):
		self.salir=Gtk.Button('Salir')
		self.contenedor.attach(self.salir,0,120,3,1)
		self.salir.connect('clicked',Gtk.main_quit)

	def agregar_lista(self):

		self.modelo = Gtk.ListStore(str,float)   
		self.lista_activos = Gtk.TreeView(self.modelo)
		descripcion = Gtk.CellRendererText() 
		columna_descripcion = Gtk.TreeViewColumn('Descripcion', descripcion,text=0) 
		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto',monto,text=1)
		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)
		self.contenedor.attach_next_to(self.lista_activos,self.label,Gtk.PositionType.BOTTOM,3,1)  
		self.boton.connect('clicked',self.agregar_fila) 

	def agregar_fila(self,btn):
   		texto = self.entrada.get_text() 
   		monto=self.entrada_monto.get_text()

   		
   		if texto.isalpha() and monto.isdigit() :   
   			self.modelo.append([texto,float(monto)])
   			self.label.set_text('Bien hecho...')

   		else : 
   			
   			self.label.set_text('POR FAVOR INGRESAR LOS VALORES CORRECTAMENTE...!')

   		self.entrada.set_text('') 
   		self.entrada_monto.set_text('')

   		########################################################
   	def lblvacio(self):
   		self.vacio = Gtk.Label()
   		self.contenedor.attach(self.vacio,0,10,3,10)

   	def lblpasivos(self):
   		self.lblpas = Gtk.Label('Lista de pasivos')
   		self.contenedor.attach(self.lblpas,0,20,3,10)


   	def agregar_entrada2(self):
		self.entrada2 = Gtk.Entry()
		self.entrada_monto2 = Gtk.Entry() 
		self.contenedor.attach_next_to(self.entrada2,self.lblpas,Gtk.PositionType.BOTTOM,2,1)
		self.contenedor.attach(self.entrada2,0,0,2,1)
		self.contenedor.attach_next_to(self.entrada_monto2,self.entrada2,Gtk.PositionType.RIGHT,1,1)

	def agregar_boton2(self):
		self.boton2 = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(self.boton2,self.entrada2,Gtk.PositionType.BOTTOM,3,1)

	def agregar_label2(self):
		self.label2= Gtk.Label('Estado....')
		self.contenedor.attach_next_to(self.label2,self.boton2,Gtk.PositionType.BOTTOM,3,1)

	def agregar_lista2(self):

		self.modelo2 = Gtk.ListStore(str,float)   
		self.lista_activos2 = Gtk.TreeView(self.modelo2)
		descripcion2 = Gtk.CellRendererText() 
		columna_descripcion2 = Gtk.TreeViewColumn('Descripcion', descripcion2,text=0) 
		monto2 = Gtk.CellRendererText()
		columna_monto2 = Gtk.TreeViewColumn('Monto',monto2,text=1)
		self.lista_activos2.append_column(columna_descripcion2)
		self.lista_activos2.append_column(columna_monto2)
		self.contenedor.attach_next_to(self.lista_activos2,self.label2,Gtk.PositionType.BOTTOM,3,1)  
		self.boton2.connect('clicked',self.agregar_fila2) 

	def agregar_fila2(self,btn2):
   		texto2 = self.entrada2.get_text() 
   		monto2=self.entrada_monto2.get_text()

   		
   		if texto2.isalpha() and monto2.isdigit() :   
   			self.modelo2.append([texto2,float(monto2)])
   			self.label2.set_text('Bien hecho...')

   		else : 
   			
   			self.label2.set_text('POR FAVOR INGRESAR LOS VALORES CORRECTAMENTE...!')

   		self.entrada2.set_text('') 
   		self.entrada_monto2.set_text('')

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()