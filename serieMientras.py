
n = int(input("Ingrese la cantidad de términos de la serie: "))

contador = 1
numero = 1

print("La serie es:")
while contador <= n:
    print(numero)
    numero = numero + 2
    contador = contador + 1
