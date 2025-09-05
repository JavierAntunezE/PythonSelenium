# ---------------------------
# Ejemplo con if/else, for y while
# ---------------------------

# Variables base
edad = 20
colores = ["rojo", "verde", "azul"]
contador = 0

# if/else -> validar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# for -> recorrer lista de colores
print("\nColores favoritos:")
for color in colores:
    print("-", color)

# while -> contar hasta 5
print("\nContador con while:")
while contador < 5:
    print("Número:", contador)
    contador += 1
