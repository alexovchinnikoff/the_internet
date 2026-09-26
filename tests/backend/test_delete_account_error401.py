# test_delete_account_error401.py
from services import post_users_register, post_users_login, delete_users_account
from helpers import get_userdata

def test_delete_account():
    user_data = get_userdata()
    print(f"👤 Тестируем пользователя: {user_data['email']}")

    reg_resp = post_users_register(user_data)
    assert reg_resp.status_code == 201, f"Ошибка регистрации: {reg_resp.text}"
    print("✅ Пользователь зарегистрирован")

    login_payload = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_resp = post_users_login(login_payload)
    assert login_resp.status_code == 200, f"Ожидался 200, но получен {login_resp.status_code}"

    del_acc_resp = delete_users_account()
    assert del_acc_resp.status_code == 401, f"Ожидался 401, но получен {del_acc_resp.status_code}"
    data = del_acc_resp.json()
    assert data["success"] is False
    assert data["status"] == 401
    assert data["message"] == "No authentication token specified in x-auth-token header"
    print(f"✅ Аккаунт не удален! Статус: {del_acc_resp.status_code}")




