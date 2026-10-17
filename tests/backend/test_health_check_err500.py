# tests/backend/test_health_check_err500.py
import requests
import allure
from unittest.mock import Mock, patch
import api.services

def create_fake_response(status_code, data):
    fake_resp = Mock()
    fake_resp.status_code = status_code
    fake_resp.url = "https://practice.expandtesting.com/notes/api/health-check"
    fake_resp.json.return_value = data
    return fake_resp

@allure.feature("Мониторинг и обработка ошибок")
@allure.story("Проверка реакции на критические ошибки сервера")
@allure.title("Тест: Симуляция ошибки 500 (Internal Error)")
@allure.description("Проверяет, что тест корректно обрабатывает ситуацию, когда сервер возвращает ошибку 500. Использует мок-объект для эмуляции ответа сервера без реального запроса.")
@allure.severity(allure.severity_level.NORMAL)
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

    with allure.step("Вызов функции проверки здоровья с подмененным ответом (500)"):
        response = api.services.get_health_check(session)
        assert response.status_code == 500, f"Ожидался статус 500, но получен {response.status_code}"

    with allure.step("Валидация структуры JSON ответа об ошибке"):
        data = response.json()
        assert data.get("success") is False, f"Ожидался success: False, но получено: {data.get('success')}"
        assert data.get("status") == 500, f"Ожидался статус 500 в JSON, но получен: {data.get('status')}"
        assert data.get(
            "message") == "Simulated Internal Error", f"Некорректное сообщение об ошибке: {data.get('message')}"

@allure.feature("Мониторинг и обработка ошибок")
@allure.story("Проверка реакции на критические ошибки сервера")
@allure.title("Тест: Реальная проверка здоровья сервера (200 OK)")
@allure.description("Проверяет реальное состояние сервера. Ожидается успешный ответ 200.")
@allure.severity(allure.severity_level.CRITICAL)

def test_health_check_real():
    session = requests.Session()

    with allure.step("Отправка реального запроса на проверку здоровья"):
        response = api.services.get_health_check(session)
        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}. Ответ: {response.text}"

    with allure.step("Валидация успешного ответа"):
        data = response.json()
        assert data.get("success") is True, f"Ожидался success: True, но получено: {data.get('success')}"
        assert data.get("status") == 200, f"Ожидался статус 200 в JSON, но получен: {data.get('status')}"