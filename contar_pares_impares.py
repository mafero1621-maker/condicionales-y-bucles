pares = 0
impares = 0

while True:
    n = int(input("Ingrese número (0 para terminar): "))

    if n == 0:
        break

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Impares:", impares)
