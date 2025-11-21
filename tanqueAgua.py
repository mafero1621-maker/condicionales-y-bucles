
litros = float(input("Ingrese la cantidad actual de litros en el tanque: "))

if litros < 250:
    print("Abrir la llave. El nivel de agua es bajo.")
elif litros > 450:
    print("Cerrar la llave. El tanque está lleno.")
else:
    print("Mantener la llave como está. Nivel adecuado.")
