
print("Ingrese las cinco notas del estudiante (entre 0.0 y 5.0):")
notas = []  

for i in range(1, 6):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)


promedio = sum(notas) / 5


print(f"\nLa nota definitiva es: {promedio:.2f}")

if promedio > 3.5:
    print(" :D El estudiante GANÓ el curso.")
else:
    print(":(  El estudiante PERDIÓ el curso.")
