"""Desenvolver en Python unha calculadora por consola capaz de realizar varias operacións matemáticas, 
pero con unha restrición fundamental:

Só se poden empregar os operadores + e - para realizar calquera cálculo interno.

Queda totalmente prohibido o uso de: *, /, //, %, **.

O programa debe funcionar mediante un menú interactivo, permitindo ao usuario seleccionar a 
operación desexada.

A calculadora implementará as seguintes funcións sen usar ningún operador distinto de + e -:"""

def suma(x,y):
    n = x+y
    return n

def resta (x,y):
    n= x-y
    return n

def multiplicacion(x,y):
    contador=0
    n=0
    #con el while lo que hacemos es sumar x un numero de y veces
    while contador < y:
        n+=x
        contador+=1
        
    return f"{n:.3f}"

def division(dividendo,divisor):
    cociente = 0
    resto = dividendo
    
    if divisor == 0:
        # lanzamos error en caso de que el divisor sea 0
        raise ZeroDivisionError("El divisor no puede ser cero.")
    elif dividendo<0 or divisor<0:
        return("mejor no manejemos numeros negativos!")
    else:        
    
    # en el while restamos el resto hasta que sea menor que el divisor, y asi nos da el cociente
        while resto >= divisor:
            resto = resto - divisor
            cociente = cociente + 1
        return f"{cociente:.3f}", f"{resto:.3f}"
    #par obtener solo el cociente al llamar a division usaremos el indice [0], division(x,x)[0]
    

def potencia(x,y):
    n=x
    contador=1
    #le mandamos a la funcion multiplicacion los valores de n(que empieza siendo x) para que lo 
    #multiplique por x un total de y veces 
    while contador<y:
        n= multiplicacion(n,x)
        contador+=1
    return n


def modulo(x,y):

    n= division(x,y)
    #aprovecho que division ya devuelve el cociente y el resto para desde aqui llamarlo y guardar solo
    #el resto, ya que el return de division nos da una lista de 2 indices
    m = n[1]
    return m

resultado= division(6.754,6.12)
print(resultado)