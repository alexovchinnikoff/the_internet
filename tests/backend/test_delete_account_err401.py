# tests/backend/test_delete_account_err401.py
import requests
import allure
from api.services import post_users_register, post_users_login, delete_users_account
from api.helpers import get_userdata

@allure.feature("Управление аккаунтом")
@allure.story("Обработка ошибок авторизации")
@allure.title("Тест: Удаление аккаунта без токена (ошибка 401)")
@allure.description("Проверяет, что попытка удаления аккаунта без токена авторизации возвращает ошибку 401 Unauthorized и корректное сообщение об ошибке.")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_account_without_token():
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

    with allure.step("3. Попытка удаления аккаунта БЕЗ токена (проверка ошибки 401)"):
        # Передаем token=None, чтобы явно показать, что мы намеренно не передаем токен
        delete_resp = delete_users_account(session, token=None)
        assert delete_resp.status_code == 401, \
            f"Ожидался статус 401 (Unauthorized), но получен {delete_resp.status_code}. Ответ: {delete_resp.text}"

    with allure.step("4. Валидация ответа сервера об ошибке"):
        data = delete_resp.json()
        assert "success" in data, "В ответе отсутствует обязательный ключ 'success'"
        assert data.get("success") is False, \
            f"Ожидался success: False, но получено: {data.get('success')}"

        assert "status" in data, "В ответе отсутствует обязательный ключ 'status'"
        assert data.get("status") == 401, \
            f"Ожидался статус 401 в JSON, но получен {data.get('status')}"

        assert "message" in data, "В ответе отсутствует сообщение"
        message = data.get("message", "")

        # Используем проверку подстроки, так как текст сообщения может немного отличаться в разных версиях API
        assert "No authentication token" in message or "Unauthorized" in message, \
            f"Некорректное сообщение об ошибке: {message}"