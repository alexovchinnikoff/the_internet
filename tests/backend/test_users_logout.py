#test_users_logout.py
import requests
from api.services import post_users_register, post_users_login, delete_users_logout
from api.helpers import get_userdata

def test_users_logout():
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

    logout_resp = delete_users_logout(session, token=token)
    assert logout_resp.status_code == 200, f"Ожидался статус 200, но получен {logout_resp.status_code}"

    data = logout_resp.json()
    assert data["success"] is True, f"Ожидался success: True, но получено: {data.get('success')}"
    assert data["status"] == 200, f"Ожидался статус 200, но получен {logout_resp.status_code}"
    assert data["message"] == "Successful Request" or data["message"] == "User has been successfully logged out"
    assert str(logout_resp.url).endswith("/users/logout"), f"Неверный URL: {logout_resp.url}"
    print("🎉 Тест 'Logout' пройден успешно!")