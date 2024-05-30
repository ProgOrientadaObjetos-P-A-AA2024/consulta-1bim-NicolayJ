receta_torta = [
    "Harina",
    "Azúcar",
    "Huevos",
    "Leche",
    "Mantequilla",
    "Polvo de hornear"
]

def agregar_ingrediente(ingrediente):
    receta_torta.append(ingrediente)
    print(f"{ingrediente} ha sido agregado a la receta de la torta.")

def remover_ingrediente(ingrediente):
    if ingrediente in receta_torta:
        receta_torta.remove(ingrediente)
        print(f"{ingrediente} ha sido removido de la receta de la torta.")
    else:
        print(f"{ingrediente} no está en la receta de la torta.")

# Agregar un ingrediente y remover otro
agregar_ingrediente("Vainilla")
remover_ingrediente("Leche")

# Mostrar la receta de la torta actualizada
print("\nIngredientes para la torta (actualizados):")
for ingrediente in receta_torta:
    print(ingrediente)
