from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_listar_tarefas():
    response = client.get("/tarefas")

    assert response.status_code == 200
    assert isinstance(response.json(), list)