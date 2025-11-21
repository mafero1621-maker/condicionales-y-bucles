

costo = float(input("Ingrese el costo del artículo: "))

if costo > 150000:
    descuento = costo * 0.05
    total = costo - descuento
    print(f"El artículo tiene un descuento de: ${descuento:.2f}")
    print(f"El precio final es: ${total:.2f}")
else:
    print(f"El artículo no tiene descuento. Su valor es: ${costo:.2f}")
