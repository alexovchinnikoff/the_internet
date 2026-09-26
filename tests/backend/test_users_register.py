# test_users_register.py
from services import post_users_register
from helpers import get_userdata

def test_users_register():
    user_data = get_userdata()
    print(f"Регистрируем: {user_data['email']}")

    register_resp = post_users_register(user_data)
    assert register_resp.status_code == 201, f"Ожидался 201, но получен {register_resp.status_code}"
    data = register_resp.json()
    assert data["success"] is True
    assert "data" in data
    assert data["data"]["email"] == user_data["email"]
    assert data["data"]["name"] == user_data["name"]
    assert data["data"]["id"] is not None
    print("✅ Тест регистрации пройден успешно!")