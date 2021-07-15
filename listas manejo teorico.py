lista = ["jose", "jose" , 33 , 56.7 , True, "jose@gmail.com"]

#Agrega elemento al final de la lista
lista.append("casado")
#Agrega más de un elemento al final de la lista
lista.extend([44, "Jardin"])
#Agrega un elemento en la posición que se indique
lista.insert(0,"Juan")
#Elimina o borra un elemento
lista.remove(True)
#Cuenta los elementos de una lista
repetidos = lista.count("jose")
print(repetidos)
#Ordena lista de numeros
num = [3,4,1,34]
num.sort()
#Ordena lista de numeros en reversa
num.reverse()
#Elimina algo de la lista
del num[3]


