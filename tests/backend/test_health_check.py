# test_health_check.py
import requests
from api.services import get_health_check

def test_health_check():
    session = requests.Session()
    health_resp = get_health_check(session)
    assert health_resp.status_code == 200, f"Ожидался 200, но получен {health_resp.status_code}"

    data = health_resp.json()
    assert data["success"] is True, f"Ожидался success: True, но получено: {data['success']}"
    assert data["status"] == 200, f"Ожидался статус 200 в JSON, но получено: {data['status']}"
    assert data["message"] == "Successful Request" or data["message"] == "Notes API is Running"
    assert str(health_resp.url).endswith("/health-check"), f"Неверный URL: {health_resp.url}"
    print("✅ Тест 'Проверка сервера' пройден успешно!")