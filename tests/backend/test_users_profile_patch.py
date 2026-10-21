# tests/backend/test_users_profile_get.py
import requests
import allure
from api.services import get_users_profile, post_users_register, post_users_login, patch_users_profile
from api.helpers import get_userdata

@allure.feature("Update the user profile information for the logged-in user")
@allure.story("Изменить информацию в профиля пользователя")
@allure.title("Тест: Успешное изменение и получение информации из профиля пользователя")
@allure.description("Проверяет полный цикл: регистрация -> логин -> получение токена -> изменение имени и добавление телефона и компании -> Получение обновленных даных из профиля. Валидирует статус, структуру JSON и корректность токена.")
@allure.severity(allure.severity_level.BLOCKER)  # Критически важный тест

def test_users_profile():
    session = requests.Session()
    user_data = get_userdata()

    with allure.step("1. Регистрация нового пользователя"):
        reg_resp = post_users_register(session, user_data)
        assert reg_resp.status_code == 201, \
            f"Ожидался статус 201 (Created), но получен {reg_resp.status_code}. Ответ: {reg_resp.text}"

        data_reg = reg_resp.json()
        assert data_reg.get("success") is True, \
            f"Ожидался success: True, но получено: {data_reg.get('success')}"

    with allure.step("2. Логин пользователя и получение токена"):
        login_payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }

        login_resp, token = post_users_login(session, login_payload)
        assert login_resp.status_code == 200, \
            f"Ожидался статус 200 (OK), но получен {login_resp.status_code}. Ответ: {login_resp.text}"
        assert token is not None, "Критическая ошибка: Не удалось извлечь токен из ответа сервера!"

    new_name = "Updated Name for Test"
    new_phone = "9998887766"
    new_company = "Updated Company for Test"
    update_payload = {"name": new_name,
                      "company": new_company,
                      "phone": new_phone}

    with allure.step("4. Изменения в профиле с передачей токена"):
        profile_resp = patch_users_profile(session, token=token, payload=update_payload)
        assert profile_resp.status_code == 200, \
            f"Ожидался статус 200 (OK) от PATCH запроса, но получен {profile_resp.status_code}. Ответ: {profile_resp.text}"

    with allure.step("5. Валидация ответа сервера на изменение данных"):
        data = profile_resp.json()

        assert "success" in data, "В ответе отсутствует обязательный ключ 'success'"
        assert data.get("success") is True, \
            f"Ожидался success: True, но получено: {data.get('success')}"

        assert "status" in data, "В ответе отсутствует обязательный ключ 'status'"
        assert data.get("status") == 200, \
            f"Ожидался статус 200 в JSON, но получен {data.get('status')}"

        assert "message" in data, "В ответе отсутствует сообщение"
        message = data.get("message", "")
        assert "successful" in message or "Profile updated successful" in message.lower(), \
            f"Некорректное сообщение: {message}"

        assert str(profile_resp.url).endswith("/users/profile"), \
            f"Неверный URL запроса: {profile_resp.url}"

    with allure.step("6. Финальная проверка: убеждаемся, что данные действительно обновились"):
        final_resp = get_users_profile(session, token=token)
        assert final_resp.status_code == 200, \
            f"Ожидался 200 при получении профиля, но получен {final_resp.status_code}"

        final_data = final_resp.json()
        updated_name = final_data.get("data", {}).get("name")
        updated_phone = final_data.get("data", {}).get("phone")
        updated_company = final_data.get("data", {}).get("company")
        assert updated_name == new_name, \
            f"Имя не обновилось! Ожидалось '{new_name}', но получено '{updated_name}'"
        assert updated_phone == new_phone, \
            f"Имя не обновилось! Ожидалось '{new_phone}', но получено '{updated_phone}'"
        assert updated_company == new_company, \
            f"Имя не обновилось! Ожидалось '{new_company}', но получено '{updated_company}'"