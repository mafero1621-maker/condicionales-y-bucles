n = int(input("Ingrese número: "))

for i in range(n, -1, -1):
    if i % 7 == 0 and i != 0:
        print(i, "← múltiplo de 7 ⚠️")
    else:
        print(i)
