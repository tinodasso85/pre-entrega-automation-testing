Pre-Entrega: Automation Testing - Martín Dasso

Proyecto de automatización web utilizando **Python + Selenium + Pytest**, sobre el sitio [saucedemo.com](https://www.saucedemo.com).

---

Objetivo
Automatizar flujos básicos de prueba sobre la aplicación *Swag Labs*:
1. Login exitoso.
2. (Próximos pasos: agregar producto al carrito, logout, validación de error de login, etc.)
3. Interacción con productos y carrito de compras.
4. Validaciones adicionales (logout, manejo de errores, etc.).


Dependencias necesarias
Ejecutar todos los tests y generar un reporte unificado:
Ejecutar un test específico:

pip install -r requirements.txt

Ejecutar un test específico:
python -m pytest -v --html=reports/reporte_login.html
---

Tecnologías utilizadas
- Python 3.11
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Webdriver-Manager

---
##  Estructura del proyecto
pre-entrega-automation-testing-martin_dasso/

│
├── tests/                      # Tests automatizados
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
│
├── utils/                      # Funciones auxiliares y setup de driver
│   └── driver_setup.py
│
├── reports/                    # Reportes HTML y capturas de fallos
│   └── screenshots/
│
├── datos/                      # Archivos de datos (CSV/JSON) si aplica
│
├── conftest.py                 # Hooks de Pytest y fixture driver
├── requirements.txt            # Dependencias del proyecto
└── README.md
