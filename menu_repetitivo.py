while True:
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "3":
        print("Saliendo...")
        break

    n1 = float(input("Ingrese primer número: "))
    n2 = float(input("Ingrese segundo número: "))

    if opcion == "1":
        print("Resultado:", n1 + n2)
    elif opcion == "2":
        print("Resultado:", n1 - n2)
    else:
        print("Opción inválida")
