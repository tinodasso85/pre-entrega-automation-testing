from selenium.webdriver.common.by import By
from conftest import logger

class LoginPage:

    url = "https://www.saucedemo.com/"

    user_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        logger.info("Abriendo página de login")
        self.driver.get(self.url)

    def ingresar_usuario(self, usuario):
        logger.info(f"Ingresando usuario: {usuario}")
        self.driver.find_element(*self.user_input).clear()
        self.driver.find_element(*self.user_input).send_keys(usuario)

    def ingresar_password(self, password):
        logger.info("Ingresando password")
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        logger.info("Haciendo click en Login")
        self.driver.find_element(*self.login_button).click()

    def obtener_mensaje_error(self):
        logger.info("Buscando mensaje de error en el login")
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return ""



