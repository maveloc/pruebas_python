#pues que decir, funciones
import random

def numero(num = 10):
    numrand= num * random.randrange(1,11)
    print(numrand)

numero(4)
#si el numero de argumentos que se le pasa a la funcion es desconocido se usa *num
#si se usa el par key = value y es desconocido se usa **
#añadirle el = x lo que hace es tenerlo por default si al invocarlo no le pasamos un parametro
def try_recursion (k):
    if(k>0):
        result = k+ try_recursion(k-1)
        print(result)
    else: 
        result= 0
    return result

print("ejemplo de recursion")
try_recursion(6)

#funciones lambda
x = lambda a : a*40
print(x(6))

def funcion(n):
    return lambda a : a * n

duplicador = funcion(2)

print(duplicador(11))