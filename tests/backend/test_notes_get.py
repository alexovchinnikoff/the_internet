# tests/backend/test_notes_get.py
import requests
import allure
from api.services import post_users_register, post_users_login, post_notes, get_notes
from api.helpers import get_userdata


@allure.feature("Retrieve a list of notes for the authenticated user")
@allure.story("Получить заметки")
@allure.title("Тест: Получение списка заметок")
@allure.description("Проверяет полный цикл: регистрация -> логин -> создание заметок -> получение списка заметок")
@allure.severity(allure.severity_level.CRITICAL)
def test_notes_get():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация"):
        resp = post_users_register(session, user_data)
        assert resp.status_code == 201 and resp.json().get("success")

    with allure.step("2. Логин"):
        resp, token = post_users_login(session, {"email": user_data["email"], "password": user_data["password"]})
        assert resp.status_code == 200 and token

    categories = ["Home", "Work", "Personal"]
    created_titles = []

    for i, category in enumerate(categories, start=1):
        with allure.step(f"3.{i}. Создание заметки №{i} (Категория: {category})"):
            note_payload = {
                "title": f"Тестовая заметка {category}",
                "description": "Описание тестовой заметки",
                "category": category
            }
            note_resp, note_data = post_notes(session, note_payload, token=token)

            assert note_resp.status_code in [200], \
                f"Ожидался статус 200, но получен {note_resp.status_code}"
            assert note_data.get("success") is True
            assert "data" in note_data
            assert "id" in note_data["data"]
            created_titles.append(note_data["data"]["title"])

    with allure.step("4. Запрос всех заметок"):
        notes_resp, notes_data = get_notes(session, token=token)
        assert notes_resp.status_code == 200, \
            (f"Ожидался статус 200, но получен {notes_resp.status_code}. "
             f"Ответ: {notes_resp.text}")

    with allure.step("5. Валидация ответа сервера на запрос всех заметок"):
        assert notes_data is not None, "Ответ сервера пуст"
        assert notes_data.get("success") is True, \
            f"Ожидался success: True, но получено: {notes_data.get('success')}"
        assert "data" in notes_data, "В ответе отсутствует блок 'data'"

        all_notes = notes_data["data"]
        assert isinstance(all_notes, list), "Поле 'data' должно быть списком заметок"
        assert len(all_notes) >= 3, \
            f"В списке 3 заметки или более. Получено: {len(all_notes)}"

        for title in created_titles:
            found = False
            for note in all_notes:
                if note.get("title") == title:
                    found = True
                    break
            assert found, f"Заметка с заголовком '{title}' не найдена в списке"

        # Проверка структуры первой заметки из списка
        first_note = all_notes[0]
        assert "id" in first_note, "В заметке отсутствует ID"
        assert "title" in first_note, "В заметке отсутствует заголовок"
        assert "category" in first_note, "В заметке отсутствует категория"
        assert "description" in first_note, "В заметке отсутствует описание"