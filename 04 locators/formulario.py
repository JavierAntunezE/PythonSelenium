from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

time.sleep(3)  # pequeña espera para que cargue

# 1. Localizador por ID
driver.find_element(By.ID, "firstName").send_keys("Javier")
driver.find_element(By.ID, "lastName").send_keys("Antúnez")
time.sleep(1)

# 2. Localizador por NAME
driver.find_element(By.ID, "userEmail").send_keys("javier@example.com")
time.sleep(1)

# 3. Localizador por CSS_SELECTOR (radio button "Male")
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()

# 4. Localizador por XPATH (campo de teléfono)
driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("5512345678")
time.sleep(1)

# 5. Localizador por CSS_SELECTOR (date picker)
date = driver.find_element(By.ID, "dateOfBirthInput")
date.send_keys("01 oct 2000")
date.send_keys(Keys.ENTER)
time.sleep(1)

# 6. Localizador por XPATH (subjects input)
subjects = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)
time.sleep(1)

# 7. Localizador por CSS_SELECTOR (checkbox 'Sports')
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()
time.sleep(1)

# 8. Localizador por ID (upload de archivo)
(driver.find_element(By.ID, "uploadPicture")
.send_keys(r"C:\Users\javie\Downloads\a0a4211edd394c0cba899911d725c0d4.jpg"))
time.sleep(1)

# 9. Localizador por CSS_SELECTOR (dirección)
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("CDMX, México")
time.sleep(1)

# 10. Localizador por XPATH (botón Submit)
submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
time.sleep(2)
submit_btn.click()

time.sleep(5)  # esperar para ver resultado

# Localizamos el modal
try:
    modal = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    assert modal.is_displayed()
    print("Formulario llenado correctamente")
except NoSuchElementException:
    print("El modal no se abrió. Probablemente los datos no fueron correctos")

driver.quit()
