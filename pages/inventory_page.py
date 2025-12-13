from selenium.webdriver.common.by import By
from conftest import logger

class InventoryPage:

    add_buttons = (By.CLASS_NAME, "btn_inventory")
    carrito_icon = (By.CLASS_NAME, "shopping_cart_link")
    title_page = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def agregar_primer_producto(self):
        logger.info("Agregando primer producto al carrito")
        self.driver.find_element(*self.add_buttons).click()

    def ir_al_carrito(self):
        logger.info("Yendo al carrito")
        self.driver.find_element(*self.carrito_icon).click()

    def titulo(self):
        logger.info("Obteniendo título de la página de inventario")
        return self.driver.find_element(*self.title_page).text


