# from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
# from time import sleep


def auth_test(browser):
    main_page = MainPage(browser)

    assert main_page.get_current_url().endswith("home")


def search_page_test(browser):
    main_page = MainPage(browser)
    search_page = main_page.open_search_page()

    assert search_page.is_displayed()


def create_new_collection_test(browser):
    main_page = MainPage(browser)
    result = main_page.create_collection()

    assert result.is_displayed()
    main_page.delete_collection()


def create_document_test(browser):

    main_page = MainPage(browser)
    main_page.create_collection()
    result = main_page.create_document()

    assert result.is_displayed()
    main_page.delete_collection()


def delete_collection_test(browser):

    main_page = MainPage(browser)
    main_page.create_collection()
    result = main_page.delete_collection()

    assert result is True
