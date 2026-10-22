# tests/backend/test_users_change.py
import requests
import allure
from api.services import post_users_register, post_users_login, post_users_change
from api.helpers import get_userdata


@allure.feature("Change a user's password")
@allure.story("Смена пароля")
@allure.title("Тест: Смена пароля и проверка доступа")
@allure.description("Проверяет полный цикл: регистрация -> логин -> смена пароля -> проверка старого и нового пароля.")
@allure.severity(allure.severity_level.CRITICAL)
def test_users_change():
    session = requests.Session()
    user_data = get_userdata()

    new_password = "StrongPass123!"
    old_password = user_data["password"]
    email = user_data["email"]

    with allure.step("1. Регистрация"):
        resp = post_users_register(session, user_data)
        assert resp.status_code == 201 and resp.json().get("success")

    with allure.step("2. Логин"):
        resp, token = post_users_login(session, {"email": user_data["email"], "password": user_data["password"]})
        assert resp.status_code == 200 and token

    with allure.step("3. Смена пароля на новый"):
        change_payload = {
            "email": email,
            "currentPassword": old_password,
            "newPassword": new_password
        }
        change_resp, _ = post_users_change(session, change_payload, token=token)
        assert change_resp.status_code == 200, \
            (f"Ожидался статус 200, но получен {change_resp.status_code}. "
             f"Ответ: {change_resp.text}")
        assert change_resp.json().get("success") is True

    with allure.step("4. Проверка: Старый пароль больше НЕ работает"):
        bad_login_payload = {
            "email": email,
            "password": old_password
        }
        bad_login_resp, _ = post_users_login(session, bad_login_payload)
        assert bad_login_resp.status_code != 200, \
            (f"Старый пароль все еще работает! Статус: {bad_login_resp.status_code}. "
             f"Ответ: {bad_login_resp.text}")

    with allure.step("5. Проверка: Новый пароль работает"):
        good_login_payload = {
            "email": email,
            "password": new_password
        }
        good_login_resp, new_token = post_users_login(session, good_login_payload)
        assert good_login_resp.status_code == 200, \
            (f"Ожидался статус 200, но получен {good_login_resp.status_code}. "
             f"Ответ: {good_login_resp.text}")
        assert new_token is not None, "Не удалось получить токен с новым паролем"