import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]


def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'ciudad': random.choice(CIUDADES)
        }

    return estudiantes
dic=generar_diccionario_estudiantes()
print('Los valores del diccionario son:')
print(dic)
print

for clave,valor in dic.iteritems():
    orden='El estudiante {0} de {1} anio es de la ciudad de {2} y cursa {3} anio en la universidad'
    print (orden.format(clave,valor['edad'],valor['ciudad'],valor['anio']))
print
print('Los estudiantes de Managua son: ')
for clave,valor in dic.iteritems():
     managuas='El estudiante {0} de edad {1}, es de la ciudad de {2} y cursa el anio {3} en la universidad'
     if valor['ciudad']=='Managua':
       print(managuas.format(clave,valor['edad'],valor['ciudad'],valor['anio']))
     
print
print('Los estudiantes de Masaya son:')
for clave, valor in dic.iteritems():
      masayenos='El estudiante {0} de edad {1} es de la cuidad de {2} y cursa el anio {3} en la universidad'
      if valor['ciudad']=='Masaya':
        print(masayenos.format(clave,valor['edad'],valor['ciudad'],valor['anio']))
print
print('Los estudiantes menores de 21 anios son: ')
for clave,valor in dic.iteritems():
  menores='El estudiante {0} de edad {1} es de la cuidad de {2} y cursa el anio {3} en la universidad'
  if valor['edad']<21:
    print(menores.format(clave,valor['edad'],valor['ciudad'],valor['anio']))