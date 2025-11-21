
precio = float(input("Ingrese el precio del artículo: "))
print("Ingrese el tipo de artículo:")
print("1 - Textil")
print("2 - Electrodoméstico")
print("3 - Elementos de cocina")
print("4 - Video juego")
tipo = int(input("Tipo: "))


if tipo == 1:
    descuento = 0      # 0 %
elif tipo == 2:
    descuento = 0.037  # 3.7 %
elif tipo == 3:
    descuento = 0.042  # 4.2 %
elif tipo == 4:
    descuento = 0.078  # 7.8 %
else:
    print("Tipo no válido")
    exit()  


monto_descuento = precio * descuento
precio_final = precio - monto_descuento


print(f"El descuento aplicado es: ${monto_descuento:.2f}")
print(f"El precio final del artículo es: ${precio_final:.2f}")
