from fraccion import Fraccion
from excepciones import FraccionException

def leer_fraccion(nombre_fraccion):
    """
    Lee un numerador y denominador desde la entrada del usuario
    y devuelve un objeto Fraccion. Maneja errores de entrada.
    """
    print(f"\n--- Ingrese los datos para la {nombre_fraccion} ---")
    while True:
        try:
            numerador = int(input("Introduce el numerador (entero): "))
            denominador = int(input("Introduce el denominador (entero y distinto de cero): "))
            # El constructor de Fraccion lanzará FraccionException si el denominador es 0
            return Fraccion(numerador, denominador)
        except ValueError:
            # Esta excepción ocurre si int() falla (ej: se ingresa texto)
            print("Error: Por favor, ingrese únicamente números enteros.")
        except FraccionException as e:
            # Esta es nuestra excepción personalizada (denominador cero)
            print(f"{e}")
            # Volvemos a empezar el bucle para pedir los datos de esta fracción de nuevo

def main():
    """Función principal para la calculadora interactiva de fracciones."""
    print("--- Calculadora de Fracciones ---")
    
    while True:
        try:
            # Leer las dos fracciones del usuario
            f1 = leer_fraccion("primera fracción")
            f2 = leer_fraccion("segunda fracción")

            print(f"\nFracción 1: {f1}")
            print(f"Fracción 2: {f2}")
            
            # Realizar y mostrar todas las operaciones
            print("\n--- Resultados ---")
            suma = f1 + f2
            print(f"{f1} + {f2} = {suma}")

            resta = f1 - f2
            print(f"{f1} - {f2} = {resta}")
            
            multiplicacion = f1 * f2
            print(f"{f1} * {f2} = {multiplicacion}")

            # Manejar la división por cero de forma específica
            try:
                division = f1 / f2
                print(f"{f1} / {f2} = {division}")
            except FraccionException as e:
                # Captura el error de división por cero
                print(f"Error en la división: {e}")

        except Exception as e:
            # Captura cualquier otro error inesperado (aunque es poco probable)
            print(f"Ha ocurrido un error inesperado: {e}")

        # Preguntar al usuario si desea continuar
        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            break

    print("\nPrograma finalizado.")

if __name__ == "__main__":
    main()