import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MiVentana(Gtk.ApplicationWindow):
	"""docstring for MiVentana"""
	def __init__(self, *args,**kwargs):
		super(MiVentana, self).__init__(*args,**kwargs)
		self.set_default_size(500,600)
		#self.connect('delete-event',Gtk.main_quit)
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
		####################
		self.lbl_calculo_activos()
		self.lbl_suma_activos()
		self.lbl_calculo_pasivo()
		self.lbl_suma_pasivos()
		self.capital()
		#self.diferencia()

	def lblactivos(self):
		self.lblact = Gtk.Label('**********************Lista de activos**********************')
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
		self.salir=Gtk.Button('************************************')
		self.contenedor.attach(self.salir,0,130,3,1)
		#self.salir.connect('clicked',Gtk.main_quit)

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
   		self.cont =0
   		
   		if texto.isalpha() and monto.isdigit() :  
   			 
   			self.modelo.append([texto,float(monto)])
   			for a in self.modelo:
   				res = float(a[1])
   				self.cont += res
   				self.suma.set_text(str(self.cont))

   			self.label.set_text('Bien hecho...')
   			self.diferencia()

   		else : 
   			
   			self.label.set_text('POR FAVOR INGRESAR LOS VALORES CORRECTAMENTE...!')

   		self.entrada.set_text('') 
   		self.entrada_monto.set_text('')

   		########################################################
   	def lblvacio(self):
   		self.vacio = Gtk.Label()
   		self.contenedor.attach(self.vacio,0,10,3,10)

   	def lblpasivos(self):
   		self.lblpas = Gtk.Label('**********************Lista de pasivos**********************')
   		self.contenedor.attach(self.lblpas,0,20,3,10)


   	def agregar_entrada2(self):
		self.entrada2 = Gtk.Entry()
		self.entrada_monto2 = Gtk.Entry() 
		self.contenedor.attach_next_to(self.entrada2,self.lblpas,Gtk.PositionType.BOTTOM,2,1)
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
   		
   		self.contador=0
   		if texto2.isalpha() and monto2.isdigit() :  
   			 
   			self.modelo2.append([texto2,float(monto2)])

   			for i  in self.modelo2:

   				add = float(i[1])
   				self.contador+= add
   				#print contador
   				self.resta.set_text(str(self.contador))
   		
   			self.label2.set_text('Bien hecho...')
   			self.diferencia()

   		else : 
   			
   			self.label2.set_text('POR FAVOR INGRESAR LOS VALORES CORRECTAMENTE...!')

   		self.entrada2.set_text('') 
   		self.entrada_monto2.set_text('')

   	def lbl_calculo_activos(self):
   		self.act = Gtk.Label('Total activos')
   		self.contenedor.attach_next_to(self.act,self.lista_activos2,Gtk.PositionType.BOTTOM,1,1)

   	def lbl_suma_activos(self):
   		self.suma = Gtk.Label('0')
   		self.contenedor.attach_next_to(self.suma,self.act,Gtk.PositionType.RIGHT,1,1)

   	def lbl_calculo_pasivo(self):
   		self.pasiv = Gtk.Label('Total pasivos')
   		self.contenedor.attach_next_to(self.pasiv,self.act,Gtk.PositionType.BOTTOM,1,1)

   	def lbl_suma_pasivos(self):
   		self.resta = Gtk.Label('0')
   		self.contenedor.attach_next_to(self.resta,self.pasiv,Gtk.PositionType.RIGHT,1,1)

   	def capital(self):
   		self.capitall = Gtk.Label('Capital')
   		self.contenedor.attach(self.capitall,0,55,1,1)
   		self.dif = Gtk.Label('0')
   		self.contenedor.attach_next_to(self.dif,self.capitall,Gtk.PositionType.RIGHT,1,1)

   	def diferencia (self):
   		z=0
   		z= float(self.cont) - float(self.contador)
   		self.dif.set_text(str(z))
   		
   
if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main(),