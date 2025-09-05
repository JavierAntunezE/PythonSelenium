from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        self.page_title = (By.CLASS_NAME, "title")

    def wait_until_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.page_title)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.cart_items)
        )

    def get_cart_products(self):
        items = self.driver.find_elements(*self.cart_items)
        nombres = []
        for item in items:
            nombre = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            nombres.append(nombre)
        return nombres

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
