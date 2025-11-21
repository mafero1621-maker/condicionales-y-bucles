#tabla

n = int(input("Ingresa el valor de n: "))

i = 1

print("Columna 1\tColumna 2\tColumna 3")


while i <= n:
    col1 = i            
    col2 = i ** 2       
    col3 = i * 2 + (i - 1)  

    print(f"{col1}\t\t{col2}\t\t{col3}")
    i += 1
