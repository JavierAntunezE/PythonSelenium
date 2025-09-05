from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()
driver.maximize_window()

# ----------------------------
# Espera implícita (aplica a todos los elementos)
driver.implicitly_wait(5)  # espera hasta 5 segundos para que los elementos estén presentes

driver.get("https://demoqa.com/automation-practice-form")

# ----------------------------
# 1. Localizador por ID
driver.find_element(By.ID, "firstName").send_keys("Javier")
driver.find_element(By.ID, "lastName").send_keys("Antúnez")

# 2. Localizador por NAME
driver.find_element(By.ID, "userEmail").send_keys("javier@example.com")

# 3. Localizador por CSS_SELECTOR (radio button "Male")
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()

# 4. Localizador por XPATH (campo de teléfono)
driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("5512345678")

# 5. Localizador por CSS_SELECTOR (date picker)
date = driver.find_element(By.ID, "dateOfBirthInput")
date.send_keys("01 Oct 2000")
date.send_keys(Keys.ENTER)

# 6. Localizador por XPATH (subjects input)
subjects = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)

# 7. Localizador por CSS_SELECTOR (checkbox 'Sports')
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()

# 8. Localizador por ID (upload de archivo)
driver.find_element(By.ID, "uploadPicture").send_keys(
    r"C:\Users\javie\Downloads\a0a4211edd394c0cba899911d725c0d4.jpg"
)

# 9. Localizador por CSS_SELECTOR (dirección)
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("CDMX, México")

# 10. Localizador por XPATH (botón Submit)
submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

# Espera explícita hasta que el botón sea clickable
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']")))
submit_btn.click()

# ----------------------------
# Validar que el modal aparece usando espera explícita
try:
    modal = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    assert modal.is_displayed()
    print("Formulario llenado correctamente")
except (NoSuchElementException, TimeoutException):
    print("El modal no se abrió. Probablemente los datos no fueron correctos")

driver.quit()
