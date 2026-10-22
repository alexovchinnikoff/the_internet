# tests/backend/test_notes_post.py
import requests
import allure
from api.services import post_users_register, post_users_login, post_notes, get_notes
from api.helpers import get_userdata

@allure.feature("Notes Management")
@allure.story("Create Note")
@allure.title("Тест: Последовательное создание и валидация заметок")
@allure.description("Проверяет создание заметок по одной с немедленной валидацией результата перед созданием следующей.")
@allure.severity(allure.severity_level.CRITICAL)
def test_notes_post_sequential():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация"):
        resp = post_users_register(session, user_data)
        assert resp.status_code == 201 and resp.json().get("success")

    with allure.step("2. Логин"):
        resp, token = post_users_login(session, {"email": user_data["email"], "password": user_data["password"]})
        assert resp.status_code == 200 and token

    categories = ["Home", "Work", "Personal"]
    created_ids = []

    for i, category in enumerate(categories, start=1):
        with allure.step(f"3.{i}. Создание заметки №{i} (Категория: {category}) и немедленная валидация"):
            note_payload = {
                "title": f"Тестовая заметка {category}",
                "description": "Описание тестовой заметки",
                "category": category
            }

            note_resp, note_data = post_notes(session, note_payload, token=token)

            assert note_resp.status_code in [200], \
                f"Ожидался статус 200, но получен {note_resp.status_code}"
            assert note_data is not None, "Ответ сервера пуст"
            assert note_data.get("success") is True, \
                f"Ожидался success: True, но получено: {note_data.get('success')}"
            assert "data" in note_data, "В ответе отсутствует блок 'data'"
            assert "id" in note_data["data"], "В данных заметки отсутствует ID"
            assert "title" in note_data["data"], "В данных заметки отсутствует заголовок"
            assert note_data["data"]["title"] == note_payload["title"], \
                f"Заголовок не совпадает! Ожидался '{note_payload['title']}', но получен '{note_data['data']['title']}'"

            created_ids.append(note_data["data"]["id"])
            allure.attach(f"Created note ID: {note_data['data']['id']}", name=f"Note {category} ID", attachment_type=allure.attachment_type.TEXT)

    with allure.step("4. Финальная проверка: все заметки присутствуют в списке"):
        notes_resp, notes_data = get_notes(session, token=token)
        assert notes_resp.status_code == 200, f"Ожидался статус 200 при получении списка, но получен {notes_resp.status_code}"

        if notes_data and "data" in notes_data:
            all_notes = notes_data["data"]
            assert isinstance(all_notes, list), "Поле 'data' должно быть списком заметок"
            assert len(all_notes) >= 3, f"В списке меньше 3 заметок. Получено: {len(all_notes)}"

            for note_id in created_ids:
                found = False
                for note in all_notes:
                    if note.get("id") == note_id:
                        found = True
                        break
                assert found, f"Заметка с ID '{note_id}' не найдена в списке всех заметок"