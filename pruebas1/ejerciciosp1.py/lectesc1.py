#Escribir un programa que calcule el área de una finca rectangular en metros cuadrados, 
# así como su perímetro exterior, también en metros.
"""m1= int(input("introduce el largo del rectangulo: "))
m2= int(input("introduce el ancho del rectangulo: "))

print(f"el area es {m1*m2}m2")
print(f"el perimetro es {2*(m1+m2)}m")

#Escribe un programa en Python que lea un número entero y muestre su último dígito.

n = int(input("introduce un numero entero: "))

print(f"el ultimo digito del numero es {n%10}")

#Escribe un programa que lea un número entero y muestre su penúltimo dígito (el de las decenas).


print(f"el penultimo digito del numero es {(n%100)/10 :.0f}")

#n comerciante vende cajas que pesan 750 g y botellas que pesan 1.2 kg. 
#  Escribe un programa que calcule el peso total de un pedido según el número de cajas y botellas.

caja = int(750)
botella = int(1200)


ncajas= int(input("introduce el numero de cajas: "))
nbotellas = int(input("introduce el numero de botellas: "))
print(f"El peso total del pedido es de {((ncajas*caja)+(nbotellas*botella))/1000}kg")"""""

#Escribe un programa en Python que lea una cantidad total de segundos 
# ntroducida por el usuario y muestre su equivalencia en horas, minutos y segundos. 
# El formato de la salida tiene que ser:

#Introduce segundos: 36128
#horas: 10
#minutos: 2
#segundos: 8

"""segundos_total = int(input("introduce los segundos totales: "))

horas = 0
if segundos_total >=3600 :
   horas= int(segundos_total/3600)
   segundos_total = segundos_total - (3600*horas)

minutos = 0
if segundos_total >=60 :
   minutos= int(segundos_total/60)
   segundos_total = segundos_total -(60*minutos)

print(f"horas: {horas}\nminutos: {minutos}\nsegundos: {segundos_total}")

print(f"horas: {horas}|| minutos: {minutos} || segundos: {segundos_total}")"""

#Escribir un programa que nos pida por teclado una cantidad de dinero "n" 
# y que a continuación escriba la descomposición de "n" 
# en el menor número de billetes y monedas de 100, 50, 20, 10, 5,2 y 1 euro.

"""n = int(input("introduce el numero de dinero: "))
b100=0
if n >= 100 :
    b100 = int(n/100)
    n= n-(100*b100)

b50=0
if n>=50 : 
    b50 = int(n/50)
    n= n-(50*b50)

b20 = 0
if n>=20 :
    b20 = int(n/20)
    n= n -(20*b20)

b10=0
if n>=10 : 
    b10 = int(n/10)
    n = n-(10*b10)
b5=0
if n>=5:
    b5= int(n/5)
    n= n-(5*b5)

b2=0 
if n>=2:
    b2 = int(n/2)
    n=n-(2*b2)"""
#print(f"""billetes de 100: {b100}\nbilletes de 50: {b50}\nbilletes de 20: {b20}\nbilletes de 10: {b10}
#billetes de 5: {b5}\nmonedas de 2: {b2}\nmonedas de 1: {n}""")   

#Escribe un programa que lea tres números y 
# muestre cuál es el mayor y cuál es el menor, utilizando las funciones integradas max() y min().
n1 = int(input("introduce el primer valor: "))
n2 = int(input("introduce el segundo valor: "))
n3 = int(input("introduce el tercer valor: "))

print(f"el mayor es {max(n1,n2,n3)} y el menor es {min(n1,n2,n3)}")