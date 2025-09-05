from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/webtables")

# Esperar a que la tabla esté visible
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "rt-table"))
)

# Bucle para eliminar todas las filas visibles
while True:
    # Buscar todos los botones de eliminar
    botones_eliminar = driver.find_elements(By.CSS_SELECTOR, "span[title='Delete']")

    if not botones_eliminar:
        print("No quedan registros en la tabla.")
        break

    # Eliminar la primera fila
    botones_eliminar[0].click()
    time.sleep(0.5)  # Pequeña pausa para que se actualice el DOM

print("Todos los registros fueron eliminados correctamente.")
driver.quit()
