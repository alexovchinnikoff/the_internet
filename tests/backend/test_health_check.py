# test_health_check.py
from services import get_health_check

def test_health_check():
    response = get_health_check()

    assert response.status_code == 200, f"Ожидался 200, но получен {response.status_code}"
    data = response.json()
    assert data["success"] is True
    assert data["status"] == 200
    # assert data["message"] == "Successful Request"
    assert str(response.url).endswith("/health-check"), f"Неверный URL: {response.url}"
    print("✅ Тест health-check пройден успешно!")