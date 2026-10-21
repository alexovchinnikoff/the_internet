# tests/backend/test_users_profile_get.py
import requests
import allure
from api.services import get_users_profile, post_users_register, post_users_login
from api.helpers import get_userdata

@allure.feature("Returns the profile information for the logged-in current user")
@allure.story("Получить информацию из профиля пользователя")
@allure.title("Тест: Успешное получение информации из профиля пользователя")
@allure.description("Проверяет, что эндпоинт /users/profile доступен, возвращает статус 200 и корректные данные.")
@allure.severity(allure.severity_level.BLOCKER)  # Критически важный тест

def test_users_profile():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация нового пользователя"):
        reg_resp = post_users_register(session, user_data)
        assert reg_resp.status_code == 201, \
            f"Ожидался статус 201 (Created), но получен {reg_resp.status_code}. Ответ: {reg_resp.text}"

        data_reg = reg_resp.json()
        assert data_reg.get("success") is True, \
            f"Ожидался success: True, но получено: {data_reg.get('success')}"

    with allure.step("2. Логин пользователя и получение токена"):
        login_payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }

        login_resp, token = post_users_login(session, login_payload)
        assert login_resp.status_code == 200, \
            f"Ожидался статус 200 (OK), но получен {login_resp.status_code}. Ответ: {login_resp.text}"
        assert token is not None, "Критическая ошибка: Не удалось извлечь токен из ответа сервера!"

    with allure.step("Шаг 3: Запрос профиля пользователя с токеном"):
        profile_resp = get_users_profile(session, token=token)
        assert profile_resp.status_code == 200, f"Ожидался 200, но получен {profile_resp.status_code}"

    with allure.step("4. Проверяем структуру ответа JSON"):
        data_profile = profile_resp.json()
        assert data_profile.get("success") is True, f"Ожидался success: True, но получено: {data_profile.get('success')}"
        assert data_profile.get("status") == 200, f"Ожидался статус 200 в JSON, но получено: {data_profile.get('status')}"

        message = data_profile.get("message", "")
        assert "successful" in message or "Successful" in message, f"Некорректное сообщение: {message}"

    with allure.step("5. Валидация данных пользователя в ответе сервера"):
        data_server = data_profile.get("data")
        assert data_server is not None, "В ответе сервера отсутствует блок 'data' с данными пользователя"

        assert "email" in data_server, "В блоке 'data' отсутствует ключ 'email'"
        assert data_server["email"] == user_data["email"], \
            f"Email не совпадает! Ожидался: {user_data['email']}, получен: {data_server['email']}"

        assert "name" in data_server, "В блоке 'data' отсутствует ключ 'name'"
        assert data_server["name"] == user_data["name"], \
            f"Name не совпадает! Ожидался: {user_data['name']}, получен: {data_server['name']}"

        assert "id" in data_server, "В блоке 'data' отсутствует ключ 'id'"
        assert data_server["id"] is not None, "В ответе сервера отсутствует ID пользователя"

        if "phone" in data_server:
            assert data_server["phone"] is not None, "Поле phone не должно быть пустым"

        if "company" in data_server:
            assert data_server["company"] is not None, "Поле company не должно быть пустым"

    with allure.step("5. Проверяем URL запроса"):
        url = str(profile_resp.url)
        assert url.endswith("/users/profile"), f"Неверный URL: {url}"