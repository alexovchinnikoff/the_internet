# test_health_check_err500.py
import requests
from unittest.mock import Mock, patch
import api.services

def create_fake_response(status_code, data):
    fake_resp = Mock()
    fake_resp.status_code = status_code
    fake_resp.url = "https://practice.expandtesting.com/notes/api/health-check"
    fake_resp.json.return_value = data
    return fake_resp

@patch('api.services.get_health_check')
def test_health_check_err500(mock_get_health_check):
    fake_data = {
        "success": False,
        "status": 500,
        "message": "Simulated Internal Error"
    }
    fake_response = create_fake_response(500, fake_data)
    mock_get_health_check.return_value = fake_response

    session = requests.Session()

    response = api.services.get_health_check(session)
    assert response.status_code == 500

    data = response.json()
    assert data["success"] is False
    assert data["status"] == 500
    print("✅ Тест на симуляцию ошибки 500 пройден!")