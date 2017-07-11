import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self,*args,**kwargs):
		Gtk.Window.__init__(self,title='Mi ventana')
		super(MiVentana, self).__init__(*args,**kwargs)
		self.set_size_request(500,300)
		self.connect('delete-event',Gtk.main_quit)

		self.agregar_button()
		self.agregar_txt()
		self.agregar_label()
		self.btnsalir()

		self.box = Gtk.VBox()
		self.box.pack_start(self.texto,True,True,0)
		self.box.pack_start(self.btn1,True,True,0)
		self.box.pack_start(self.label1,True,True,0)
		self.box.pack_start(self.btnsalir,True,True,0)

		self.add(self.box)

	def imprimir(self,btn):
		imprimir = self.texto.get_text()
		self.label1.set_text(imprimir)

	def agregar_button(self):
		self.btn1 = Gtk.Button('Enviar valor')
		self.btn1.connect('clicked',self.imprimir)

	def agregar_txt(self):
		self.texto = Gtk.Entry()

	def agregar_label(self):
		self.label1 = Gtk.Label('Atrapa el valor del textbox')

	def btnsalir(self):
		self.btnsalir = Gtk.Button('Salir')
		self.btnsalir.connect('clicked',Gtk.main_quit)

if __name__ == '__main__':
	 ventana=MiVentana()
	 ventana.show_all()
	 Gtk.main()

	