from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Selenium Manager se encarga de conseguir el driver
driver = webdriver.Chrome() # Firefox(), Edge()

try:
    driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")
    driver.maximize_window()

    #Ingresa username
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")

    #Ingresa password
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    #Presiona la tecla ENTER
    password.send_keys(Keys.RETURN)

    #Espera 3 segundos
    time.sleep(3)

    #Obtiene el elemento h2
    result = driver.find_element(By.CSS_SELECTOR, "h2")

    #Valida que tenga el texto 'Secure Area'
    found = result.text == "Secure Area"
    #any("Secure Area" in r.text for r in results)

    #Despliega mensaje correspondiente
    print("Test PASSED") if found else print("Test FAILED")

finally:
    driver.quit()
