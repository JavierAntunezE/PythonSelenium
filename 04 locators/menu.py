from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/menu")

# Inicializar ActionChains
actions = ActionChains(driver)

# Esperar y ubicar el primer nivel del menú
menu_item_2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='Main Item 2']"))
)
actions.move_to_element(menu_item_2).perform() #Simulación de hover

# Esperar y ubicar el submenú
sub_sub_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']"))
)
actions.move_to_element(sub_sub_list).perform()

# Esperar y hacer clic en “Sub Sub Item 2”
sub_sub_item_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Sub Sub Item 2']"))
)
sub_sub_item_2.click()

print("Se hizo clic en 'Sub Sub Item 2' correctamente.")

driver.quit()
