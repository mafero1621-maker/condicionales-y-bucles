
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

android = 0
ios = 0
no_validos = 0
contador = 0

while contador < cantidad_estudiantes:
    print("\n--- Estudiante", contador + 1, "---")
    codigo = input("Ingrese el código del estudiante: ")
    eleccion = input("Ingrese su plataforma preferida (Android / iOS): ").strip().lower()
    
    if eleccion == "android":
        android += 1
    elif eleccion == "ios":
        ios += 1
    else:
        print("⚠️ Plataforma no válida. Este voto no será tenido en cuenta.")
        no_validos += 1

    contador += 1

print("\n--- RESULTADOS FINALES ---")
print("Votos por Android:", android)
print("Votos por iOS:", ios)
print("Votos no válidos:", no_validos)

if android > ios:
    print("\n La plataforma seleccionada es: ANDROID")
elif ios > android:
    print("\n La plataforma seleccionada es: iOS")
else:
    print("\n Hay un EMPATE, se debe usar otro mecanismo de elección.")
