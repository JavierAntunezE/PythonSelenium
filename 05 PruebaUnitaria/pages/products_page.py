from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_item = (By.CLASS_NAME, "shopping_cart_container")
        self.product_cards = (By.CLASS_NAME, "inventory_item")
        self.add_button_by_name = lambda name: (
            By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']"
        )

    def wait_until_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.product_cards)
        )

    def add_product_by_name(self, product_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button_by_name(product_name))
        ).click()
        print(f"Se agrega el producto {product_name}")

    def add_multiple_products(self, product_names):
        for name in product_names:
            self.add_product_by_name(name)

    def get_cart_count(self):
        try:
            badge = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.cart_badge)
            )
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.cart_item).click()



mi_lista = [18, -3, 5, 0, -1, 12]
lista_nueva = list(filter(lambda x: x > 0, mi_lista))
print(lista_nueva) # [18, 5, 12]