# services.py
import requests
from endpoints import (
    URL,
    ep_users_delete_account,
    ep_users_register,
    ep_users_logout,
    ep_users_login,
    ep_health_check
)

def post_users_register(payload: dict):
    print(f"🚀 РЕГИСТРАЦИЯ: Отправляем на {ep_users_register}")
    return requests.post(ep_users_register, json=payload)

def post_users_login(payload: dict):
    print(f"🚀 ЛОГИН: Отправляем на {ep_users_login}")
    return requests.post(ep_users_login, json=payload)

def get_health_check():
    return requests.get(ep_health_check)

def delete_users_logout():
    print(f"🚀 ЛОГАУТ: Отправляем на {ep_users_logout}")
    return requests.delete(ep_users_logout)

def delete_users_account():
    return requests.delete(ep_users_delete_account)




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