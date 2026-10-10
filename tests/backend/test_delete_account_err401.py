# test_delete_account_err401.py
import requests
from api.services import post_users_register, post_users_login, delete_users_account
from api.helpers import get_userdata

def test_delete_account():
    session = requests.Session()
    user_data = get_userdata()
    print(f"👤 Тестируем пользователя: {user_data['email']}")

    reg_resp = post_users_register(session, user_data)
    assert reg_resp.status_code == 201, f"Ошибка регистрации: {reg_resp.text}"
    print("✅ Пользователь зарегистрирован")

    login_payload = {
        "email": user_data["email"],
        "password": user_data["password"]
    }

    login_resp, token = post_users_login(session, login_payload)
    assert login_resp.status_code == 200, f"Ошибка логина: {login_resp.text}"
    print(f"🔑 Токен получен")

    delete_resp = delete_users_account(session, token=None)

    assert delete_resp.status_code == 401, f"Ожидался 401, но получен {delete_resp.status_code}"
    data = delete_resp.json()
    assert data["success"] is False
    assert data["status"] == 401
    assert data["message"] == "No authentication token specified in x-auth-token header"
    print(f"✅ Аккаунт не удален! Статус: {delete_resp.status_code}")




