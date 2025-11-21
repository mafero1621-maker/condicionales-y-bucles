num = int(input("Ingrese un número mayor que 1: "))

es_primo = True

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        es_primo = False
        break

if es_primo:
    print(num, "es primo")
else:
    print(num, "NO es primo")
