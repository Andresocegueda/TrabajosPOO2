import math

def calcular_raices(a, b, c):
    # Validar que 'a' no sea cero
    if a == 0:
        raise ValueError("Error: El coeficiente 'a' no puede ser cero. Esto no es una ecuación cuadrática.")

    # Calcular el discriminante
    discriminante = (b**2) - (4*a*c)

    # Validar que las raíces sean reales
    if discriminante < 0:
        raise ValueError("Error: El discriminante es negativo. La ecuación no tiene soluciones reales.")
    
    # Calcular las raíces
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    return raiz1, raiz2

def main():
    """Función principal para la interacción con el usuario."""
    print("--- Calculadora de Ecuaciones Cuadráticas (ax² + bx + c = 0) ---")
    
    while True:
        try:
            # Leer y convertir coeficientes
            try:
                a = float(input("\nIntroduce el coeficiente 'a': "))
                b = float(input("Introduce el coeficiente 'b': "))
                c = float(input("Introduce el coeficiente 'c': "))
            except ValueError:
                # Se lanza si la conversión a float falla
                raise TypeError("Error: Todos los coeficientes deben ser números válidos.")

            # Calcular e imprimir las raíces
            raiz1, raiz2 = calcular_raices(a, b, c)
            
            print("\nResultados:")
            
            if raiz1 == raiz2:
                print(f"La ecuación tiene una única raíz real: x = {raiz1}")
            else:
                print(f"Las raíces reales son: x₁ = {raiz1} y x₂ = {raiz2}")

        except (ValueError, TypeError) as e:
            # Captura las excepciones de lógica (a=0, disc<0) y de tipo de dato
            print(f"\n{e}")
            # Preguntar si desea continuar solo si el error es por discriminante negativo
            if "discriminante es negativo" in str(e):
                continuar = input("¿Deseas intentar con otros coeficientes? (s/n): ").lower()
                if continuar != 's':
                    break
        else:
            continuar = input("\n¿Deseas calcular otra ecuación? (s/n): ").lower()
            if continuar != 's':
                break
    print("\nUsted ha salido de la aplicación...")

if __name__ == "__main__":
    main()