"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han suspendido.
"""

contador = 0
aprobados = 0
reprobados = 0


numero_alumnos = int(input("cuantos alumnos tienes ? "))

while contador <= numero_alumnos:
    nota = int(input(f"que nota quieres ponerle al \"alumno {contador}\""))
    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1

    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados : {reprobados}")

