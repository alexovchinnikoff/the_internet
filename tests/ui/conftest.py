# tests/ui/conftest.py
import pytest
from playwright.sync_api import Browser, BrowserContext, Playwright, sync_playwright
from typing import Generator


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=100)
    yield browser
    browser.close()


@pytest.fixture
def context(browser: Browser, request) -> Generator[BrowserContext, None, None]:
    # Получаем параметры авторизации из теста
    auth_params = getattr(request, "param", {})

    http_creds = None
    if auth_params:
        http_creds = {
            "username": auth_params.get("username"),
            "password": auth_params.get("password")
        }

    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        http_credentials=http_creds
    )

    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Generator:
    page = context.new_page()
    yield page


'''
import pytest
from playwright.sync_api import Browser, Page, BrowserContext, Playwright, sync_playwright
from typing import Generator

# Фикстура для инициализации playwright
@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    """Создает экземпляр Playwright на всю сессию тестов"""
    with sync_playwright() as playwright:
        yield playwright

# Фикстура для браузера
@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    """Инициализирует браузер на всю сессию тестов"""
    browser = playwright_instance.chromium.launch(
        headless=False,  # False, чтобы видеть браузер
        slow_mo=100      # Замедление для наглядности
    )
    yield browser
    browser.close()

# Фикстура для контекста браузера
@pytest.fixture
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Создает новый контекст для каждого теста"""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    yield context
    context.close()

# ОСНОВНАЯ ФИКСТУРА - только инициализирует браузер и открывает страницу
@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """
    Фикстура, которая только создает страницу.
    Дальнейшие действия (переходы, клики, заполнение форм) выполняются в тесте.
    """
    page = context.new_page()
    yield page
    # Страница закроется автоматически при закрытии контекста
'''