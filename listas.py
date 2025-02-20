# LISTAS [COLECCION DE ELEMENTOS MUTABLES Y ORDENADOS]


            #indices                           # Los indices siemore empiezab a contar desde cero 
#nombre      0 (-6)    1 (-5)     2(-4)      3(-3)       4(-2)    5(-1)
lista1 = [ "Manzana", "Platano", "Pera",  "Mandarina"]
lista2 = [ "Manzana", "Platano" , "Pera",  "Mandarina",  "Fresa", "Piña"]  # puedes poner valores negativos como el -1 y empezara desde el ultimo

print(lista1)   #  output : ['Manzana', 'Banana', 'Pera', 'Manzana']

print(lista1[0])  # output: Manzana
print(lista2[-1]) # output : Mandarina
print(lista2[2:5]) # output :  ['Pera', 'Mandarina', 'Fresa'] empieza desde el 2 pero no toma el 5
print(lista2[:4])  # output: ['Manzana', 'Banana', 'Pera', 'Mandarina']  toma desde el 0 hasta la posicion3 que es mandarina
print(lista2[2:]) # output : ['Pera', 'Mandarina', 'Fresa', 'Piña']
print(lista2[-3:-1])  #output ['Mandarina', 'Fresa']

if "Mandarina" in lista2:
    print("Si, mandarina está en la lista")  # output:  Si, mandarina está en la lista

if "Sandia" in lista2:
    print("Si, mandarina está en la lista")   # output : No aparece nada

# que sucede si cambiamos algunos nombres de lista2
lista2[1] = "Banana"
lista2[4] = "Frutilla"
lista2[5] = " Ananá"   # si se le pone su equivalente en negavtivoque es -1 tambien saldra igual 
# hacemos print
print(lista2) # output : ['Manzana', 'Banana', 'Pera', 'Mandarina', ' Frutilla', ' Ananá']

lista3 = [ "Manzana", "Platano" , "Pera",  "Mandarina",  "Fresa", "Piña"]

lista3[4:] = ["Frutilla","Ananá"] 
print(lista3) # output: ['Manzana', 'Platano', 'Pera', 'Mandarina', 'Frutilla', 'Ananá']

lista3 = [ "Manzana", "Platano" , "Pera",  "Mandarina",  "Fresa", "Piña"]

#INSERT  aegragr o insertar elemento segun la posicion indicada

print(lista3[4])
lista3.insert(2, "Aguacate")
print(lista3[4])
 #  output  saldra
# Fresa
# Mandarina

print(lista3) # output: ['Manzana', 'Platano', 'Aguacate', 'Pera', 'Mandarina', 'Fresa', 'Piña']

# en caso de querer agregar ultimo se utiliza  append

# APPEND AGREGAR ELEMENTO AL FINAL
lista4 = [ "Manzana", "Platano" , "Pera",  "Mandarina",  "Fresa", "Piña"]

print(lista4[4])
lista4.append("Aguacate")
print(lista4[4])

print(lista4)

# output
# fresa
# fresa
# ['Manzana', 'Platano', 'Pera', 'Mandarina', 'Fresa', 'Piña', 'Aguacate']


ListaA = ["Manzana", "Platano", "Pera"]
ListaB =["Mandarina", "Fresa", "Piña"]

ListaA.extend(ListaB)
print(ListaA) # output: ['Manzana', 'Platano', 'Pera', 'Mandarina', 'Fresa', 'Piña']


ListaA = ["Manzana", "Platano", "Pera"]
tupla =["Mandarina", "Fresa", "Piña"]

ListaA.extend(tupla)
print(ListaA) # # output: ['Manzana', 'Platano', 'Pera', 'Mandarina', 'Fresa', 'Piña'] 
# aparece lo mismo ya que la tupla es inmutable pero puede utilizarse para extenderse


lista4 = [ "Manzana", "Platano" , "Pera",  "Mandarina",  "Fresa", "Piña"]

# se quiere borrar un elemento como fresa 
# MEDIANTE LA FUNCION REMOVE

lista4.remove("Fresa")
print(lista4) # output: ['Manzana', 'Platano', 'Pera', 'Mandarina', 'Piña']  
# remove borra la primera ocurrencia del valor 

# FUNCION POP 

lista4.pop(2)

print(lista4) # retiro el elemnto que estaba en la posicion 2 (Pera)

lista4.pop() # borra el ultimo elemento 

# DEl
lista5 = [ "Manzana", "Platano" , "Pera",  "Mandarina",  "Fresa", "Piña"]
del lista5[3]

print(lista5) # otro forma de eliminar el elemnto de la posicion 3 de la lista


# clear
lista4.clear()
print (lista4) # output: []  deja la lista vacia
