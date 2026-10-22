# tests/backend/test_notes_id_get.py
import requests
import allure
from api.services import post_users_register, post_users_login, post_notes, get_notes_id
from api.helpers import get_userdata


@allure.feature("Retrieve a note by ID")
@allure.story("Получить заметку по ID")
@allure.title("Тест: Получение заметки по ID")
@allure.description("Проверяет полный цикл: регистрация -> логин -> создание заметки -> получение конкретной заметки по ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_notes_get_by_id():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация"):
        resp = post_users_register(session, user_data)
        assert resp.status_code == 201 and resp.json().get("success")

    with allure.step("2. Логин"):
        resp, token = post_users_login(session, {"email": user_data["email"], "password": user_data["password"]})
        assert resp.status_code == 200 and token

    categories = ["Home", "Work", "Personal"]
    created_notes = []

    for i, category in enumerate(categories, start=1):
        with allure.step(f"3.{i}. Создание заметки №{i} (Категория: {category})"):
            note_payload = {
                "title": f"Тестовая заметка {category}",
                "description": "Описание тестовой заметки",
                "category": category
            }
            note_resp, note_data = post_notes(session, note_payload, token=token)
            assert note_resp.status_code in [200, 201], \
                f"Ожидался статус 200/201, но получен {note_resp.status_code}"
            assert note_data.get("success") is True
            assert "data" in note_data
            assert "id" in note_data["data"]
            assert "title" in note_data["data"]
            created_notes.append(note_data["data"])

    target_note = created_notes[0]
    target_id = target_note["id"]
    target_title = target_note["title"]

    with allure.step(f"4. Запрос заметки по ID: {target_id}"):
        note_resp, note_data = get_notes_id(session, note_id=target_id, token=token)
        assert note_resp.status_code == 200, \
            (f"Ожидался статус 200, но получен {note_resp.status_code}. "
             f"Ответ: {note_resp.text}")
        assert note_data is not None
        assert note_data.get("success") is True

    with allure.step("5. Валидация данных полученной заметки"):
        assert "data" in note_data
        result_note = note_data["data"]
        assert "id" in result_note
        assert result_note["id"] == target_id
        assert "title" in result_note
        assert result_note["title"] == target_title
        assert "category" in result_note
        assert result_note["category"] == target_note["category"]