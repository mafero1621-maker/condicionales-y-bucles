#tablaMultiplicar

while True:
    print("\n=== REPASO DE TABLAS DE MULTIPLICAR ===")
    

    tabla = int(input("¿Qué tabla deseas repasar? (1 a 20) "))
    
    if tabla < 1 or tabla > 20:
        print("Por favor elige una tabla entre 1 y 20.")
        continue
    
    print(f"\nRepasemos la tabla del {tabla}!\n")
    
    aciertos = 0  
    i = 1        
    
    while i <= 10:
        respuesta = int(input(f"{tabla} x {i} = "))
        resultado = tabla * i
        
        if respuesta == resultado:
            print("¡Muy bien! Respuesta correcta.")
            aciertos += 1
        else:
            print(f" Incorrecto. El resultado correcto es {resultado}.")
        i += 1
    
    print("\nTu puntuación final es:", aciertos, "de 10.")
    
    if aciertos <= 5:
        valoracion = "Insuficiente"
    elif aciertos <= 7:
        valoracion = "Aceptable"
    elif aciertos <= 9:
        valoracion = "Sobresaliente"
    else:
        valoracion = "Excelente"
    
    print(f"Tu valoración: {valoracion}")
    
    otra = input("\n¿Deseas repasar otra tabla? (s/n) ").lower()
    if otra != "s":
        print("\nGracias por practicar. ¡Hasta pronto! ")
        break
