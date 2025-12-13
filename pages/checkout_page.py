from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import logger

class CheckoutPage:

    first_name = (By.ID, "first-name")
    last_name  = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    final_message = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def completar_info(self, nombre, apellido, codigo):
        logger.info(f"Completando formulario: {nombre} {apellido}, CP {codigo}")
        self.driver.find_element(*self.first_name).send_keys(nombre)
        self.driver.find_element(*self.last_name).send_keys(apellido)
        self.driver.find_element(*self.postal_code).send_keys(codigo)

    def continuar(self):
        logger.info("Click en Continue")
        self.driver.find_element(*self.continue_button).click()

    def finalizar(self):
        logger.info("Haciendo scroll hasta el botón Finish")
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*self.finish_button))

        logger.info("Click en Finalizar")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()

    def obtener_mensaje_final(self):
        logger.info("Obteniendo mensaje final del Checkout")
        return self.driver.find_element(*self.final_message).text


