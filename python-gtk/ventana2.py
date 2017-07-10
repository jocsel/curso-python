import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def imprimir_algo(btn):
    print btn
    print 'HOLA MUNDO'

if __name__== '__main__':
    ventana = Gtk.Window(title='Ejemplo 2')
    ventana.connect('delete-event',Gtk.main_quit)
    button=Gtk.Button('Esto es un Btn 1')
    #button.connect('clicked', imprimir_algo)
    button2= Gtk.Button('Segundo button')
    button3= Gtk.Button('3er button')
    button4=Gtk.Button('Salir')
    button4.connect('clicked', Gtk.main_quit)

    contenedor= Gtk.Grid()
    contenedor.set_column_homogeneous(True)
    contenedor.set_row_homogeneous(False)

    contenedor.attach(
    button,#Elemento
    0,#columna
    0,#Fila
    3,#Nro de columnas a usar
    1,#Nro filas a usar
    )

    contenedor.attach(button2,1,1,1,1)
    contenedor.attach(button3,2,1,1,1)
    contenedor.attach(button4,0,5,1,3)
    ventana.add(contenedor)

    ventana.show_all()
    Gtk.main()
