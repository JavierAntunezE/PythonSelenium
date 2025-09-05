# ---------------------------
# Ejemplo de tipos de datos en Python
# ---------------------------

# int (número entero)
edad = 30
print("Edad (int):", edad, type(edad))

# string (cadena de texto)
nombre = "Javier"
print("Nombre (string):", nombre, type(nombre))

# float (número decimal)
altura = 1.75
print("Altura (float):", altura, type(altura))

# bool (valor lógico)
es_programador = True
print("¿Es programador? (bool):", es_programador, type(es_programador))

# list (colección ordenada y mutable)
colores = ["rojo", "verde", "azul"]
print("Lista de colores (list):", colores, type(colores))

# dict (diccionario: pares clave-valor)
persona = {
    "nombre": "Javier",
    "edad": 30,
    "programador": True
}
print("Diccionario persona (dict):", persona, type(persona))

# tuple (colección ordenada e inmutable)
coordenadas = (10.5, 20.3)
print("Coordenadas (tuple):", coordenadas, type(coordenadas))

# ---------------------------
# Ejemplo combinando todo
# ---------------------------

print(f"\nHola, me llamo {nombre}, tengo {edad} años, mido {altura}m.")
print(f"¿Soy programador?: {es_programador}")
print(f"Mis colores favoritos son: {', '.join(colores)}")
print(f"Diccionario persona: {persona}")
print(f"Posición en el mapa: x={coordenadas[0]}, y={coordenadas[1]}")
