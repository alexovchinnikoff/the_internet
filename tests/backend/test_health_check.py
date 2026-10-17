# tests/backend/test_health_check.py
import requests
import allure
from api.services import get_health_check

@allure.feature("API Health Check")
@allure.story("Проверка доступности сервиса")
@allure.title("Тест: Проверка здоровья сервера (Health Check)")
@allure.description("Проверяет, что эндпоинт /health-check доступен, возвращает статус 200 и корректные данные.")
@allure.severity(allure.severity_level.BLOCKER)  # Критически важный тест

def test_health_check():
    session = requests.Session()

    with allure.step("1. Отправляем запрос на проверку здоровья сервера"):
        health_resp = get_health_check(session)
        assert health_resp.status_code == 200, f"Ожидался 200, но получен {health_resp.status_code}"

    with allure.step("2. Проверяем структуру ответа JSON"):
        data = health_resp.json()
        assert data.get("success") is True, f"Ожидался success: True, но получено: {data.get('success')}"
        assert data.get("status") == 200, f"Ожидался статус 200 в JSON, но получено: {data.get('status')}"

        message = data.get("message", "")
        assert "Successful" in message or "Running" in message, f"Некорректное сообщение: {message}"

    with allure.step("3. Проверяем URL запроса"):
        url = str(health_resp.url)
        assert url.endswith("/health-check"), f"Неверный URL: {url}"