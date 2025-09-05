from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")

# Espera explícita para el botón del prompt
prompt_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "promtButton"))
)
prompt_btn.click()
time.sleep(2)

# Espera a que aparezca el alert tipo prompt
WebDriverWait(driver, 5).until(EC.alert_is_present())
alerta = driver.switch_to.alert

# Leer el texto del prompt
print("Texto del prompt:", alerta.text)

# Enviar texto al prompt y aceptar
alerta.send_keys("Javier")
alerta.accept()
time.sleep(2)

# Validar que el texto se reflejó en la página
resultado = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "promptResult"))
)
assert "Javier" in resultado.text
print("Resultado en página:", resultado.text)

time.sleep(1)
driver.quit()
