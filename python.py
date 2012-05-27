#Mi primer programa en python V 2.7.3
#--------------------------------------
#Primeras lineas de comando

print "Hola mundo"
print 10

variable1 = "imprimiendo la variable con el comando print"
print variable1
numero1 = 50
print numero1

#Averiguar los tipos de variables

variable2 = "conteniendo en la variable texto"
type(variable2)
numero2 = 100
type(numero2)

#Condicionales con if/else y elif

num = 10
if num<10:
	print "el numero es menor a 10"
elif num == 10:
	print "el numero es igual a 10"

else:
	print "el numero es mayor a 10"

#Bucles con while, For

i = 0
while i<10:
	i = i+1
	print "El numero es " + str(i)

lenguajes = ["HTML5", "Javascript", "Python", "CSS"]

for data in lenguajes:
	print "->" + data

#Funciones

def suma(dato1, dato2):
	print dato1 + dato2

def desplegar(cadena, numero):
	print numero*cadena

suma(5,5)

desplegar("texto a multiplicar ", 2)
	