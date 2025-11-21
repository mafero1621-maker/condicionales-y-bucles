clave_correcta = "abc123"
intentos = 0

while intentos < 3:
    clave = input("Ingrese clave: ")

    if clave == clave_correcta:
        print("Acceso permitido")
        break
    else:
        print("Clave incorrecta")
        intentos += 1

if intentos == 3:
    print("Acceso denegado. Demasiados intentos.")
