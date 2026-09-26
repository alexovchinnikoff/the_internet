# test_users_login.py
from services import post_users_register, post_users_login
from helpers import get_userdata

def test_login_user():
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
    data = login_resp.json()
    assert data["success"] is True
    print("✅ Тест входа в аккаунт пройден успешно!")