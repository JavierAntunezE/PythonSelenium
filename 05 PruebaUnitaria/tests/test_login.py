# archivo: test_login.py
import time
import unittest
from selenium import webdriver

from db.sql_connector import SqlConnector
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

        #bd
        db = SqlConnector(server="localhost", database="TestLoginDB", user="userPythonDB", password="Abc.123")
        conn = db.connect()

        query = "SELECT Username, Password FROM Users WHERE Username = 'user1'"
        usuario_result = db.execute_query(query)
        if usuario_result:
            usuario = usuario_result[0]
        else:
            raise ValueError("No se encontró ningún usuario activo.")

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    # Test de login exitoso
    def test_login_valido(self):
        self.login_page.enter_username(self.usuario.Username)#"standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login()

        # Espera explícita a que cargue la página de inventario
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("inventory.html")
        )
        self.assertIn("inventory.html", self.driver.current_url)

    # Test de login inválido
    def test_login_invalido(self):
        self.login_page.enter_username("usuario_invalido")
        self.login_page.enter_password("1234")
        self.login_page.click_login()

        # Validar mensaje de error
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )
        error = self.login_page.get_error_message()
        self.assertIn("Epic sadface", error)

if __name__ == "__main__":
    unittest.main()
