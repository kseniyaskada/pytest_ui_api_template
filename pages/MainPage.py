import allure
from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть страницу поиска")
    def open_search_page(self) -> bool:
        self.__driver.find_element(By.CSS_SELECTOR, '[href="/search"]').click()
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "._styledInput_oof1d_6")))
        search_input = self.__driver.find_element(
            By.CSS_SELECTOR, "._styledInput_oof1d_6")
        return search_input

    @allure.step("Создать коллекцию")
    def create_collection(self) -> bool:
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="sidebar-action-новая-коллекция"]'
        ).click()
        WebDriverWait(self.__driver, 15).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '[placeholder="Имя"]'))
        )
        self.__driver.find_element(
            By.CSS_SELECTOR, '[placeholder="Имя"]').send_keys("New collection")
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]').click()
        new_collect = self.__driver.find_element(
            By.CSS_SELECTOR, 'a[title="New collection"]')
        return new_collect.is_displayed()

    @allure.step("Создать документ")
    def create_document(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="create-document-button"]'
        ).click()
        WebDriverWait(self.__driver, 15).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '[title="Без названия"]'))
        )
        new_doc = self.__driver.find_element(
            By.CSS_SELECTOR, 'a[title="Без названия"]')
        return new_doc

    @allure.step("Удалить коллекцию")
    def delete_collection(self) -> bool:
        self.__driver.find_element(
            By.CSS_SELECTOR, 'a[title="New collection"]').click()
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="collection-actions-button"]'
        ).click()
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="collection-menu-item-delete"]'
        ).click()
        WebDriverWait(self.__driver, 15).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '[data-testid='
                '"collection-delete-confirm-button"]'))
        )
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="collection-delete-confirm-button"]'
        ).click()
        WebDriverWait(self.__driver, 10).until(
            EC.invisibility_of_element_located((
                By.CSS_SELECTOR, '[title="New collection"]')))
        return True
