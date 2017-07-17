import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk	
class Capital(Gtk.Window):
	"""docstring for ClassName"""
	def __init__(self, *args, **kwargs):
		super(Capital, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event',Gtk.main_quit)

		self.agregar_interfaz()
		self.introducir_datos()
		self.boton_activos()
		self.lbl_activo()
		self.lista_activos()

	def agregar_interfaz(self):
		self.interfaz =Gtk.Grid()
		self.interfaz.set_column_homogeneous(True)
		self.add(self.interfaz)

	def introducir_datos(self):
		self.descripcion = Gtk.Entry()
		self.cantidad = Gtk.Entry()
		self.interfaz.attach(self.descripcion,0,0,2,1)
		self.interfaz.attach_next_to(self.cantidad,self.descripcion,Gtk.PositionType.RIGHT,1,1)
		
	def boton_activos(self):
		self.activos = Gtk.Button('Agregar')
		self.interfaz.attach_next_to(self.activos,self.descripcion,Gtk.PositionType.BOTTOM,3,1)

	def lbl_activo(self):
		self.label = Gtk.Label('Estado...')
		self.interfaz.attach_next_to(self.label,self.activos,Gtk.PositionType.BOTTOM,3,1)

	def lista_activos(self):
		self.lista = Gtk.ListStore(str, float)
		self.almacen = Gtk.TreeView(self.lista)
		descrip = Gtk.CellRendererText()
		columna_descrip = Gtk.TreeViewColumn('Descripcion', descrip, text=0)
		cant = Gtk.CellRendererText()
		columna_cant = Gtk.TreeViewColumn('Cantidad', cant , text=1)
		self.almacen.append_column(columna_descrip)
		self.almacen.append_column(columna_cant)
		self.interfaz.attach_next_to(self.almacen,self.label, Gtk.PositionType.BOTTOM,3,1)
		self.activos.connect('clicked', self.agregar_valores)


	def agregar_valores(self, btn):
		A = self.descripcion.get_text()
		B = self.cantidad.get_text()
		self.lista.append([A, float(B)])

if __name__ == '__main__':
	mostrar = Capital()
	mostrar.show_all()
	Gtk.main()
		
