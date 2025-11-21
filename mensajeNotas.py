#decisionesNotasdefinitivas

nota = float(input("Escribe tu nota definitiva: "))

if nota < 3.0:
    print("Tu nota es Insuficiente :(")
elif nota <= 3.5:
    print("Tu nota es Aceptable")
elif nota <= 4.0:
    print("Tu nota es Sobresaliente")
else:
    print("Tu nota es Excelente :)")
