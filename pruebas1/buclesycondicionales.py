x= 50
y=20 
#if else, mitico, no hay fallo
if x<y:
    print("a")
else: 
    print ("b")

#match case es lo mismo que switch case
dia = 3

match dia:
    case 1 | 2 | 4 | 5 if x == 50:
        print ("sabado")
    case 3:
        print("lunes")
    case _:
        print("Julio")

#while loops
i=0
while i < 10:
    i+=1
    print(i)
    if i == 10:
        continue #con continue rompemos el bucle, con un else al final puedes hacer algo
    #cuando se ha cumplico la condicion del while

#y los bucles for... pues bucles for
cesta = ["lechuga","tofu","kiwi"]
for x in cesta:
    print(x)
    if x == "tofu":
        break

    


