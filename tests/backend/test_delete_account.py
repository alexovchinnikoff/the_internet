# test_delete_account.py
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

    delete_resp = delete_users_account(session, token=token)
    assert delete_resp.status_code == 200, f"Ожидался статус 200 при удалении, но получен {delete_resp.status_code}. Ответ: {delete_resp.text}"

    data = delete_resp.json()
    assert data["success"] is True, f"Ожидался success: True, но получено: {data['success']}"
    assert data["status"] == 200, f"Ожидался статус 200 в JSON, но получено: {data['status']}"
    assert data["message"] == "Successful Request" or data["message"] == "Account successfully deleted"
    assert str(delete_resp.url).endswith("/users/delete-account"), f"Неверный URL: {delete_resp.url}"
    print("🎉 Тест 'Удалить аккаунт' пройден успешно!")