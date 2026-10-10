# test_users_login.py
import requests
from api.services import post_users_register, post_users_login
from api.helpers import get_userdata

def test_login_user():
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
    print("🚀 Отправляем запрос на логин...")

    login_resp, token = post_users_login(session, login_payload)
    assert login_resp.status_code == 200, f"Ожидался 200, но получен {login_resp.status_code}, ответ: {login_resp.text}"
    print(f"🔑 Токен получен: {token}")

    data = login_resp.json()
    assert data["success"] is True, f"Ожидался success: True, но получено: {data['success']}"
    assert data["status"] == 200, f"Ожидался статус 200 в JSON, но получено: {data['status']}"
    assert data["message"] == "Login successful"

    data_server = data.get("data")
    assert data_server["email"] == user_data.get("email"), f"Email не совпадает! Ожидался {user_data['email']}, но получен {user_from_server.get('email')}"
    assert data_server["name"] == user_data.get("name"), f"Name не совпадает!"
    assert data_server["id"] is not None, "В ответе сервера отсутствует ID пользователя"
    assert data_server["token"] == token, f"token не совпадает!"
    print("✅ Тест входа в аккаунт пройден успешно!")