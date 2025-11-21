
numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    
    cifras = len(str(numero))
    
    
    suma = 0
    temp = numero
    while temp > 0:
        digito = temp % 10
        suma += digito ** cifras
        temp //= 10
    
    
    if suma == numero:
        print(f"\nEl número {numero} ES un número de Armstrong.")
    else:
        print(f"\nEl número {numero} NO es un número de Armstrong.")
else:
    print("\nDebe ingresar un número positivo.")
