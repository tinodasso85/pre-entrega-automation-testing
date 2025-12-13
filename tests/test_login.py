import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(driver):
    login = LoginPage(driver)
    inventario = InventoryPage(driver)

    # Abrir página
    login.abrir()

    # Completar login
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()

    # Validar
    assert "inventory" in driver.current_url, "❌ El login no redirigió al inventario"
    assert inventario.titulo() == "Products", "❌ No se cargó la página de productos"

    print("✅ Login exitoso usando POM")

