
numero = int(input("Ingrese un número entero: "))

if numero > 0:
    
    cifras = len(str(numero))
    
    
    suma_cifras = 0
    temp = numero
    while temp > 0:
        digito = temp % 10
        suma_cifras += digito
        temp //= 10
    
   
    print("\nEl número es positivo.")
    print("Cantidad de cifras:", cifras)
    print("Suma de las cifras:", suma_cifras)
else:
    print("\nEl número no es positivo.")
