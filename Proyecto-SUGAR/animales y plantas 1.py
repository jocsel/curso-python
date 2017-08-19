import random
import gi

#import logging


# importar modulo que contiene clase base de actividad.
'''
from sugar3.activity import activity

from sugar3.graphics.toolbarbox import ToolbarBox

# boton para toolbar
from sugar3.activity.widgets import (
    ActivityToolbarButton,
    StopButton
)

#from ppt_utils import OPCIONES  agrega el modulo ppt_utils que contiene el diccionario llamado OPCIONES
'''
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

#logger = logging.getLogger(__name__)

class Inicio(Gtk.Window):
	"""docstring for ClassName"""
	def __init__(self, *args, **kwargs):
		super(Inicio, self).__init__(*args,**kwargs)
		self.set_default_size(500,500)
		self.agregar_contenedor()
		self.PrimeraVentanaPlanta()
		

	def agregar_contenedor(self):
        
		self.contenedor = Gtk.Grid()
		self.contenedor.set_row_homogeneous(False)

		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def PrimeraVentanaPlanta(self):

		
		self.planta = Gtk.Button('Clasificacion de las plantas')
		self.animales = Gtk.Button('Clasificacion de los animales')
		self.contenedor.attach(self.planta,0,0,1,1)
		self.contenedor.attach_next_to(self.animales,self.planta,Gtk.PositionType.RIGHT,1,1)	
		self.planta.connect('clicked',self.SegundaVentanaPlanta)
		self.animales.connect('clicked',self.SegundaVentanaAnimal)
		

	def SegundaVentanaPlanta(self,btn):

		#self.gtk_window_set_title (title="hola")

		for widget in self.contenedor:
			self.contenedor.remove(widget)

		self.boton_conflor_planta = Gtk.Button('Con Flor')
		self.boton_sinFlor_planta = Gtk.Button('Sin Flor')
		self.contenedor.attach(self.boton_conflor_planta,0,0,1,1)
		self.contenedor.attach_next_to(self.boton_sinFlor_planta,self.boton_conflor_planta,Gtk.PositionType.RIGHT,1,1)

		self.contenedor.show_all()
		self.boton_conflor_planta.connect('clicked',self.TerceraVentanaPlanta)
		self.boton_sinFlor_planta.connect('clicked',self.TerceraVentanaPlanta)


	def TerceraVentanaPlanta(self,b):
		
		for widget in self.contenedor:
			self.contenedor.remove(widget)
		
	
		self.boton_inicio_planta = Gtk.Button('Inicio')
		self.label_numero_planta = Gtk.Label('Numero de veces')
		self.numero_de_entrada_planta = Gtk.Entry()	
		self.contenedor.attach(self.label_numero_planta,0,0,1,1)
		self.contenedor.attach_next_to(self.numero_de_entrada_planta,self.label_numero_planta,Gtk.PositionType.RIGHT,1,1)
		self.contenedor.attach_next_to(self.boton_inicio_planta,self.label_numero_planta,Gtk.PositionType.BOTTOM,1,1)
		self.contenedor.show_all()
		self.boton_inicio_planta.connect('clicked',self.CuartaVentanaPlanta)
		

	def CuartaVentanaPlanta(self,btn):

		for widget in self.contenedor:
			self.contenedor.remove(widget)

		self.label_planta = Gtk.Label('las plantas de mi pais')
		self.contenedor.attach(self.label_planta,0,0,1,1)
		self.contenedor.show_all()


	def SegundaVentanaAnimal(self,btn):

		for widget in self.contenedor:
			self.contenedor.remove(widget)

		self.boton_dondeviven_animal = Gtk.Button('Donde Viven')
		self.boton_alimentacion_animal = Gtk.Button('Su alimentacion')
		self.contenedor.attach(self.boton_dondeviven_animal,0,0,1,1)
		self.contenedor.attach_next_to(self.boton_alimentacion_animal,self.boton_dondeviven_animal,Gtk.PositionType.RIGHT,1,1)
		self.contenedor.show_all()
		self.boton_dondeviven_animal.connect('clicked',self.TerceraVentanaAnimal)
		self.boton_alimentacion_animal.connect('clicked',self.TerceraVentanaAnimal)
		

	def TerceraVentanaAnimal(self,b):
		
		for widget in self.contenedor:
			self.contenedor.remove(widget)
		
		
		self.boton_inicio_animal = Gtk.Button('Inicio')
		self.label_numero_animal = Gtk.Label('Numero de veces')
		self.numero_de_entrada_animal = Gtk.Entry()	
		self.contenedor.attach(self.label_numero_animal,0,0,1,1)
		self.contenedor.attach_next_to(self.numero_de_entrada_animal,self.label_numero_animal,Gtk.PositionType.RIGHT,1,1)
		self.contenedor.attach_next_to(self.boton_inicio_animal,self.label_numero_animal,Gtk.PositionType.BOTTOM,1,1)
		self.contenedor.show_all()
		self.boton_inicio_animal.connect('clicked',self.CuartaVentanaAnimal)
		
		
		

	def CuartaVentanaAnimal(self,btn):
		for widget in self.contenedor:
			self.contenedor.remove(widget)

		self.label_animal = Gtk.Label('Los animales de mi pais')
		self.contenedor.attach(self.label_animal,0,0,1,1)
		self.contenedor.show_all()















if __name__ == '__main__':
	init = Inicio()
	init.show_all()
	Gtk.main()
		







