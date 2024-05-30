class Pelicula:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def mostrar_duracion(self):
        horas = self.duracion // 60
        minutos = self.duracion % 60
        print(f"Duración de {self.titulo}: {horas} horas {minutos} minutos")

# Crear una instancia de Pelicula
pelicula = Pelicula("Whiplash", 106)
pelicula.mostrar_duracion()

# Crear otra instancia de Pelicula 2 
pelicula2 = Pelicula("El Padrino", 175)
pelicula2.mostrar_duracion()