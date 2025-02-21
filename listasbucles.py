# LISTAS COLECCION DE ELEMENTOS MUTABLES Y ORDENADOS

            #indices
#nombre      0 (-6)    1 (-5)     2(-4)      3(-3)       4(-2)    5(-1)

#frutas = [ "Manzana", "Platano" , "Pera",  "Mandarina",  "Fresa", "Piña"]

# FROMA ABREVIADA O SHORTHAND
#[print(fruta) for fruta in frutas] # IMPRIME UNA FRUTA POR CADA LINEA 


# BLUCLE FOR
#for fruta in frutas:
#  print(fruta) # imprime una fruta por linea 

# BUCLE FOR CON INDICE DISPONIBLE
#for i in range(len(frutas)):
#   print(frutas[i])

#len(frutas) # va a dar el tamaño de la lista 

##print(len(frutas)) # output: 6 ( contabiliza la cantidad de elementos que hay en la lista "frutas")

#print(range(6)) # output: range(0, 6) 

#for i in range(6):
#   print(i) # contabiliza del 0 al 5 colocando un numero por cada linea 
   # output:     0
   #             1
   #             2
   #             3
   #             4
   #             5

# BUCLE WHILE
# i = 0 
#while i <  len(frutas):
#    print(frutas[i])
#    i += 1
# output: 
           # Manzana
           # Platano
           # Pera
           # Mandarina
           # Fresa
           # Piña
frutas = [ "Manzana", "Platano" , "Pera",  "Mandarina",  "Fresa", "Piña"]
#frutas_con_e = []



#for fruta in frutas:
    #if "e" in fruta:
        #frutas_con_e.append(fruta)

#print(frutas_con_e) # output:  ['Pera', 'Fresa']

# forma abreviada

#               dato a 
# nombre        asignar    bucle            condicion
frutas_con_e = [fruta for fruta in frutas if "e" in fruta]
print(frutas_con_e) # tambien sale lo mismo que la forma anterior 