#Esto es un comentario
#print("Comentario")
print("Hola Mundo")
print("Adios mundo")

#Operadores aritmeticos
5+1
print(4+6)
print(5-2)
print(3+4)
print(20/4)
#Como la vida real
print(5+8*(3+2))

#Tipos de Datos
print(type(2))
print(type(8.62))
print(type("Texto"))
print(type("5"))

#Variables
mensaje = "Esto es un mensaje"
print(mensaje)
mensaje = "Mensaje Modificado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)
print(type(mensaje))

mis3animales = "perico, gallo, chivo"
print(mis3animales)

tresAnimales= "perico, gallo, chivo"
print(tresAnimales)

textoUno = "Mi texto"
textoDos = "Mi Segundo texto"

print(textoDos + textoUno)
#str() int() float()
edad = 20
print("La edad del usuario es: " + str(edad))
print("El tipo de edato de edad es: " + str(type(edad)))

import math

grados = 45.0
radiales = grados * math.pi / 100.0
seno = math.sin(radiales)
print("seno de 45: " + str(seno))

#hacer propia funcion
#void saludar() ejmp.

def saludar(nombre):
    #para añadir "nombre" tienes que especificarlo en en "saladur"
    print("Hola " + nombre)
    print("¿Como estas?")
    print("Te saludo de lejos")

def despedir():
    print("ya me voy")
    print("Bye")    

def concatenar(parte1, parte2):
    return parte1 + parte2

print("esto no es parte de la funcion")
#aqui se espcifica saldura
saludar("Emiliano")
despedir()  

frase = concatenar("Hola", "Adios")
print(frase)