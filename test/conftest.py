# import Faker
import pytest
# from constant import HEADERS, BASE_URL
from playwright.sync_api import sync_playwright

# faker = Faker()


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="session")
def auth_session():
    session = requestes.Session()
    session.headers.update(HEADERS)

    response = requestes.post(f"{BASE_URL}/auth", headers=HEADERS, json={"username" : "admin", "password" : "password"})
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    assert token is not None, "В ответе не оказалось токена"