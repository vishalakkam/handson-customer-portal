import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app.app import app, customers

import pytest
from app.app import app, customers


@pytest.fixture
def client():
    app.config["TESTING"] = True
    customers.clear()
    return app.test_client()


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "UP"


def test_register_customer(client):
    response = client.post(
        "/register",
        json={
            "name": "Rahul",
            "email": "rahul@example.com"
        }
    )

    assert response.status_code == 201
    assert response.json["name"] == "Rahul"
    assert response.json["email"] == "rahul@example.com"

def test_get_customer(client):
    client.post(
        "/register",
        json={
            "name": "Vishal",
            "email": "vishal@example.com"
        }
    )

    response = client.get("/customers/1")

    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["name"] == "Vishal"