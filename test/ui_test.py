import allure
import pytest
from pages.MainPage import MainPage


@pytest.mark.ui
@allure.title("Авторизация")
@allure.story("Авторизация")
def auth_test(browser):
    main_page = MainPage(browser)

    with allure.step("Проверить, что URL заканчивается на /home"):
        assert main_page.get_current_url().endswith("home")

@pytest.mark.ui
@allure.title("Открытие страницы поиска")
@allure.story("Переход на страницу")
def search_page_test(browser):
    main_page = MainPage(browser)
    search_page = main_page.open_search_page()

    with allure.step("Проверить, что элемент отображается на странице"):
        assert search_page.is_displayed()

@pytest.mark.ui
@allure.title("Создание новой коллекции")
@allure.story("Создание новой сущности")
def create_new_collection_test(browser):
    main_page = MainPage(browser)
    result = main_page.create_collection()

    with allure.step("Проверить, что коллекция создана"):
        assert result is True

    main_page.delete_collection()

@pytest.mark.ui
@allure.title("Создание нового документа")
@allure.story("Создание новой сущности")
def create_document_test(browser):

    main_page = MainPage(browser)
    main_page.create_collection()
    result = main_page.create_document()
    
    with allure.step("Проверить, что документ создан"):
        assert result.is_displayed()
    main_page.delete_collection()

@pytest.mark.ui
@allure.title("Удаление коллекции")
@allure.story("Удаление сущности")
def delete_collection_test(browser):

    main_page = MainPage(browser)
    main_page.create_collection()
    result = main_page.delete_collection()

    with allure.step("Проверить, что коллекция удалена"):
        assert result is True
