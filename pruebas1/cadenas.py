#CADENAS Y CONCATENACIONES
#para poner multilinea se usan 3 ""
multicadena = """ habia un cerdito que me dijo una vez
que por mucho que quisiera
no tendria su casa
"""
print(multicadena)

#partiendo una cadena (va desde DONDE eliges hasta DONDE eliges (ultimo no incluido))
print(multicadena[0:17])
print(multicadena[-5:-2])

#modificando cadenas
print(multicadena.upper())
print(multicadena.strip())#quita el espacio antes y despues de que empiece el texto

print(multicadena.replace("a","i").strip())
print(multicadena.split(" "))

edad=23
texto= f"tengo {edad} años"
print(texto)

precio=59.99
texto= f"el articulo cuesta {precio:.2f}€, me parece caro" #el .2f añade 2 decimales
print(texto)

#\'	Single Quote
#\\	Backslash
#\n	New Line
#\r	Carriage Return
#\t	Tab
#\b	Backspace
#\f	Form Feed
#\ooo	Octal value
#\xhh	Hex value

#Para metodos de strings mirar la documentacion (hay un cristo)