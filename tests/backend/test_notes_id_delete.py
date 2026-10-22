# tests/backend/test_notes_id_delete.py
import requests
import allure
from api.services import post_users_register, post_users_login, post_notes, get_notes, delete_notes_id
from api.helpers import get_userdata

@allure.feature("Delete a note")
@allure.story("Удалить заметку")
@allure.title("Тест: Успешное удаление заметки")
@allure.severity(allure.severity_level.CRITICAL)
def test_notes_id_delete():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация"):
        resp = post_users_register(session, user_data)
        assert resp.status_code == 201 and resp.json().get("success")

    with allure.step("2. Логин"):
        resp, token = post_users_login(session, {"email": user_data["email"], "password": user_data["password"]})
        assert resp.status_code == 200 and token

    with allure.step("3. Создание заметки"):
        payload = {"title": "To Delete", "description": "Desc", "category": "Home"}
        resp, data = post_notes(session, payload, token=token)
        assert resp.status_code in [200, 201] and data.get("success")
        note_id = data["data"]["id"]

    with allure.step("4. Проверка наличия заметки перед удалением"):
        resp, data = get_notes(session, token=token)
        assert resp.status_code == 200 and data.get("success")
        assert any(n["id"] == note_id for n in data["data"]), "Заметка не найдена в списке перед удалением"

    with allure.step("5. Удаление заметки"):
        # Передаем note_id внутрь функции
        delete_resp, delete_data = delete_notes_id(session, note_id=note_id, token=token)
        # Сервер может вернуть 200 (с сообщением) или 204 (пусто)
        assert delete_resp.status_code in [200, 204], f"Ожидался статус 200 или 204, но получен {delete_resp.status_code}"

    with allure.step("6. Проверка, что заметка удалена из списка"):
        resp, data = get_notes(session, token=token)
        assert resp.status_code == 200 and data.get("success")
        # Проверяем, что заметки с таким ID больше нет в списке
        assert not any(n["id"] == note_id for n in data["data"]), "Заметка все еще присутствует в списке после удаления!"