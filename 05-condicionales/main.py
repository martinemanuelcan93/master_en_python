"""
# condicional IF

Si se_cumple_esta_condicion : 
 Ejecutar grupo de instrucciones
 SI NO:
  Se ejecutan otro grupo de instrucciones 

  if condicion:
      instrucciones 
else:
     otras instrucciones

"""
"""
# operadores de comparacion 
==
!=
<
>
>=
<=
"""
"""
# Ejemplo 1 
print("###### EJEMPLO 1 #######")

color = "rojo"
color = input("cual es mi color favorito?") 

if color == "rojo":
    print("Bien el color es rojo!")
else: print("el color no es el correcto, deberas morir empleado")


#Ejemplo 2 

print("#####  EJEMPLO 2 #####")

year = int(input("en que año estamos?"))

if year >= 2021: 
    print("Hostia viajero del pasado, valla que la has pegado")
else:
    print("Hostia eso sucedió hace mucho tiempo atrás")
        


# Ejemplo 3

print("\n#### ejemplo 3 #####")

nombre = "Martin Maldonado"
ciudad = "Argentina"
continente = "America"
mayoria_de_edad = 18


edad = int(input(" \"Completa el formulario :\" \n Cuantos años tenes ?"))
if edad >= mayoria_de_edad :
   print("Sos mayor ya podes ir preso !")
else: print("anda a dormir sos un nene de mama xD " )
# ejemplo 4

print("\##### ejemplo 4 ###")

dia = int(input("introduce dia de la semana "))

"""
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("es miercoles")
"""
"""
if dia == 1:
    print("es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")    
# es lo mismo que arriba pero acotado como hablar acortando palabras

"""
# EJEMPLO 5
"""
edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("Para saber si podes recibir la beca: \n cuantos años tenes?"))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("estas en edad de recibir una beca")
else:
    print("no estas en edad de recibir una beca")
"""
# EJEMPLO 6

pais = input("En que pais naciste?")
nacionalidad = ("Latinoamericano/a")
nacionalidad1 = ("Europeo")

if not (pais == "Mexico" or pais == "Argentina" or pais == "Chile" or pais == "Bolivia"):
    print (f"sos  europeo probablemente ")
else:
    print(f"seguro eres {nacionalidad}")
