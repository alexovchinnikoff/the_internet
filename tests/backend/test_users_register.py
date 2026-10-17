# tests/backend/test_users_register.py
import requests
import allure
from api.services import post_users_register
from api.helpers import get_userdata

@allure.feature("Регистрация пользователя")
@allure.story("Успешная регистрация нового аккаунта")
@allure.title("Тест: Регистрация пользователя")
@allure.description("Проверяет успешную регистрацию нового пользователя, валидацию статуса 201, структуры JSON и совпадение данных пользователя.")
@allure.severity(allure.severity_level.CRITICAL)

def test_users_register():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Отправка запроса на регистрацию"):
        register_resp = post_users_register(session, user_data)
        assert register_resp.status_code == 201, \
            f"Ожидался статус 201 (Created), но получен {register_resp.status_code}. Ответ сервера: {register_resp.text}"

    with allure.step("2. Проверка структуры ответа и флага success"):
        data = register_resp.json()
        assert "success" in data, "В ответе отсутствует обязательный ключ 'success'"
        assert data.get("success") is True, f"Ожидался success: True, но получено: {data.get('success')}"

        assert "status" in data, "В ответе отсутствует обязательный ключ 'status'"
        assert data.get("status") == 201, \
            f"Ожидался статус 201 в JSON, но получен {data.get('status')}"
        assert "message" in data, "В ответе отсутствует сообщение"
        assert "created successfully" in data.get("message", ""), \
            f"Некорректное сообщение: {data.get('message')}"

    with allure.step("3. Валидация данных пользователя в ответе сервера"):
        assert "data" in data, "В ответе отсутствует блок 'data' с данными пользователя"

        data_server = data["data"]
        assert "email" in data_server, "В блоке 'data' отсутствует ключ 'email'"
        assert data_server["email"] == user_data["email"], \
            f"Email не совпадает! Ожидался: {user_data['email']}, получен: {data_server['email']}"

        assert "name" in data_server, "В блоке 'data' отсутствует ключ 'name'"
        assert data_server["name"] == user_data["name"], \
            f"Name не совпадает! Ожидался: {user_data['name']}, получен: {data_server['name']}"

        assert "id" in data_server, "В блоке 'data' отсутствует ключ 'id'"
        assert data_server["id"] is not None, "В ответе сервера отсутствует ID пользователя"