class administracion_hospitales:
    # Constructor
    def __init__(self, nombre, tipo_hospital, numero_pacientes, numero_doctores):
        self.nombre = nombre
        self.tipo_hospital = tipo_hospital
        self.numero_pacientes = numero_pacientes
        self.numero_doctores = numero_doctores

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_tipo_hospital(self, tipo_hospital):
        self.tipo_hospital = tipo_hospital

    def establecer_numero_pacientes(self, numero_pacientes):
        self.numero_pacientes = numero_pacientes

    def establecer_numero_doctores(self, numero_doctores):
        self.numero_doctores = numero_doctores

    def obtener_nombre(self):
        return self.nombre

    def obtener_tipo_hospital(self):
        return self.tipo_hospital

    def obtener_numero_pacientes(self):
        return self.numero_pacientes

    def obtener_numero_doctores(self):
        return self.numero_doctores

# Creación de una instancia de la clase
hospital = administracion_hospitales("Hospital General Isidro Ayora", "Público", 1600, 500)

# Impresión de la información del hospital
print("Información del hospital:")
print(f"Nombre: {hospital.obtener_nombre()}")
print(f"Tipo de hospital: {hospital.obtener_tipo_hospital()}")
print(f"Número de pacientes: {hospital.obtener_numero_pacientes()}")
print(f"Número de doctores: {hospital.obtener_numero_doctores()}")
