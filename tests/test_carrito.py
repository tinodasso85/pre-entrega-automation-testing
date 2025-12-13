import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_agregar_producto_carrito(driver):
    login = LoginPage(driver)
    inventario = InventoryPage(driver)
    carrito = CartPage(driver)

    login.abrir()
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()

    inventario.agregar_primer_producto()
    inventario.ir_al_carrito()

    items = carrito.obtener_items()
    assert len(items) > 0, "❌ No se pudo agregar el producto al carrito"

    print("✅ Producto agregado correctamente al carrito")

