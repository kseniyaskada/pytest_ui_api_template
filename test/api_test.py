import allure
from config import BASE_URL, USER_TOKEN

@allure.title("Создание новой коллекции")
@allure.story("Создание новой сущности")
def test_create_collection(api_client):
    response = api_client.create_collection("Новая коллекция")
    collection_id = response.json()["data"]["id"]

    with allure.step("Проверить, что статус код равен 200"):
        assert response.status_code == 200
    with allure.step("Проверить, что имя новой коллекции корректно и отображается"):
        assert response.json()["data"]["name"] == "Новая коллекция"
    
    api_client.delete_collection(collection_id)

@allure.title("Создание нового документа")
@allure.story("Создание новой сущности")
def test_create_document(api_client):
    new_collection = api_client.create_collection("Новая коллекция")
    collection_id = new_collection.json()["data"]["id"]

    response_doc = api_client.create_document("Новый документ", collection_id)
    
    with allure.step("Проверить, что статус код равен 200"):
        assert response_doc.status_code == 200
    with allure.step("Проверить, что имя нового документа корректно и отображается"):
        assert response_doc.json()["data"]["title"] == "Новый документ"
    api_client.delete_collection(collection_id)

@allure.title("Содание ссылки для доступа к коллекции")
@allure.story("Создание ссылки")
def test_create_share_link(api_client):
    new_collection = api_client.create_collection("Новая коллекция")
    collection_id = new_collection.json()["data"]["id"]
    new_document = api_client.create_document("Новый документ", collection_id)
    document_id = new_document.json()["data"]["id"]
    response = api_client.create_share_link(document_id)

    with allure.step("Проверить, что статус код равен 200"):
        assert response.status_code == 200
    api_client.delete_collection(collection_id)

@allure.title("Удаление коллекции")
@allure.story("Удаление сущности")
def test_delete_collection(api_client):
    id_collection = api_client.create_collection("Новая коллекция").json()["data"]["id"]
    response = api_client.delete_collection(id_collection)

    with allure.step("Проверить, что статус код равен 200"):
        assert response.status_code == 200

@allure.title("Добавление коментария в коллекцию")
@allure.story("Добавление комментария")
def test_create_comment(api_client):
    new_collection = api_client.create_collection("Новая коллекция")
    collection_id = new_collection.json()["data"]["id"]
    new_document = api_client.create_document("Новый документ", collection_id)
    document_id = new_document.json()["data"]["id"]
    response = api_client.create_comment(document_id, "Текст комментария")

    with allure.step("Проверить, что статус код равен 200"):
        assert response.status_code == 200
    api_client.delete_collection(collection_id)