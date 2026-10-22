# tests/backend/test_notes_get.py
import requests
import allure
from api.services import post_users_register, post_users_login, post_notes, get_notes
from api.helpers import get_userdata


@allure.feature("Retrieve a list of notes for the authenticated user")
@allure.story("Получить заметки")
@allure.title("Тест: Создание одной заметки (Home) и проверка ответа")
@allure.description("Проверяет цикл: регистрация -> логин -> создание одной заметки категории Home -> валидация ответа")
@allure.severity(allure.severity_level.CRITICAL)
def test_note_home_post():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация"):
        resp = post_users_register(session, user_data)
        assert resp.status_code == 201 and resp.json().get("success")

    with allure.step("2. Логин"):
        resp, token = post_users_login(session, {"email": user_data["email"], "password": user_data["password"]})
        assert resp.status_code == 200 and token

    with allure.step("3. Создание одной заметки (Категория: Home)"):
        note_payload = {
            "title": "Тестовая заметка Home",
            "description": "Описание тестовой заметки Home",
            "category": "Home"
        }
        note_resp, note_data = post_notes(session, note_payload, token=token)
        assert note_resp.status_code in [200], \
            (f"Ожидался статус 200, но получен {note_resp.status_code}. "
             f"Ответ: {note_resp.text}")
        assert note_data is not None
        assert note_data.get("success") is True
        assert "data" in note_data

        created_note = note_data["data"]
        assert "id" in created_note
        assert "title" in created_note
        assert created_note["title"] == "Тестовая заметка Home"
        assert created_note["category"] == "Home"

    with allure.step("4. Проверка наличия созданной заметки в общем списке"):
        notes_resp, notes_data = get_notes(session, token=token)
        assert notes_resp.status_code == 200, \
            (f"Ожидался статус 200, но получен {notes_resp.status_code}. "
             f"Ответ: {notes_resp.text}")
        assert notes_data is not None
        assert notes_data.get("success") is True
        assert "data" in notes_data