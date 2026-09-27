# services.py
import requests
from endpoints import (
    URL,
    url_users_delete_account,
    url_users_register,
    url_users_logout,
    url_users_login,
    url_health_check
)

session = requests.Session()

def post_users_register(payload: dict):
    print(f"🚀 РЕГИСТРАЦИЯ: Отправляем на {url_users_register}")
    return requests.post(url_users_register, json=payload)

def post_users_login(payload: dict):
    print(f"🚀 ЛОГИН: Отправляем на {url_users_login} и вынимаем из ответа токен")
    response = session.post(url_users_login, json=payload)
    data = response.json()
    token = data.get("data", {}).get("token")
    return response, token

def get_health_check():
    return requests.get(url_health_check)

def delete_users_logout(token=None):
    print(f"🚀 ЛОГAУТ: Отправляем на {url_users_logout} c токеном в заголовках")
    headers = {}
    if token:
        headers["x-auth-token"] = token
    return session.delete(url_users_logout, headers=headers)

def delete_users_account(token=None):
    print(f"🚀 УДАЛИТЬ АККАУНТ: Отправляем на {url_users_delete_account} c токеном в заголовках")
    headers = {}
    if token:
        headers["x-auth-token"] = token
    return requests.delete(url_users_delete_account, headers=headers)




'''
import httpx
from data import URL, users_register_body
def get_health_check():
    url = f"{URL}/health-check"
    with httpx.Client() as client:
        return client.get(url)

def post_users_register():
    url = f"{URL}/users/register"
    with httpx.Client() as client:
        return client.post(url, json=users_register_body)

def get_id(post_users_register):
    id = post_users_register.json()["id"]
    return id

def post_users_login():
    url = f"{URL}/api/users/login"
    with httpx.Client() as client:
        return client.post(url, json=users_register_body)

def post_users_login(payload: dict) -> httpx.Response:
    url = f"{URL}/api/users/login"
    return httpx.post(url, json=payload)

def delete_users_logout():
    url = f"{URL}/users/logout"
    with httpx.Client() as client:
        return client.delete(url)

def delete_users_account():
    url = f"{URL}/users/delete-account"
    with httpx.Client() as client:
        return client.delete(url)
'''