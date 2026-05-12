# pytest_ui_api_template

## Автоматизация тестирования на Python

### Шаги

1. Склонировать проект `git clone https://github.com/kseniyaskada/pytest_ui_api_template.git`
2. Установить все зависимости `pip install -r requirements.txt`
3. В файле config.py подставить данные для авторизации пользователя
4. Запустить тесты и сгенерировать отчет `python -m pytest --alluredir=allure-results`
5. Открыть отчет `allure serve allure-results`

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- config
- json

### Структура:
- ./test - тесты
- ./pages - описание страниц
