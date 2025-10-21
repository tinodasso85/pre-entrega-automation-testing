# tests/test_catalogo.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navegacion_catalogo(driver):
    """Valida el catálogo de productos en saucedemo.com"""

    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # --- LOGIN ---
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # --- VALIDACIÓN DE PÁGINA ---
    wait.until(EC.url_contains("/inventory.html"))
    titulo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert titulo.text == "Products", "❌ El título de la página no es 'Products'"

    # --- VALIDAR PRESENCIA DE PRODUCTOS ---
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "❌ No se encontraron productos visibles"

    # --- VALIDAR ELEMENTOS IMPORTANTES ---
    menu_boton = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_boton.is_displayed(), "❌ El menú lateral no está visible"

    filtro_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro_dropdown.is_displayed(), "❌ El filtro de productos no está presente"

    # --- LISTAR NOMBRE Y PRECIO DEL PRIMER PRODUCTO ---
    primer_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"✅ Primer producto: {primer_nombre} - Precio: {primer_precio}")

    # Validación final
    assert primer_nombre != "" and primer_precio != "", "❌ No se pudo obtener nombre o precio del producto"
    print("✅ Catálogo validado correctamente.")
