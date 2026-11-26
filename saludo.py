# Función para saludar a los usuarios
def saludar(nombre_completo):
    if not nombre_completo:
        return "Hola, no ingresaste un nombre."
    return f"Hola {nombre_completo}"

print(saludar("GitHub"))