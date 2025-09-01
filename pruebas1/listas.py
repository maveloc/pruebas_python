#LISTAS
lista = ["manzana", "platano","esquina"]
print(lista)
print(lista[0])

#con la lista . se pueden ver cosas que hacer como meter elementos en index especificos...
lista2 = ["hueso", "palo", "ruido"]
lista.extend(lista2)
print(lista)
lista.sort() #si queremos hacerla inversa es sort(reverse = true)
print(lista)

#RECORRER UNA LISTA
for x in lista:
    print(x)

for i in range (len(lista)):
    print(lista[i])

#Comprension de una lista si queremos hacer una lista a partir de una ya existente
lista3 = [x for x in lista if "o" in x]
print(lista3)

#para copiar listas usa lista4 = lista3[:]
#para mas mejor mirar los metodos de las listas en la documentacion o echar un vistazo haciendo lista.
