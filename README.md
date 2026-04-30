# pytest_ui_api_template

## Автоматизация тестирования на Python

### Шаги

1. Склонировать проект `git clone https://github.com/kseniyaskada/pytest_ui_api_template.git`
2. Установить все зависимости
3. В файле config.py подставить данные для авторизации
4. Запустить тесты `pytest`
5. Сгенерировать отчет 'allure generate allure-files -o allure-report'
6. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Структура:
- ./test - тесты
- ./pages - описание страниц

### Библиотеки (!)

- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure-pytest