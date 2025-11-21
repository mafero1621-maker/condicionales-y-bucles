#aspiranteEjercito

genero = input("¿Cual es el género del aspirante? (M/F) ")
estadoC = input("¿Cual es el estado civil del aspirante? (S/C/V/D/U) ")
estatura = float(input("¿Cual es la estatura del aspirante (en metros)? "))
edad = int(input("¿Cual es la edad del aspirante? "))

if estadoC == "S":
    if genero == "F":
        if estatura > 1.60 and 20 <= edad <= 25:
            print("Eres apta :)")
        else:
            print("No eres apta :(")
    elif genero == "M":
        if estatura > 1.65 and 18 <= edad <= 24:
            print("Eres apto :)")
        else:
            print("No eres apto :(")
    else:
        print("Genero no válido.")
else:
    print("Debes ser soltero para ingresar al ejercito.")
