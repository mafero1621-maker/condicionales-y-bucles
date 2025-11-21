suma = 0

while True:
    num = int(input("Ingrese número (0 para terminar): "))

    if num == 0:
        break
    
    if num < 0:
        continue

    suma += num

print("La suma de positivos es:", suma)
