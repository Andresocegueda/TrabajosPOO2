
class persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.__correo = correo
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.__correo}")

class estudiante(persona):
    def __init__(self, matricula):
        super().__init__("Andres", 22, "Andresocegueda1.d@gmail.com")
        self.__matricula = matricula
    def inscribir_curso(self, curso):
        self.curso = []
        self.curso.append(curso)
        print(f"El estudiante se añadió al curso: {curso}")
class profesor(persona):
    def __init__(self, especialidad):
        super().__init__("José", 45, "EstoEsUnEjemplo@gmail.com")
        self.especialidad = especialidad
    def asignar_curso(self, curso):
        self.curso = []
        self.curso.append(curso)
        print(f"Se asignó un curso al profesor: {curso}")
    def mostrar_asignaciones(self):
        print(f"El profesor {self.nombre} tiene asignados los cursos: {self.curso}")
class curso():
    def __init__(self, nombre, clave, creditos):
        self.nombre = nombre
        self.clave = clave
        self.creditos = creditos
    def descripcion(self):
        print(f"Nombre del curso: {self.nombre}, Código: {self.clave}, Créditos: {self.creditos}")

Alumno1 = estudiante("230281") #Crea un objeto de la clase estudiante
Profesor1 = profesor("Matemáticas") #Crea un objeto de la clase profesor
Curso1 = curso("Matemáticas", 1234, 4) #Crea un objeto de la clase curso
Curso2 = curso("Física", 5678, 4) #Crea otro objeto de la clase curso
Alumno1.inscribir_curso(Curso1.nombre) #Inscribe al alumno a un curso
Alumno1.inscribir_curso(Curso2.nombre) #Inscribe al alumno a otro curso
Profesor1.asignar_curso(Curso1.nombre) #Asigna un curso al profesor
Profesor1.asignar_curso(Curso2.nombre) #Asigna otro curso al profesor
Alumno1.mostrar_datos() #Muestra los datos del alumno
Profesor1.mostrar_asignaciones() #Muestra los cursos asignados al profesor
Curso1.descripcion() #Muestra la descripción del curso