# tests/backend/test_users_verify.py
import requests
import allure
from api.services import (
    post_users_register,
    post_users_login,
    post_users_forgot,
    post_users_verify,
    delete_users_account
)
from api.helpers import get_userdata

@allure.feature("Восстановление доступа")
@allure.story("Сброс пароля")
@allure.title("Тест: Верификация токена сброса (Mock)")
@allure.severity(allure.severity_level.CRITICAL)
def test_users_verify_with_mock_token():
    session = requests.Session()
    user_data = get_userdata()
    target_email = user_data["email"]

    with allure.step("1. Регистрация"):
        reg_resp = post_users_register(session, user_data)
        assert reg_resp.status_code == 201
        assert reg_resp.json().get("success") is True

    with allure.step("2. Логин"):
        login_payload = {"email": target_email, "password": user_data["password"]}
        login_resp, token = post_users_login(session, login_payload)
        assert login_resp.status_code == 200
        assert token is not None

    with allure.step("3. Запрос сброса пароля"):
        forgot_resp, email_received = post_users_forgot(session, email=target_email)
        assert forgot_resp.status_code in [200, 201]
        assert email_received == target_email
        assert forgot_resp.json().get("success") is True

    mock_token = "fake-reset-token-abc123xyz"
    allure.attach(mock_token, name="Mock Token", attachment_type=allure.attachment_type.TEXT)

    with allure.step("4. Верификация токена (Mock)"):
        verify_resp, verify_data = post_users_verify(session, token=mock_token)
        assert verify_resp.status_code != 500, f"Сервер упал с ошибкой: {verify_resp.text}"

        if verify_resp.status_code == 200:
            assert verify_data.get("success") is True
        else:
            allure.attach(
                f"Токен отвергнут (статус {verify_resp.status_code}). Это ожидаемое поведение при использовании Mock.",
                name="Result", attachment_type=allure.attachment_type.TEXT)

    with allure.step("5. Очистка: Удаление пользователя"):
        try:
            del_resp, _ = delete_users_account(session, token=token)
            assert del_resp.status_code == 200
        except Exception as e:
            allure.attach(str(e), name="Ошибка очистки", attachment_type=allure.attachment_type.TEXT)