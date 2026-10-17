# tests/backend/test_users_logout_err401.py
import requests
import allure
from api.services import post_users_register, delete_users_logout
from api.helpers import get_userdata

@allure.feature("Авторизация и сессия")
@allure.story("Обработка ошибок авторизации")
@allure.title("Тест: Логаут без токена (ошибка 401)")
@allure.description("Проверяет, что попытка выполнить логаут без передачи токена авторизации возвращает ошибку 401 Unauthorized.")
@allure.severity(allure.severity_level.NORMAL)
def test_logout_without_token():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация нового пользователя"):
        reg_resp = post_users_register(session, user_data)
        assert reg_resp.status_code == 201, \
            f"Ожидался статус 201 (Created), но получен {reg_resp.status_code}. Ответ: {reg_resp.text}"
        data_reg = reg_resp.json()
        assert data_reg.get("success") is True, \
            f"Ожидался success: True, но получено: {data_reg.get('success')}"

    with allure.step("2. Попытка логаута БЕЗ токена (ожидаем 401)"):
        # ВАЖНО: Мы НЕ делаем логин и НЕ передаем токен.
        # Мы намеренно вызываем функцию без токена, чтобы проверить защиту сервера.
        logout_resp = delete_users_logout(session, token=None)
        assert logout_resp.status_code == 401, \
            f"Ожидался статус 401 (Unauthorized), но получен {logout_resp.status_code}. Ответ: {logout_resp.text}"

    with allure.step("3. Валидация ответа об ошибке"):
        data = logout_resp.json()
        assert "success" in data, "В ответе отсутствует обязательный ключ 'success'"
        assert data.get("success") is False, \
            f"Ожидался success: False, но получено: {data.get('success')}"

        assert "status" in data, "В ответе отсутствует обязательный ключ 'status'"
        assert data.get("status") == 401, \
            f"Ожидался статус 401 в JSON, но получен: {data.get('status')}"

        assert "message" in data, "В ответе отсутствует сообщение"
        message = data.get("message", "")

        assert "token" in message.lower() or "unauthorized" in message.lower(), \
            f"Некорректное сообщение об ошибке: {message}"