import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def imprimir_algo(btn):
    print btn
    print 'HOLA MUNDO'

if __name__== '__main__':
    ventana = Gtk.Window(title='Ejemplo 1')
    ventana.connect('delete-event',Gtk.main_quit)
    button=Gtk.Button('Esto es un Btn 1')
    button.connect('clicked', imprimir_algo)
    button2= Gtk.Button('Segundo button')
    button3= Gtk.Button('Salir')
    button3.connect('clicked', Gtk.main_quit)
    #contenedor
    contenedor = Gtk.VBox()
    contenedor.pack_start(button,True,True,5)
    contenedor.pack_start(button2,True,True,5)
    contenedor.pack_end(button3,False,False,5)
    #False=eypand..expandir
    #false2=fill..rellenar
    #0=padding..margen
    ventana.add(contenedor)
    ventana.add(button)
    ventana.show_all()
    Gtk.main()
