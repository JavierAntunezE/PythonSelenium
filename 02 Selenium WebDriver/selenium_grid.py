from selenium import webdriver
from selenium.webdriver.common.by import By

# Dirección del hub de Selenium Grid
GRID_URL = "http://localhost:4444/wd/hub"

# Configuración de las capacidades (ejemplo con Chrome)
capabilities = {
    "browserName": "chrome",
    "browserVersion": "latest",
    "platformName": "ANY",
}

# Inicializa el Remote WebDriver apuntando al Grid
driver = webdriver.Remote(
    command_executor=GRID_URL,
    desired_capabilities=capabilities
)

try:
    # Navegar a una página de prueba
    driver.get("https://www.saucedemo.com/")

    # Interactuar con la página
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verificar que se haya hecho login
    assert "inventory" in driver.current_url
    print("✅ Prueba ejecutada correctamente en Selenium Grid")

finally:
    driver.quit()
