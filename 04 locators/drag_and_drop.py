from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/droppable")

# Esperar a que cargue la pestaña "Prevent Propogation" y hacer clic
prevent_tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "droppableExample-tab-preventPropogation"))
)
prevent_tab.click()

# Esperar a que aparezca el draggable
draggable = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dragBox"))
)

# Localizar el contenedor interno
inner_drop = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "notGreedyInnerDropBox"))
)

# Simular drag-and-drop
actions = ActionChains(driver)
#Arrastrar el elemento draggable y lo suelta sobre el elemento inner_drop.
actions.drag_and_drop(draggable, inner_drop).perform()

time.sleep(2)

# Texto del contenedor interno
resultado = inner_drop.text
print("Texto del contenedor interno:", resultado)

driver.quit()
