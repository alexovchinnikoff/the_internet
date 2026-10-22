# tests/backend/test_users_reset.py
import requests
import allure
from api.services import (
    post_users_register,
    post_users_login,
    post_users_forgot,
    post_users_reset,
    delete_users_account
)
from api.helpers import get_userdata


@allure.feature("Восстановление доступа")
@allure.story("Сброс пароля")
@allure.title("Тест: Сброс пароля (Mock Token - Проверка защиты)")
@allure.severity(allure.severity_level.CRITICAL)
def test_users_reset():
    session = requests.Session()
    user_data = get_userdata()
    target_email = user_data["email"]
    old_password = user_data["password"]
    new_password = "NewSecurePass123!"

    mock_token = "fake-reset-token-abc123xyz"
    allure.attach(mock_token, name="Mock Token", attachment_type=allure.attachment_type.TEXT)

    with allure.step("1. Регистрация пользователя"):
        reg_resp = post_users_register(session, user_data)
        assert reg_resp.status_code == 201
        assert reg_resp.json().get("success") is True

    with allure.step("2. Логин (Старый пароль)"):
        login_payload = {
            "email": target_email,
            "password": old_password
        }
        login_resp, token = post_users_login(session, login_payload)
        assert login_resp.status_code == 200
        assert token is not None

    with allure.step("3. Запрос на сброс пароля"):
        forgot_resp, email_received = post_users_forgot(session, email=target_email)
        assert forgot_resp.status_code in [200, 201]
        assert email_received == target_email
        assert forgot_resp.json().get("success") is True

    with allure.step("4. Попытка сброса пароля с НЕВАЛИДНЫМ токеном"):
        reset_resp, reset_data = post_users_reset(session, token=mock_token, new_password=new_password)

        # Сервер ДОЛЖЕН отвергнуть фейковый токен. Если тут 200 — значит, API не проверяет токены (баг).
        assert reset_resp.status_code != 200, \
            f"Ожидался отказ (400/401), но сервер принял фейковый токен! Статус: {reset_resp.status_code}"

        # Дополнительно: убедимся, что сервер честно сказал, что токен неверен
        if reset_data:
            assert reset_data.get("success") is False, "Ожидался success: False при неверном токене"

    with allure.step("5. Проверка: Старый пароль всё ещё работает"):
        # Так как сброс не прошел, старый пароль должен работать
        good_login_payload = {
            "email": target_email,
            "password": old_password
        }
        good_login_resp, _ = post_users_login(session, good_login_payload)
        assert good_login_resp.status_code == 200

    with allure.step("6. Проверка: Новый пароль НЕ работает"):
        # Так как сброс не прошел, новый пароль не должен работать
        bad_login_payload = {
            "email": target_email,
            "password": new_password
        }
        bad_login_resp, _ = post_users_login(session, bad_login_payload)
        assert bad_login_resp.status_code != 200

    with allure.step("7. Очистка: Удаление пользователя"):
        try:
            # Используем токен от старого пароля для удаления
            del_resp, _ = delete_users_account(session, token=token)
            assert del_resp.status_code == 200
        except Exception as e:
            allure.attach(str(e), name="Ошибка очистки", attachment_type=allure.attachment_type.TEXT)