
minimoValor = int(input("Ingrese el valor mínimo del intervalo: "))
maximoValor = int(input("Ingrese el valor máximo del intervalo: "))
x = int(input("Ingrese el número a verificar: "))

if minimoValor <= x <= maximoValor:
    print(f"El número {x} está DENTRO del intervalo [{minimoValor}, {maximoValor}].")
else:
    print(f"El número {x} está FUERA del intervalo [{minimoValor}, {maximoValor}].")
