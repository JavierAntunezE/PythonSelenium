import time
import unittest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.login_page import LoginPage

from pages.products_page import ProductsPage


class TestAddProduct(unittest.TestCase):

    def setUp(self): #Se ejecuta antes de cada función
        self.config_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def config_options(self):
        self.options = webdriver.ChromeOptions()
        prefs = {
             "profile.password_manager_leak_detection": False
        }
        self.options.add_experimental_option("prefs", prefs)

    def tearDown(self): #Se ejecuta después de cada función
        time.sleep(0.5)
        self.driver.quit()

    def test_buy_products(self):
        self.login()

        self.add_products(products_names=[
                "Sauce Labs Backpack",
                "Sauce Labs Bike Light"])

        self.cart_page.wait_until_loaded()
        self.cart_page.get_cart_products()
        self.cart_page.click_checkout()
        print(f"Se continua con el checkout")

    def login(self):
        self.login_page.wait_until_loaded()
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login()

    def add_products(self, products_names):
        self.products_page.wait_until_loaded()
        # Agregar productos específicos
        self.products_page.add_multiple_products(
            products_names
        )
        # Validar que el carrito tiene 2 productos
        assert self.products_page.get_cart_count() == 2, "El carrito no tiene los productos esperados"
        print(f"El carrito tiene {self.products_page.get_cart_count()} productos")

        self.products_page.go_to_cart()


if __name__ == "__main__": #Solo se ejecuta si el archivo se corre directamente
    unittest.main() #Ejecuta automáticamente todas las funciones que comienzan con test_