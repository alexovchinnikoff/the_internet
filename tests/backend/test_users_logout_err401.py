#test_users_logout_err401.py
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

    logout_resp = delete_users_logout(session)
    assert logout_resp.status_code == 401, f"Ожидался 401, получил {logout_resp.status_code}"
    print("✅ Тест прошел!") 