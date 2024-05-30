class Estudiante:
    def __init__(self, nombre, edad, materia):
        self.nombre = nombre
        self.edad = edad
        self.materia = materia

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Materia: {self.materia}")

# Crear una instancia de Estudiante 1
estudiante = Estudiante("María", 20, "Programación Orientada a Objetos")
estudiante.mostrar_informacion()

# Crear otra instancia de Estudiante 2
otro_estudiante = Estudiante("Juan", 19, "Estructura de Datos")
otro_estudiante.mostrar_informacion()
