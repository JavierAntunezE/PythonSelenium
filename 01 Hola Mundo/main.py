
def nombre_funcion(parametros):
    """Docstring: descripción de lo que hace la función"""
    # Bloque de código
    return resultado


area = calcular_area_rectangulo(5.0, 3.0)
print(area)  # Resultado: 15.0


def saludar(nombre="invitado"):
    print(f"Hola, {nombre}!")

saludar()           # Hola, invitado!
saludar("Ana")      # Hola, Ana!

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura

try:
    # Código que puede fallar
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero.")


conexion = None
try:
    conexion = conectar_base_datos()
    datos = conexion.obtener_datos()
except ConnectionError:
    print("Error de conexión")
else:
    print("Datos obtenidos correctamente")
finally:
    # Cerrar conexión siempre, haya error o no
    if conexion:
        conexion.cerrar()
    print("Recursos liberados")


    def validar_edad(edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")

        try:
            # This will raise a ValueError
            print(int("xyz"))
        except Exception as e:
            print(f"Caught an exception: {type(e).__name__}")


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "usuario"))
)


driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Se aplica a TODOS los find_element()

# Todos estos métodos usarán la espera de 10 segundos
driver.find_element(By.ID, "elemento1")
driver.find_element(By.CLASS_NAME, "mi-clase")
driver.find_elements(By.TAG_NAME, "div")

# Espera hasta 10s para encontrar el elemento
boton = driver.find_element(By.ID, "mi-boton")

# Pero si el botón no es clickeable, falla inmediatamente
boton.click()  # Puede fallar si el botón está deshabilitado


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Esperar hasta que se cumpla una condición específica
elemento = wait.until(EC.presence_of_element_located((By.ID, "mi-elemento")))


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Esperar hasta que se cumpla una condición específica
elemento = wait.until(EC.presence_of_element_located((By.ID, "mi-elemento")))
