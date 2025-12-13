import pytest
from pages.login_page import LoginPage

def test_login_invalido(driver):
    login = LoginPage(driver)
    login.abrir()

    login.ingresar_usuario("usuario_falso")
    login.ingresar_password("clave_incorrecta")
    login.click_login()

    mensaje = login.obtener_mensaje_error()

    assert "Epic sadface" in mensaje, "❌ No apareció mensaje de error en login inválido"

    print("✅ Login negativo validado correctamente")
