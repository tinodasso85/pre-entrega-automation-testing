from selenium.webdriver.common.by import By
from conftest import logger

class CartPage:

    checkout_button = (By.ID, "checkout")
    items_carrito = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        logger.info("Click en Checkout")
        self.driver.find_element(*self.checkout_button).click()

    def obtener_items(self):
        logger.info("Obteniendo items del carrito")
        return self.driver.find_elements(*self.items_carrito)


