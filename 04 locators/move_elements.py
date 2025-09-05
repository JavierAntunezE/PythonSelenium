from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/sortable")

# Esperar a que la lista esté visible
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "demo-tabpane-list"))
)

# Localizar los elementos de la lista
items = driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")

# Inicializar ActionChains
actions = ActionChains(driver) #ejecutar una secuencia de acciones con el mouse o teclado

# Mover el primer elemento al final
source = items[0] #Selecciona el primer elemento de la lista como origen
target = items[-1] #Selecciona el último elemento de la lista como destino

#simulando una acción de drag-and-drop
actions.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(1)

# Mover el primer elemento al final
source = items[0] #Selecciona el primer elemento de la lista como origen
target = items[-1] #Selecciona el último elemento de la lista como destino

#simulando una acción de drag-and-drop
actions.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(2)

print(f"Se movió '{source.text}' al final de la lista.")

driver.quit()
