# test_health_check_error.py
from services import get_health_check

def test_get_health_check_error():
    response = get_health_check()
    assert response.status_code == 500
    assert response.json().get("success") is False
    assert response.json().get("status")  == 500
    assert response.json().get("message") == "Internal Error Server"