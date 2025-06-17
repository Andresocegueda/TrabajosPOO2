import math
from excepciones import FraccionException

class Fraccion:
    def __init__(self, numerador, denominador):
        if not isinstance(numerador, int) or not isinstance(denominador, int):
            raise FraccionException("Error: El numerador y el denominador deben ser enteros.")
        
        if denominador == 0:
            raise FraccionException("Error: El denominador no puede ser cero.")
        
        # Encontrar el Máximo Común Divisor para simplificar
        divisor_comun = math.gcd(numerador, denominador)
        
        
        self.numerador = numerador // divisor_comun
        self.denominador = denominador // divisor_comun

        
        if self.denominador < 0:
            self.numerador = -self.numerador
            self.denominador = -self.denominador
            

    def __str__(self):
        """Representación en cadena de la fracción."""
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra_fraccion):
        """Suma dos fracciones."""
        nuevo_num = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_den = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __sub__(self, otra_fraccion):
        """Resta dos fracciones."""
        nuevo_num = self.numerador * otra_fraccion.denominador - otra_fraccion.numerador * self.denominador
        nuevo_den = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __mul__(self, otra_fraccion):
        """Multiplica dos fracciones."""
        nuevo_num = self.numerador * otra_fraccion.numerador
        nuevo_den = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __truediv__(self, otra_fraccion):
        """Divide dos fracciones."""
        if otra_fraccion.numerador == 0:
            raise FraccionException("Error: División por una fracción nula (cero) no permitida.")
        
        nuevo_num = self.numerador * otra_fraccion.denominador
        nuevo_den = self.denominador * otra_fraccion.numerador
        return Fraccion(nuevo_num, nuevo_den)