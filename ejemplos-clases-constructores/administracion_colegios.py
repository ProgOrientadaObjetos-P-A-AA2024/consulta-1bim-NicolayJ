# La implementación de clases, objetos, constructores
class administracion_colegios:
    # Constructor
    def __init__(self, nomb, tipo_instit, num_alumn, num_docen):
        self.nombre = nomb
        self.tipo_institucion = tipo_instit
        self.numero_alumnos = num_alumn
        self.numero_docentes = num_docen

    def establecer_nombre(self, nomb):
        self.nombre = nomb

    def establecer_tipo_institucion(self, tipo_instit):
        self.tipo_institucion = tipo_instit

    def establecer_numero_alumnos(self, num_alumn):
        self.numero_alumnos = num_alumn

    def establecer_numero_docentes(self, num_docen):
        self.numero_docentes = num_docen

    def obtener_nombre(self):
        return self.nombre

    def obtener_tipo_institucion(self):
        return self.tipo_institucion

    def obtener_numero_alumnos(self):
        return self.numero_alumnos

    def obtener_numero_docentes(self):
        return self.numero_docentes

# Creación de una instancia de la clase
colegio = administracion_colegios("Colegio Daniel Álvarez Burneo", "Fiscomisional", 1500, 200)

# Impresión de la información del hospital
print("Información del colegio:")
print(f"Nombre: {colegio.obtener_nombre()}")
print(f"Tipo de institución: {colegio.obtener_tipo_institucion()}")
print(f"Número de alumnos: {colegio.obtener_numero_alumnos()}")
print(f"Número de docentes: {colegio.obtener_numero_docentes()}")