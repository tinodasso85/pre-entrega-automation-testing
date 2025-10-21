import pytest
from utils.driver_setup import create_driver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def setup():
    driver = create_driver()
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Ingresar credenciales
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Validar login correcto
    assert "inventory" in driver.current_url, "❌ No se redirigió correctamente al inventario"
    assert "Swag Labs" in driver.title, "❌ El título no es el esperado"

    print("✅ Login exitoso")
