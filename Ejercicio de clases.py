class Mascotas(object):
    def __init__(self,perro,gato):
        self.perro=perro
        self.gato=gato
    def obtener_datos(self):
        print 'Informacion sobre esta clase: '
        return 'Esta clase sera sobre {perro} {gato}'.format(perro=self.perro,gato=self.gato)
class Gatos(Mascotas):
    def __init__(self,nombre,raza,edad,color):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.color=color
    def datos_gato(self):
        print 'Informacion con respecto a los gatos: '
        return 'El nombre de esta gato es {nombre} y es de  raza {raza} con una edad de {edad} anios de color {color}'.format(nombre=self.nombre,
                raza=self.raza,edad=self.edad,color=self.color)
class Perro(Mascotas):
    def __init__(self,nombre,raza,color,tamanio):
        self.nombre=nombre
        self.raza=raza
        self.color=color
        self.tamanio=tamanio
    def datos_perro(self):
        print 'Los datos de los perros son: '
        return 'El nombre de el perro es {nombre} de raza {raza} con un color {color} y tamanio de {tamanio} cm'.format(nombre=self.nombre
                ,raza=self.raza,color=self.color,tamanio=self.tamanio)
if __name__=='__main__':
    datos=Mascotas('Perros y','gatos')
    print datos.obtener_datos(), '\n'
    gat=Gatos('Pekka','Angora','1/2','pardo')
    print gat.datos_gato(),'\n'
    dog=Perro('Oso','Pastor Velgar','negro','120')
    print dog.datos_perro()
