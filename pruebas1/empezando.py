print ("hello world")


#VARIABLES
if 5>2:
       print("5 es mayor lol")
    # print ("esto esta mal entonces"), hay que tener en cuenta la sangria en python

if 3<4:
       print("prueba de linea")    

#las variables no tienen por que asignarse en python, simplemente damos un valor y ya
x= 5
y= "luis"
print(x,y)

#despues se puede cambiar el tipo de la varible sin hacer nada
y=12
print(x,y)

#aunque tambien puedes hacer casting para decir de que tipo es cada variable
x=str(3)
y=int(3)
z=float(3)
print(x,y,z)

#se pueden asignar varias variables a la vez o que sean del mismo tipo
x = y = z = "platano"
print(x,y,z)

x, y, z = "banana", "sandia", 5
print(x,y,z)

frutas = ["melon", "manzana"]
x, y = frutas
print(x,y)

#las variables que se encuentran fuera de funciones son globales y se pueden llamar siempre que se quiera
def lafruta():
             print("mi fruta preferida es la "+y)

lafruta()

#una variable map es asi (un "dict")
map = {"nombre" : "luis", "edad" : 23}
print(map)

#una variable set es asi
set = {"ola", "que onda", "como tas"}
print(set)

#para randoms se importa el random y despues se usa
import random
print(random.randrange(1,11))
