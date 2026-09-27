# test_health_check_err500.py
from unittest.mock import Mock
from services import get_health_check
import services

def test_health_check_err500():
    fake_response = Mock()
    fake_response.status_code = 500
    fake_response.url = "https://practice.expandtesting.com/notes/api/health-check"
    fake_response.json.return_value = {
        "success": False,
        "status": 500,
        "message": "Simulated Internal Error"
    }

    original_func = services.get_health_check
    try:
        services.get_health_check = lambda: fake_response
        response = services.get_health_check()

        assert response.status_code == 500, f"Ожидался 500, но получен {response.status_code}"
        data = response.json()
        assert data["success"] is False
        assert data["status"] == 500
        print("✅ Тест на симуляцию ошибки 500 пройден!")

    finally:
        services.get_health_check = original_func

def test_health_check():
    response = get_health_check()
    assert response.status_code == 200
    print("✅ Тест на реальный успех (200) пройден!")