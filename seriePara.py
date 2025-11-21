# serie para

n = int(input("Ingresa el valor de n: "))

i = 1

print("Serie generada:")

while i <= n:
    print(i, end=", " if i + 2 <= n else "")
    i += 2
