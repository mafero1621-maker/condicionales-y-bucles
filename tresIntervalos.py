
a1, b1 = map(int, input("Ingrese los límites del primer intervalo (a1 b1): ").split())
a2, b2 = map(int, input("Ingrese los límites del segundo intervalo (a2 b2): ").split())
a3, b3 = map(int, input("Ingrese los límites del tercer intervalo (a3 b3): ").split())

x = int(input("Ingrese el número a verificar: "))

if (a1 < x < b1) or (a2 < x < b2) or (a3 < x < b3):
    print(f"El número {x} está DENTRO de al menos uno de los intervalos.")
else:
    print(f"El número {x} está FUERA de todos los intervalos.")
