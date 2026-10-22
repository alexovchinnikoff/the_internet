# tests/backend/test_delete_account.py
import requests
import allure
from api.services import post_users_register, post_users_login, delete_users_account
from api.helpers import get_userdata


@allure.feature("Управление аккаунтом")
@allure.story("Удаление аккаунта пользователя")
@allure.title("Тест: Удаление аккаунта пользователя")
@allure.description("Проверяет полный цикл: регистрация -> логин -> получение токена -> успешное удаление аккаунта. Валидирует статус, структуру JSON и корректность токена.")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_account():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация"):
        resp = post_users_register(session, user_data)
        assert resp.status_code == 201 and resp.json().get("success")

    with allure.step("2. Логин"):
        resp, token = post_users_login(session, {"email": user_data["email"], "password": user_data["password"]})
        assert resp.status_code == 200 and token

    with allure.step("3. Выполнение удаления аккаунта с передачей токена"):
        delete_resp = delete_users_account(session, token=token)
        assert delete_resp.status_code == 200, \
            (f"Ожидался статус 200 (OK), но получен {delete_resp.status_code}. "
             f"Ответ: {delete_resp.text}")

    with allure.step("4. Валидация ответа сервера на удаление"):
        data = delete_resp.json()
        assert "success" in data, "В ответе отсутствует обязательный ключ 'success'"
        assert data.get("success") is True, \
            f"Ожидался success: True, но получено: {data.get('success')}"
        assert "status" in data, "В ответе отсутствует обязательный ключ 'status'"
        assert data.get("status") == 200, \
            f"Ожидался статус 200 в JSON, но получен {data.get('status')}"
        assert "message" in data, "В ответе отсутствует сообщение"
        message = data.get("message", "")
        assert "Successful" in message or "deleted" in message, \
            f"Некорректное сообщение: {message}"
        assert str(delete_resp.url).endswith("/users/delete-account"), \
            f"Неверный URL запроса: {delete_resp.url}"