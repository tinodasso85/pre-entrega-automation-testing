import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
import logging

# ==========================
# CONFIGURACIÓN DEL LOGGING
# ==========================
LOG_DIR = "reports"
LOG_FILE_PATH = os.path.join(LOG_DIR, "execution.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger()


# ==========================
# FIXTURE DEL DRIVER
# ==========================
@pytest.fixture
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # si querés modo sin UI

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    logger.info("===== INICIO DE TEST =====")
    yield driver

    driver.quit()
    logger.info("===== FIN DEL TEST =====")


# ==========================
# SCREENSHOT AUTOMÁTICO AL FALLAR
# ==========================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "reports/screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            logger.error(f"❌ Test FALLÓ — Screenshot guardado: {file_path}")
            print(f"\n📸 Captura guardada en: {file_path}")


