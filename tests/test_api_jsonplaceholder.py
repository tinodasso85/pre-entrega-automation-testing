import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    json_data = response.json()

    # Validaciones de contenido
    assert "userId" in json_data
    assert "id" in json_data
    assert json_data["id"] == 1


def test_create_post():
    payload = {
        "title": "Tincho Test",
        "body": "Probando creación de post",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

    json_data = response.json()

    # JSONPlaceholder simula creación y devuelve ID siempre
    assert "id" in json_data
    assert json_data["title"] == payload["title"]


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    # JSONPlaceholder simula un borrado exitoso retornando 200 o 204
    assert response.status_code in [200, 204]
