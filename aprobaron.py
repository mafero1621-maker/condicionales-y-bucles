
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

contador_estudiantes = 0
aprobados = 0
reprobados = 0
suma_definitivas = 0

while contador_estudiantes < cantidad_estudiantes:
    codigo = input("\nIngrese el código del estudiante: ")
    nota = float(input("Ingrese la nota definitiva: "))
    
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1
    
    suma_definitivas += nota
    contador_estudiantes += 1

promedio_grupo = suma_definitivas / cantidad_estudiantes

print("\n--- Resultados ---")
print("Cantidad que aprobaron:", aprobados)
print("Cantidad que reprobaron:", reprobados)
print("Promedio del grupo:", round(promedio_grupo, 2))
