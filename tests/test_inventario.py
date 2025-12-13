import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_catalogo_productos(driver):
    login = LoginPage(driver)
    inventario = InventoryPage(driver)

    login.abrir()
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()

    assert inventario.titulo() == "Products", "❌ No se cargó el catálogo"

    print("✅ Título del inventario validado correctamente")

