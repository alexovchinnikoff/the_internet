# api/services.py
import requests
import allure
from .endpoints import (
    url_users_delete_account,
    url_users_register,
    url_users_logout,
    url_users_login,
    url_health_check,
    url_users_reset,
    url_users_change,
    url_users_forgot,
    url_users_verify,
    url_users_profile,
    url_notes,
    # url_notes_id
)

@allure.step("Чек состояния сервера")
def get_health_check(session: requests.Session):
    return session.get(url_health_check)

@allure.step("Регистрация пользователя")
def post_users_register(session: requests.Session, payload: dict):
    return session.post(url_users_register, json=payload)

@allure.step("Создать сессию и логин пользователя")
def get_session(user_data: dict):
    session = requests.Session()
    login_payload = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    response = session.post(url_users_login, json=login_payload)
    data = response.json()
    token = data.get("data", {}).get("token")
    return session, token

@allure.step("Логин пользователя")
def post_users_login(session: requests.Session, payload: dict):
    response = session.post(url_users_login, json=payload)
    data = response.json()
    token = data.get("data", {}).get("token")
    return response, token

@allure.step("Получить информацию о пользователе")
def get_users_profile(session: requests.Session, token=None):
    headers = {}
    if token:
        headers["x-auth-token"] = token
    return session.get(url_users_profile, headers=headers)

@allure.step("Изменить информацию о пользователе")
def patch_users_profile(session: requests.Session, token=None, payload=None):
    if payload is None:
        payload = {}
    headers = {}
    if token:
        headers["x-auth-token"] = token
    response = session.patch(url_users_profile, json=payload, headers=headers)
    return response

@allure.step("Отправить на почту ссылку на сброс пароля")
def post_users_forgot(session: requests.Session, email: str):
    payload = {
        "email": email
    }
    response = session.post(url_users_forgot, json=payload)
    data = response.json()
    server_email = data.get("data", {}).get("email")
    if server_email is None:
        return response, email
    return response, server_email

@allure.step("Сброс пароля меняет токен")
def post_users_verify(session: requests.Session, token: str):
    payload = {
        "token": token
    }
    response = session.post(url_users_verify, json=payload)
    data = response.json()
    if token is None:
        return response, token
    return response, data

@allure.step("Логин пользователя")
def post_users_change(session: requests.Session, payload: dict):
    response = session.post(url_users_change, json=payload)
    data = response.json()
    token = data.get("data", {}).get("token")
    return response, token


@allure.step("Сбросить пароль пользователя (Reset Password)")
def post_users_reset(session: requests.Session, token: str, new_password: str):
    payload = {
        "token": token,
        "newPassword": new_password
    }
    response = session.post(url_users_reset, json=payload)
    data = response.json()
    return response, data

@allure.step("Изменить пароль используя актуальный пароль")
def post_users_change(session: requests.Session, payload: dict, token: str):
    headers = {}
    if token:
        headers["x-auth-token"] = token
    response = session.post(url_users_change, json=payload, headers=headers)
    return response, None

@allure.step("Логаут пользователя")
def delete_users_logout(session: requests.Session, token=None):
    headers = {}
    if token:
        headers["x-auth-token"] = token
    return session.delete(url_users_logout, headers=headers)

@allure.step("Удалить пользователя")
def delete_users_account(session: requests.Session, token=None):
    headers = {}
    if token:
        headers["x-auth-token"] = token
    return session.delete(url_users_delete_account, headers=headers)

@allure.step("Создать заметку")
def post_notes(session: requests.Session, payload: dict, token: str = None):
    headers = {}
    if token:
        headers["x-auth-token"] = token
    response = session.post(url_notes, json=payload, headers=headers)
    data = response.json()
    return response, data

@allure.step("Получить информацию о всех заметках")
def get_notes(session: requests.Session, token: str):
    headers = {}
    if token:
        headers["x-auth-token"] = token
    response = session.get(url_notes, headers=headers)
    data = response.json()
    return response, data

@allure.step("Получить информацию о заметке по ID")
def get_notes_id(session: requests.Session, note_id: str, token: str):
    url = f"{url_notes}/{note_id}"
    headers = {}
    if token:
        headers["x-auth-token"] = token
    response = session.get(url, headers=headers)
    data = response.json()
    return response, data

@allure.step("Изменить заметку c названием, описанием, категорией и ID пользователя")
def put_notes_id(session: requests.Session, note_id: str, payload: dict, token: str = None):
    url = f"{url_notes}/{note_id}"
    headers = {}
    if token:
        headers["x-auth-token"] = token
    response = session.put(url, json=payload, headers=headers)
    data = response.json()
    return response, data

@allure.step("Изменить атрибут в заметке")
def patch_notes_id(session: requests.Session, note_id: str, payload: dict, token: str = None):
        url = f"{url_notes}/{note_id}"
        headers = {}
        if token:
            headers["x-auth-token"] = token
        response = session.patch(url, json=payload, headers=headers)
        data = response.json()
        return response, data

@allure.step("Удалить заметку")
def delete_notes_id(session: requests.Session, note_id: str, token: str = None):
        url = f"{url_notes}/{note_id}"
        headers = {}
        if token:
            headers["x-auth-token"] = token
        response = session.delete(url, headers=headers)
        data = response.json()
        return response, data