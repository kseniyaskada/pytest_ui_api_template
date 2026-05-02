import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import allure
import pytest
from pages.AuthPage import AuthPage
from pages.ApiClient import ApiClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config import USER_LOGIN, USER_PASSWORD

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=chrome_options)
        browser.implicitly_wait(4)
        browser.maximize_window()
        auth_page = AuthPage(browser)
        auth_page.go()
        auth_page.login_as(USER_LOGIN, USER_PASSWORD)
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client():
    return ApiClient()