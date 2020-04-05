from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}


@pytest.mark.parametrize("name", ["Karina", "Partyk", "Asia", "Basia"])
def test_hello_name(name):
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}"}


@pytest.mark.parametrize("counter", [1,2,3,4,5])
def test_counter(counter):
    response = client.get("/counter")
    assert response.status_code == 200
    assert response.text == f'"{counter}"'


def test_receive_something():
    response = client.post("/dej/mi/coś", json={'first_key': 'some_value'})
    assert response.json() == {"received": {'first_key': 'some_value'},
                             "constant_data": "python jest super"}


def test_method():
    response = client.post("/method", json={})
    assert response.status_code == 200
    assert response.json() == {"method": "METHOD"}


def test_patient():
    response = client.post('/patient')