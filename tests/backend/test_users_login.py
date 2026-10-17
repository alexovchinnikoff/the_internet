# tests/backend/test_users_login.py
import requests
import allure
from api.services import post_users_register, post_users_login
from api.helpers import get_userdata

@allure.feature("Авторизация пользователя")
@allure.story("Успешный вход в систему")
@allure.title("Тест: Успешный логин пользователя")
@allure.description("Проверяет регистрацию нового пользователя, успешный логин, получение токена и валидацию данных в ответе сервера.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_user():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация нового пользователя"):
        reg_resp = post_users_register(session, user_data)
        data_reg = reg_resp.json()
        assert "success" in data_reg, f"Ответ не содержит ключа 'success': {reg_resp.text}"
        assert reg_resp.status_code == 201, f"Ожидался статус 201 (Created), но получен {reg_resp.status_code}"
        assert data_reg.get("success") is True, f"Ожидался success: True, но получено: {data_reg.get('success')}"

    with allure.step("2. Отправка запроса на логин"):
        login_payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        login_resp, token = post_users_login(session, login_payload)
        assert login_resp.status_code == 200, f"Ожидался статус 200 (OK), но получен {login_resp.status_code}. Ответ: {login_resp.text}"

    with allure.step("3. Проверка структуры ответа логина и токена"):
        data_login = login_resp.json()
        assert "success" in data_login, "В ответе отсутствует обязательный ключ 'success'"
        assert data_login.get("success") is True, f"Ожидался success: True, но получено: {data_login.get('success')}"

        assert "status" in data_login, "В ответе отсутствует обязательный ключ 'status'"
        assert data_login.get("status") == 200, f"Ожидался статус 200, но получено: {data_login.get('status')}"

        assert "message" in data_login, "В ответе отсутствует сообщение"
        assert "Login successful" in data_login.get("message",
                                                    ""), f"Некорректное сообщение: {data_login.get('message')}"

        assert token is not None, "Критическая ошибка: Не удалось извлечь токен из ответа сервера!"
        assert data_login.get("data", {}).get(
            "token") == token, "Токен в JSON-ответе не совпадает с возвращенным токеном"

    with allure.step("4. Валидация данных пользователя в ответе сервера"):
        data_server = data_login.get("data")
        assert data_server is not None, "В ответе сервера отсутствует блок 'data' с данными пользователя"

        assert "email" in data_server, "В блоке 'data' отсутствует ключ 'email'"
        assert data_server["email"] == user_data["email"], \
            f"Email не совпадает! Ожидался: {user_data['email']}, получен: {data_server['email']}"

        assert "name" in data_server, "В блоке 'data' отсутствует ключ 'name'"
        assert data_server["name"] == user_data["name"], \
            f"Name не совпадает! Ожидался: {user_data['name']}, получен: {data_server['name']}"

        assert "id" in data_server, "В блоке 'data' отсутствует ключ 'id'"
        assert data_server["id"] is not None, "В ответе сервера отсутствует ID пользователя"