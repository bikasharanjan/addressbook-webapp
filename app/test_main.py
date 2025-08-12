from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_read_delete():
    # Create
    response = client.post("/addresses/", json={"name": "Home", "latitude": 12.97, "longitude": 77.59})
    assert response.status_code == 200
    data = response.json()
    address_id = data["id"]

    # Read
    res_get = client.get("/addresses/")
    assert res_get.status_code == 200
    assert any(addr["id"] == address_id for addr in res_get.json())

    # Delete
    res_del = client.delete(f"/addresses/{address_id}")
    assert res_del.status_code == 200
