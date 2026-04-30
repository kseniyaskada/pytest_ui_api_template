import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = (
            "https://auth.yonote.ru/realms/yonote"
            "/protocol/openid-connect/auth?response_type=code&redirect_uri"
            "=https%3A%2F%2Fapp.yonote.ru%2Fauth%2Foidc.callback&scope=openid"
            "%20email&state=f1ca5acc028145ff&client_id=yonote"
        )
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self) -> None:
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str) -> None:
        self.__driver.find_element(
            By.CSS_SELECTOR, "#username").send_keys(email)
        self.__driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#kc-login").click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "._title_c3h4h_1")))

        self.__driver.find_element(By.CSS_SELECTOR, "._title_c3h4h_1").click()
