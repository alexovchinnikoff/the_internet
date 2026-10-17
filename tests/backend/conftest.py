# tests/backend/conftest.py
import pytest
import requests

@pytest.fixture
def session():
    """Создает сессию requests для каждого теста"""
    with requests.Session() as s:
        yield s