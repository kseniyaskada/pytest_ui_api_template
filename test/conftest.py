import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.AuthPage import AuthPage
# from pages.MainPage import MainPage


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.implicitly_wait(4)
    browser.maximize_window()
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("kseniyaksenya@gmail.com", "ksy199902s")
    yield browser

    browser.quit()
