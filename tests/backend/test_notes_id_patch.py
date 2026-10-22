# tests/backend/test_notes_id_patch.py
import requests
import allure
from api.services import post_users_register, post_users_login, post_notes, get_notes, patch_notes_id
from api.helpers import get_userdata

@allure.feature("Update the completed attribute of the note")
@allure.story("Изменить атрибут заметки (completed)")
@allure.title("Тест: Успешное изменение статуса заметки")
@allure.severity(allure.severity_level.CRITICAL)
def test_notes_id_patch():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация"):
        resp = post_users_register(session, user_data)
        assert resp.status_code == 201 and resp.json().get("success")

    with allure.step("2. Логин"):
        resp, token = post_users_login(session, {"email": user_data["email"], "password": user_data["password"]})
        assert resp.status_code == 200 and token

    with allure.step("3. Создание заметки"):
        payload = {"title": "Test Home", "description": "Desc", "category": "Home"}
        resp, data = post_notes(session, payload, token=token)
        assert resp.status_code in [200, 201] and data.get("success")
        note_id = data["data"]["id"]

    with allure.step("4. Обновление статуса completed на True"):
        upd_payload = {"completed": True}
        resp, data = patch_notes_id(session, note_id=note_id, payload=upd_payload, token=token)
        assert resp.status_code in [200, 201] and data.get("success")
        assert data["data"]["completed"] is True

    with allure.step("5. Проверка списка заметок"):
        resp, data = get_notes(session, token=token)
        assert resp.status_code == 200 and data.get("success")
        assert any(n["id"] == note_id and n["completed"] is True for n in data["data"])