import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_completo(driver):
    login = LoginPage(driver)
    inventario = InventoryPage(driver)
    carrito = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    login.abrir()
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()

    # Agregar producto
    inventario.agregar_primer_producto()
    inventario.ir_al_carrito()

    carrito.click_checkout()

    # Completar datos
    checkout.completar_info("Martin", "Dasso", "1234")
    checkout.continuar()

    # ⭐ ESPERA IMPORTANTE: esperar que aparezca el botón Finish
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    checkout.finalizar()

    # Espera del mensaje final
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    mensaje = checkout.obtener_mensaje_final()

    assert mensaje == "Thank you for your order!", "❌ No se completó el checkout"

    print("✅ Checkout finalizado exitosamente")

