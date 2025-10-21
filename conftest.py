# conftest.py
import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Inicializa el navegador Chrome para los tests."""
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()  # ChromeDriver debe estar en el PATH
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook de Pytest para generar capturas automáticas al fallar un test."""
    outcome = yield
    report = outcome.get_result()
    driver = item.funcargs.get("driver", None)

    if report.when == "call" and report.failed and driver:
        # Crear carpeta de capturas dentro de /reports/screenshots/
        screenshots_dir = os.path.join("reports", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # Nombre del archivo con timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(screenshots_dir, f"{item.name}_{timestamp}.png")

        # Guardar captura
        driver.save_screenshot(filename)
        print(f"\n📸 Captura guardada en: {filename}")

