"""
Ejercicio 8. Cuanto es el X por ciento de X numero ?
                        20% de 150 
"""

numero = int(input("Hey tu !! Introduce el numero a calcular: "))
porcentaje =int(input(f"¿que porcentaje quieres sacar de {numero}?  " ))

operacion = (numero * (porcentaje/100))
print(f"el {porcentaje}% de {numero} es : {operacion}")

mano = ( numero -  operacion)

