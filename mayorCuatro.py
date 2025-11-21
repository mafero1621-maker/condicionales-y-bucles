#cuatroNumeros

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))
num3 = int(input("Escribe el tercer numero: "))
num4 = int(input("Escribe el cuarto numero: "))


if (num1 == num2) and (num1 == num3) and (num1 == num4):
    print("Todos los numeros son iguales")
else:
    if (num1 > num2) and (num1 > num3) and (num1 > num4):
        print("El numero mayor es", num1)
    elif (num2 > num1) and (num2 > num3) and (num2 > num4):
        print("El numero mayor es", num2)
    elif (num3 > num1) and (num3 > num2) and (num3 > num4):
        print("El numero mayor es", num3)
    else:
        print("El numero mayor es", num4)
