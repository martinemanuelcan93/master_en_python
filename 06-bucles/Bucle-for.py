"""
# FOR 
for variable in elemento iterable (lista, rango, etc.)
     BLOQUE DE INSTRUCCIONES 
"""
"""
contador = 0 
resultado = 0

for contador in range(0, 10):   
    print("voy por el "+ str(contador))

    resultado =  resultado + contador
 

    print(f" El resultado es : {resultado}")


resultado = resultado + contador 
    1           0          1
resultado = resultado + contador
    3           1          2     

"""  
# Ejemplo tablas de mutliplicar

print("\n##### EJEMPLO ######")

numero_usuario = int(input("de que numero quieres la tabla?"))

if numero_usuario < 1 :
    numero_usuario = 1

print(f" ### tabla de multiplicar del numero {numero_usuario}")

for numero_tabla in range(1,11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("tabla finalizada.")
