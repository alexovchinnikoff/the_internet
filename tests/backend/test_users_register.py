# test_users_register.py
import requests
from api.services import post_users_register
from api.helpers import get_userdata

def test_users_register():
    session = requests.Session()
    user_data = get_userdata()
    print(f"👤 Регистрируем пользователя: {user_data['email']}")

    register_resp = post_users_register(session, user_data)
    assert register_resp.status_code == 201, f"Ожидался статус 201, но получен {register_resp.status_code}. Ответ: {register_resp.text}"

    data = register_resp.json()
    assert data["success"] is True, f"Ожидался success: True, но получено: {data.get('success')}"
    assert data["status"] == 201, f"Ожидался статус 201, но получен {register_resp.status_code}. Ответ: {register_resp.text}"
    assert data["message"] == 'User account created successfully'
    assert "data" in data, "В ответе отсутствует блок 'data' с данными пользователя"

    data_server = data["data"]
    assert data_server["email"] == user_data.get("email"), f"Email не совпадает! Ожидался {user_data['email']}, но получен {user_from_server.get('email')}"
    assert data_server["name"] == user_data.get("name"), f"Name не совпадает!"
    assert data_server["id"] is not None, "В ответе сервера отсутствует ID пользователя"
    print("✅ Тест 'Регистрация пользователя' пройден успешно!")