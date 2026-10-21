# tests/backend/test_notes_get.py
import requests
import allure
from api.services import post_users_register, post_users_login, post_notes, get_notes
from api.helpers import get_userdata


@allure.feature("Notes Management")
@allure.story("Получить заметки")
@allure.title("Тест: Получение списка заметок")
@allure.description("Проверяет полный цикл: регистрация -> логин -> создание заметок -> получение списка заметок")
@allure.severity(allure.severity_level.CRITICAL)
def test_notes_get():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация нового пользователя"):
        reg_resp = post_users_register(session, user_data)
        assert reg_resp.status_code == 201, f"Ожидался статус 201, но получен {reg_resp.status_code}. Ответ: {reg_resp.text}"
        assert reg_resp.json().get("success") is True

    with allure.step("2. Логин пользователя и получение токена"):
        login_payload = {"email": user_data["email"], "password": user_data["password"]}
        login_resp, token = post_users_login(session, login_payload)
        assert login_resp.status_code == 200, f"Ожидался статус 200, но получен {login_resp.status_code}. Ответ: {login_resp.text}"
        assert token is not None, "Не удалось получить токен"

    with allure.step("3. Создание заметки №1 (Категория: Home)"):
        note_payload = {"title": "Тестовая заметка от автотеста", "description": "Описание тестовой заметки",
                        "category": "Home"}
        note_resp, note_data = post_notes(session, note_payload, token=token)
        _validate_note_response(note_resp, note_data)

    with allure.step("4. Создание заметки №2 (Категория: Work)"):
        note_payload = {"title": "Тестовая заметка от автотеста", "description": "Описание тестовой заметки",
                        "category": "Work"}
        note_resp, note_data = post_notes(session, note_payload, token=token)
        _validate_note_response(note_resp, note_data)

    with allure.step("5. Создание заметки №3 (Категория: Personal)"):
        note_payload = {"title": "Тестовая заметка от автотеста", "description": "Описание тестовой заметки",
                        "category": "Personal"}
        note_resp, note_data = post_notes(session, note_payload, token=token)
        _validate_note_response(note_resp, note_data)

    with allure.step("6. Запрос всех заметок"):
        notes_resp, notes_data = get_notes(session, token=token)
        assert notes_resp.status_code == 200, f"Ожидался статус 200, но получен {notes_resp.status_code}. Ответ: {notes_resp.text}"

        if notes_data:
            assert notes_data.get(
                "success") is True, f"Ожидался success: True, но получено: {notes_data.get('success')}"
            assert "data" in notes_data, "В ответе отсутствует блок 'data'"
            assert len(notes_data["data"]) >= 3, "В списке заметок меньше 3 элементов"


def _validate_note_response(resp, data):
    assert resp.status_code in [200,
                                201], f"Ожидался статус 200 или 201, но получен {resp.status_code}. Ответ: {resp.text}"
    if data:
        assert data.get("success") is True, f"Ожидался success: True, но получено: {data.get('success')}"
        assert "data" in data, "В ответе отсутствует блок 'data'"
        assert "id" in data["data"], "В данных заметки отсутствует ID"