# tests/backend/test_users_forgot.py
import requests
import allure
from api.services import post_users_register, post_users_login, delete_users_logout, post_users_forgot
from api.helpers import get_userdata

@allure.feature("Sends a password reset link to the user's email address, allowing them to reset their password")
@allure.story("Сброс пароля")
@allure.title("Тест: Ссылка на сброс пароля отправляется на почту")
@allure.description("Проверяет полный цикл: регистрация -> логин -> получение токена -> успешный логаут-> отправка ссылки на сброс пароля на почту. Валидирует статус, структуру JSON и корректность токена.")
@allure.severity(allure.severity_level.CRITICAL)

def test_users_forgot():
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

    with allure.step("3. Выполнение логаута с передачей токена"):
        logout_resp = delete_users_logout(session, token=token)
        assert logout_resp.status_code == 200, \
            f"Ожидался статус 200 (OK), но получен {logout_resp.status_code}. Ответ: {logout_resp.text}"

    with allure.step("4. Валидация ответа сервера на логаут"):
        data = logout_resp.json()
        assert "success" in data, "В ответе отсутствует обязательный ключ 'success'"
        assert data.get("success") is True, \
            f"Ожидался success: True, но получено: {data.get('success')}"

        assert "status" in data, "В ответе отсутствует обязательный ключ 'status'"
        assert data.get("status") == 200, \
            f"Ожидался статус 200 в JSON, но получен {data.get('status')}"

        assert "message" in data, "В ответе отсутствует сообщение"
        message = data.get("message", "")
        assert "successful" in message or "Password reset link successfully sent to practice@expandtesting.com. Please verify by clicking on the given link" in message, \
            f"Некорректное сообщение: {message}"

        assert str(logout_resp.url).endswith("/users/logout"), \
            f"Неверный URL запроса: {logout_resp.url}"

    target_email = user_data["email"]

    with allure.step(f"Отправка запроса на сброс пароля для {target_email}"):
        resp, email_received = post_users_forgot(session, email=target_email)
        assert resp.status_code == 200, f"Ожидался 200, но получен {resp.status_code}"

        data = resp.json()
        assert data.get("success") is True, f"Ожидался success: True, но получено: {data.get('success')}"

        assert email_received == target_email, f"Email не совпадает! Ожидался {target_email}, получен {email_received}"