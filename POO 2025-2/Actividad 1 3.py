def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):  
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

while True:
    try:
        num = float(input("Escribe un número: "))
        break
    except ValueError:
        print("Entrada inválida. Solo se permiten números.")

while True:
    try:
        opcion = int(input("""Elija una opción: 
1.- suma 
2.- resta
3.- multiplicación
4.- división
Opción: """))
        
        if opcion not in [1, 2, 3, 4]:
            print("Opción inválida.")
            continue

        while True:
            try:
                num2 = float(input("Escribe otro número: "))
                if opcion == 4 and num2 == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero.")
                break
            except ValueError:
                print("Entrada inválida. Solo se permiten números.")
            except ZeroDivisionError as e:
                print(f"{e}")

        match opcion:
            case 1:
                resultado = suma(num, num2)
                print(f"La suma de {num} y {num2} es: {resultado}")
            case 2:
                resultado = resta(num, num2)
                print(f"La resta de {num} y {num2} es: {resultado}")
            case 3:
                resultado = multiplicacion(num, num2)
                print(f"La multiplicación de {num} y {num2} es: {resultado}")
            case 4:
                resultado = division(num, num2)
                print(f"La división de {num} y {num2} es: {resultado}")
        break
    except ValueError:
        print("Debes ingresar un número entero para la opción.")