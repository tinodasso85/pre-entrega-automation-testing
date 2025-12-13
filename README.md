Entrega Final – Automation Testing
Autor: Martín Dasso

Proyecto de automatización de pruebas UI y API utilizando Python, Selenium y Pytest, aplicando Page Object Model, reportes HTML, capturas automáticas y logging.

Sitio automatizado (UI):
https://www.saucedemo.com

APIs públicas utilizadas:
JSONPlaceholder
---------------------------------------------------------------------------------------------------------------------------------
Objetivo del proyecto

Automatizar y validar:

Login exitoso y login inválido
Login parametrizado con datos externos
Visualización del inventario
Agregado de productos al carrito
Flujo de checkout
Pruebas de API (GET, POST, DELETE)
Generación de reportes y evidencias
---------------------------------------------------------------------------------------------------------------------------------
Tecnologías utilizadas

Python 3.11
Selenium WebDriver
Pytest
Pytest-HTML
Requests
WebDriver Manager
Logging
---------------------------------------------------------------------------------------------------------------------------------
Estructura del proyecto

pre-entrega-automation-testing-martin_dasso/

pages/
login_page.py
inventory_page.py
cart_page.py
checkout_page.py

tests/
test_login.py
test_login_negativo.py
test_login_parametrizado.py
test_inventario.py
test_carrito.py
test_checkout.py
test_api_jsonplaceholder.py

reports/
reporte_test.html

screenshots/

conftest.py
requirements.txt
README.md
---------------------------------------------------------------------------------------------------------------------------------
Instalación de dependencias

Ejecutar desde la raíz del proyecto:
python -m pip install -r requirements.txt
---------------------------------------------------------------------------------------------------------------------------------
Ejecución de pruebas

Ejecutar toda la suite y generar reporte HTML:
python -m pytest -v -s --html=reports/reporte_test.html --self-contained-html --capture=tee-sys
---------------------------------------------------------------------------------------------------------------------------------
Reportes y evidencias

El reporte HTML se genera en la carpeta reports
Las pruebas fallidas generan automáticamente capturas de pantalla
Las capturas incluyen nombre del test y fecha/hora
---------------------------------------------------------------------------------------------------------------------------------
Observaciones

El flujo de checkout puede fallar en algunos entornos locales por comportamiento del navegador.
El framework maneja correctamente el error, registra logs y genera evidencia visual.