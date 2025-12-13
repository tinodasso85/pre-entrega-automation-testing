# tests/test_login_parametrizado.py
import csv
import os
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Lee el CSV desde la carpeta data (ruta relativa a la raíz del proyecto)
def leer_datos():
    ruta = os.path.join(os.path.dirname(__file__), "..", "data", "users.csv")
    ruta = os.path.abspath(ruta)
    with open(ruta, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

@pytest.mark.parametrize("info", leer_datos())
def test_login_parametrizado(driver, info):
    login = LoginPage(driver)
    inventario = InventoryPage(driver)

    login.abrir()
    login.ingresar_usuario(info["username"])
    login.ingresar_password(info["password"])
    login.click_login()

    # Espera explícita: hasta que aparezca el título o el mensaje de error
    wait = WebDriverWait(driver, 8)
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        # Si llegamos acá, estamos en inventario
        assert inventario.titulo() == "Products"
    except Exception:
        # Si no aparece el título, revisamos si apareció mensaje de error (login fallido)
        # Intentamos leer el mensaje de error (si existe) para la comprobación
        try:
            error_el = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            error_msg = error_el.text
        except Exception:
            error_msg = ""
        # Si el CSV tiene usuarios que deberían fallar, podrías validar aquí. 
        # Para este test simple asumimos que si no está "Products" falló el login:
        pytest.fail(f"Login con {info['username']} falló. Mensaje de error: {error_msg}")
