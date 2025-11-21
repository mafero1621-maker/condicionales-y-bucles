#factorial

n = int(input("Ingresa un número entero: "))

if n < 0:
    print("Los números negativos no tienen factorial.")
else:
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        i += 1

    print(f"El factorial de {n} es: {factorial}")
