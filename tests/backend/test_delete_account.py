# test_delete_account.py
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

    login_resp, token = post_users_login(login_payload)

    assert login_resp.status_code == 200, f"Ошибка логина: {login_resp.text}"

    if not token:
        pytest.fail(
            "Критическая ошибка: Не удалось извлечь токен из ответа логина! "
            "Сервер требует токен в заголовке x-auth-token для логаута."
        )
    print(f"🔑 Токен получен")

    del_acc_resp = delete_users_account(token=token)
    assert del_acc_resp.status_code == 200, f"Ожидался статус 200, но получен {del_acc_resp.status_code}"
    data = del_acc_resp.json()
    assert data["success"] is True
    assert data["status"] == 200
    assert data["message"] == "Successful Request" or data["message"] == "Account successfully deleted"