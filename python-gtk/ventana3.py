import  gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
    def __init__(self,*args,**kwargs):
        super(MiVentana, self).__init__(*args,**kwargs)
        self.set_default_size(500,300)
        self.connect('delete-event',Gtk.main_quit)
	self.agregar_texto()
 	#self.agregar_label()
    def agregar_texto(self):
	self.texto=Gtk.Entry()
  	texto.get_text()
	contenedor=Gtk.Entry()
    def agregar_button(self):
        self.button=Gtk.Button('Inicio')

    def agregar_label(self):
        self.label=Gtk.Label('')
        label.set_markup('Texto')

    def agregar_contenedor(self):
        self.contenedor = Gtk.Grid()
        self.contenedor=Gtk.Entry()
        #self.contenedor=Gtk.Button()
        #self.contenedor=Gtk.Label()


if __name__== '__main__':
    ventana= MiVentana()
    ventana.show_all()
    Gtk.main()
