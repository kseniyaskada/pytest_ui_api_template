import requests
import allure
from config import BASE_URL, USER_TOKEN


class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            'Authorization': f'Bearer {USER_TOKEN}',
            'Content-Type': 'application/json'
        }

    @allure.step("Создать коллекцию")
    def create_collection(self, name: str) -> list:
        url = self.base_url + "/collections.create"
        payload = {
            "name": name
        }
        return requests.post(url, headers=self.headers, json=payload)

    @allure.step("Создать документ")
    def create_document(self, name: str, collection_id: str) -> list:
        url = self.base_url + "/documents.create"
        payload = {
            "title": name,
            "collectionId": collection_id
        }
        return requests.post(url, headers=self.headers, json=payload)

    @allure.step("Создать ссылку для доступа к документу")
    def create_share_link(self, document_id: str) -> list:
        url = self.base_url + "/shares.create"
        payload = {
            "documentId": document_id
        }
        return requests.post(url, headers=self.headers, json=payload)

    @allure.step("Удалить коллекцию")
    def delete_collection(self, id: str) -> list:
        url = self.base_url + "/collections.delete"
        payload = {
            "id": id
        }
        return requests.post(url, headers=self.headers, json=payload)
    
    @allure.step("Создать комментарий")
    def create_comment(self, entity_id: str, text: str) -> list:
        url = self.base_url + "/comments.create"
        payload = {
            "entityId": entity_id,
            "entityType": "document",
            "text": text
        }
        return requests.post(url, headers=self.headers, json=payload)