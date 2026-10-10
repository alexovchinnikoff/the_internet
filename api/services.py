# services.py
import requests
import allure
from .endpoints import (
    url_users_delete_account,
    url_users_register,
    url_users_logout,
    url_users_login,
    url_health_check
)

@allure.step("Создаем сессию и логиним пользователя")
def get_session(user_data: dict):
    session = requests.Session()
    login_payload = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    response = session.post(url_users_login, json=login_payload)
    data = response.json()
    token = data.get("data", {}).get("token")
    print(f"🔑 get_session(): Логин успешен, токен получен: {token}")
    return session, token

@allure.step("Регистрируем пользователя")
def post_users_register(session: requests.Session, payload: dict):
    return session.post(url_users_register, json=payload)

@allure.step("Логин пользователя")
def post_users_login(session: requests.Session, payload: dict):
    response = session.post(url_users_login, json=payload)
    data = response.json()
    token = data.get("data", {}).get("token")
    return response, token

@allure.step("Чек состояния сервера")
def get_health_check(session: requests.Session):
    return session.get(url_health_check)

@allure.step("Логаут пользователя")
def delete_users_logout(session: requests.Session, token=None):
    headers = {"x-auth-token": token}
    return session.delete(url_users_logout, headers=headers)

@allure.step("Удалить пользователя")
def delete_users_account(session: requests.Session, token=None):
    headers = {"x-auth-token": token}
    return session.delete(url_users_delete_account, headers=headers)