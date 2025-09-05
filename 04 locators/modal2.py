from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/modal-dialogs")

# Esperar a que el botón del modal grande esté disponible
boton_grande = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "showLargeModal"))
)
boton_grande.click()

# Esperar a que el modal sea visible
modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
)

# Obtener el título del modal
titulo = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
print("Título del modal:", titulo)

# Validar que el modal contiene texto
contenido = driver.find_element(By.CLASS_NAME, "modal-body").text
print("Contenido del modal:", contenido[:100], "...")  # Mostrar primeros 100 caracteres

# Cerrar el modal
cerrar_btn = driver.find_element(By.ID, "closeLargeModal")
cerrar_btn.click()

# Validar que el modal ya no está visible
WebDriverWait(driver, 5).until(
    EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content"))
)
print("Modal cerrado correctamente")

driver.quit()
