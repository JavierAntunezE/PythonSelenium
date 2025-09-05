

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/auto-complete")

# Esperar a que el campo esté disponible
input_colores = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "autoCompleteMultipleInput"))
)

# Escribir "Red" y seleccionar con ENTER
input_colores.send_keys("Red")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'auto-complete__option')]"))
)
input_colores.send_keys(Keys.ENTER)

# Escribir "Green" y seleccionar con ENTER
input_colores.send_keys("Green")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'auto-complete__option')]"))
)
input_colores.send_keys(Keys.ENTER)

time.sleep(2)

# Validar que los colores fueron seleccionados
seleccionados = driver.find_elements(By.CSS_SELECTOR, ".auto-complete__multi-value__label")
for color in seleccionados:
    print("Color seleccionado:", color.text)

driver.quit()
