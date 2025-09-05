# ---------------------------
# Ejemplo con funciones y manejo de excepciones
# ---------------------------

# Definimos una función para calcular el IMC
def calcular_imc(peso, altura):
    try:
        # Fórmula IMC = peso / altura^2
        imc = peso / (altura ** 2)
        return round(imc, 2)  # Redondeamos a 2 decimales
    except ZeroDivisionError:
        # Manejo de error si la altura es 0
        return "Error: la altura no puede ser 0"
    except TypeError:
        # Manejo de error si los datos no son numéricos
        return "Error: peso y altura deben ser números"

# Función que interpreta el resultado del IMC
def interpretar_imc(imc):
    if isinstance(imc, str):
        # Si recibimos un mensaje de error, lo devolvemos tal cual
        return imc
    elif imc < 18.5:
        return f"IMC={imc} → Bajo peso"
    elif 18.5 <= imc < 25:
        return f"IMC={imc} → Peso normal"
    elif 25 <= imc < 30:
        return f"IMC={imc} → Sobrepeso"
    else:
        return f"IMC={imc} → Obesidad"

# ---------------------------
# Pruebas
# ---------------------------
print("Caso válido:")
imc_valido = calcular_imc(70, 1.75)  # peso=70kg, altura=1.75m
print(interpretar_imc(imc_valido))

print("\nCaso con altura = 0:")
imc_error = calcular_imc(70, 0)  # Provoca ZeroDivisionError
print(interpretar_imc(imc_error))

print("\nCaso con datos no numéricos:")
imc_error_tipo = calcular_imc("70kg", 1.75)  # Provoca TypeError
print(interpretar_imc(imc_error_tipo))
