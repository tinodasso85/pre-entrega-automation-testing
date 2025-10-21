# tests/test_carrito.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_producto_carrito(driver):
    """Valida la funcionalidad de agregar un producto al carrito en saucedemo.com"""

    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # --- LOGIN ---
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # --- ESPERA A INVENTARIO ---
    wait.until(EC.url_contains("/inventory.html"))

    # --- AGREGAR EL PRIMER PRODUCTO ---
    primer_boton_add = driver.find_element(By.CLASS_NAME, "btn_inventory")
    primer_boton_add.click()

    # --- VERIFICAR CONTADOR DEL CARRITO ---
    contador_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert contador_carrito.text == "1", "❌ El contador del carrito no se incrementó correctamente"

    # --- NAVEGAR AL CARRITO ---
    driver.find_element(By.ID, "shopping_cart_container").click()
    wait.until(EC.url_contains("/cart.html"))

    # --- VERIFICAR PRODUCTO EN EL CARRITO ---
    producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    nombre_producto = producto_carrito.text
    assert nombre_producto != "", "❌ No se detectó producto en el carrito"

    print(f"✅ Producto '{nombre_producto}' agregado correctamente al carrito.")
