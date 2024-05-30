baraja = [
    ("As", "Corazones"),
    ("10", "Diamantes"),
    ("Reina", "Picas"),
    ("8", "Tréboles")
]

def agregar_carta(valor, palo):
    carta_nueva = (valor, palo)
    baraja.append(carta_nueva)
    print(f"Se ha agregado la carta {valor} de {palo} a la baraja.")

def remover_carta(valor, palo):
    carta_a_remover = (valor, palo)
    if carta_a_remover in baraja:
        baraja.remove(carta_a_remover)
        print(f"Se ha removido la carta {valor} de {palo} de la baraja.")
    else:
        print(f"La carta {valor} de {palo} no está en la baraja.")

# Agregar una carta y remover otra
agregar_carta("2", "Espadas")
remover_carta("Reina", "Picas")

# Mostrar las cartas actualizadas en la baraja
print("\nCartas en la baraja (actualizadas):")
for valor, palo in baraja:
    print(f"{valor} de {palo}")
