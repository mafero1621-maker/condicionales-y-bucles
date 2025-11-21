#descuentoArticulo

costo= float(input("Escribe el costo del artículo "))

if costo > 150000:
    dto = costo * 0.05
    print("Tu descuento es de ", dto)
else:
    dto = 0
    print("No aplica el descuento. Tu valor a pagar es", costo)
