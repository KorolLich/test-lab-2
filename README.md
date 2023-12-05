[![Coverage Status](https://coveralls.io/repos/github/KorolLich/test-lab-2/badge.svg?branch=main)](https://coveralls.io/github/KorolLich/test-lab-2?branch=main)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=KorolLich_test-lab-2&metric=alert_status)](https://sonarcloud.io/dashboard?id=KorolLich_test-lab-2)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=KorolLich_test-lab-2&metric=bugs)](https://sonarcloud.io/summary/new_code?id=KorolLich_test-lab-2)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=KorolLich_test-lab-2&metric=code_smells)](https://sonarcloud.io/dashboard?id=KorolLich_test-lab-2)

# test-lab-2

# План тестирования
# Аттестационное тестирование

## Тест А1 (положительный)
- **Начальное состояние**: Запущена консольная программа `python main.py`
- **Действия пользователя**:
  - Вводит "1" (создать проект) и нажимает Enter
  - Вводит "Test Project", Enter, "Test Description", Enter, "2023-12-31", Enter
- **Ожидаемый результат**: Количество проектов равно 1

## Тест А2 (негативный)
- **Начальное состояние**: Запущена консольная программа `python main.py`
- **Действия пользователя**:
  - Вводит "1" (создать проект) и нажимает Enter
  - Вводит "Test Project", Enter, "Test Description", Enter, "2023-12-31", Enter
  - Вводит "1" (создать проект) и нажимает Enter
  - Вводит "Test Project", Enter, "Test Description", Enter, "2023-12-31", Enter
- **Ожидаемый результат**: Выводится сообщение об ошибке о попытке создать проект с уже существующим названием.

## Тест А3 (положительный)
- **Начальное состояние**: Запущена консольная программа `python main.py`, создан проект с названием "Test Project"
- **Действия пользователя**:
  - Вводит "2" (добавить задачу в проект) и нажимает Enter
  - Вводит "Test Project", Enter, "Test Task", Enter, "Task Description", Enter, "2023-12-15", Enter
- **Ожидаемый результат**: Количество задач в проекте "Test Project" равно 1

## Тест А4 (негативный)
- **Начальное состояние**: Запущена консольная программа `python main.py`
- **Действия пользователя**:
  - Вводит "2" (добавить задачу в проект) и нажимает Enter
  - Вводит "Nonexistent Project", Enter, "Test Task", Enter, "Task Description", Enter, "2023-12-15", Enter
- **Ожидаемый результат**: Выводится сообщение об ошибке о попытке добавления задачи к несуществующему проекту.

## Тест А5 (положительный)
- **Начальное состояние**: Запущена консольная программа `python main.py`, создан проект "Test Project"
- **Действия пользователя**:
  - Вводит "3" (удалить проект) и нажимает Enter
  - Вводит "Test Project", Enter
- **Ожидаемый результат**: Проект "Test Project" успешно удален, и количество проектов равно 0.

## Тест А6 (негативный)
- **Начальное состояние**: Запущена консольная программа `python main.py`
- **Действия пользователя**:
  - Вводит "3" (удалить проект) и нажимает Enter
  - Вводит "Nonexistent Project", Enter
- **Ожидаемый результат**: Выводится сообщение об ошибке о попытке удаления несуществующего проекта.

## Тест А7 (негативный)
- **Начальное состояние**: Запущена консольная программа `python main.py`
- **Действия пользователя**:
  - Вводит "9" (некорректный выбор) и нажимает Enter
- **Ожидаемый результат**: Выводится сообщение: "Неверный выбор. Попробуйте снова.".

# Блочное тестирование
## Класс Task
### Метод __init__(self, title: str, description: str, deadline: date)
#### Тест Б1.1.1 (положительный)
- **Входные данные**: title = "Test Task", description = "Test Description", deadline = (datetime.now() + timedelta(days=7)).date()
- **Ожидаемый результат**: Создание объекта класса Task с полями:
  - title = "Test Task"
  - description = "Test Description"
  - deadline = (datetime.now() + timedelta(days=7)).date()
  - status = StatusType.NEW_TASK
- **Действия пользователя**:
  - Вызвать конструктор Task с указанными входными данными
    
#### Тест Б1.1.2 (негативный)
- **Входные данные**: title = "Test Task", description = "Test Description", deadline = datetime.now() + timedelta(days=7)
- **Ожидаемый результат**: Возникновение исключения ValueError с сообщением "deadline должен быть производным от класса datetime.date"
- **Действия пользователя**:
  - Вызвать конструктор Task с указанными входными данными
    
#### Тест Б1.1.3 (негативный)
- **Входные данные**: title = "Expired Task", description = "Test Description", deadline = (datetime.now() - timedelta(days=1)).date()
- **Ожидаемый результат**: Возникновение исключения ValueError с сообщением "Дедлайн должен быть как минимум на один день больше сегодняшней даты."
- **Действия пользователя**:
  - Вызвать конструктор Task с указанными входными данными

#### Тест Б1.1.4 (негативный)
- **Входные данные**: title = "Expired Task", description = "Test Description", deadline = datetime.now().date()
- **Ожидаемый результат**: Возникновение исключения ValueError с сообщением "Дедлайн должен быть как минимум на один день больше сегодняшней даты."
- **Действия пользователя**:
  - Вызвать конструктор Task с указанными входными данными
    
### Метод change_status(self, new_status: StatusType) -> bool
#### Тест Б1.2.1 (положительный)
- **Начальное состояние**: Создан объект task с title = "Test Task", description = "Test Description", deadline = (datetime.now() + timedelta(days=7)).date()
- **Входные данные**: new_status = StatusType.IN_PROGRESS
- **Ожидаемый результат**: Изменение статуса задачи на "В работе"
- **Действия пользователя**:
  - Вызвать метод change_status с указанными входными данными
  - Проверить, что статус задачи изменен на "В работе"

#### Тест Б1.2.2 (негативный)
- **Начальное состояние**: Создан объект task с title = "Test Task", description = "Test Description", deadline = (datetime.now() + timedelta(days=7)).date(), изменен статус на StatusType.IN_PROGRESS
- **Входные данные**: new_status = StatusType.NEW_TASK
- **Ожидаемый результат**: Метод возвращает False, и статус задачи остается "В работе"
- **Действия пользователя**:
  - Вызвать метод change_status с указанными входными данными
  - Проверить, что метод вернул False
  - Проверить, что статус задачи остался "В работе"

### Метод get_days_before_deadline(self) -> int
#### Тест Б1.3.1 (положительный)
- **Начальное состояние**: Создан объект task с title = "Test Task", description = "Test Description", deadline = (datetime.now() + timedelta(days=1)).date()
- **Ожидаемый результат**: Получение количества дней до дедлайна (1 день)
- **Действия пользователя**:
  - Вызвать метод get_days_before_deadline
  - Проверить, что результат равен 1

### Метод get_info(self) -> str
#### Тест Б1.4.1 (положительный)
- **Начальное состояние**: Создан объект task с title = "Test Task", description = "Test Description", deadline = (datetime.now() + timedelta(days=7)).date()
- **Ожидаемый результат**: Получение информации о задаче в виде строки с соответствующими данными
- **Действия пользователя**:
  - Вызвать метод get_info
  - Проверить, что результат содержит подстроки:
    - "Название задачи: Test Task"
    - "Описание: Test Description"
    - "Статус: Новая задача"
   
## Класс Project
### Метод __init__(self, title: str, description: str, deadline: date) 
#### Тест Б2.1.1 (положительный)
- **Входные данные**: title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Ожидаемый результат**: Создание объекта класса Project с указанными параметрами, пустым списком задач
- **Действия пользователя**:
  - Вызвать конструктор Project с указанными входными данными
  - Проверить, что поля объекта инициализированы корректно

#### Тест Б2.1.1 (негативный)
- **Входные данные**: title = "Invalid Deadline Project", description = "Test Description", deadline = datetime.now()
- **Ожидаемый результат**: Возникновение исключения ValueError с сообщением "deadline должен быть производным от класса datetime.date"
- **Действия пользователя**:
  - Вызвать конструктор Project с указанными входными данными
  - Проверить, что возникло исключение ValueError
 
### Метод add_task(self, task: Task) -> None
#### Тест Б2.2.1 (положительный)
- **Начальное состояние**: Создан объект project с title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Создать задачу task_before с deadline = (datetime.now() + timedelta(days=4)).date()
  - Вызвать метод add_task с task_before
- **Ожидаемый результат**: Задача task_before добавлена в список задач проекта

#### Тест Б2.2.2 (негативный)
- **Начальное состояние**: Создан объект project с title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Создать задачу task_after с deadline = (datetime.now() + timedelta(days=6)).date()
  - Вызвать метод add_task с task_after
- **Ожидаемый результат**: Возникновение исключения ValueError с сообщением "Дедлайн задачи превышает дедлайн проекта"
- **Действия пользователя**:
  - Создать задачу task_same с deadline = (datetime.now() + timedelta(days=5)).date()
  - Вызвать метод add_task с task_same
- **Ожидаемый результат**: Задача task_same добавлена в список задач проекта

### Метод get_info(self) -> str
#### Тест Б2.3.1 (положительный)
- **Начальное состояние**: Создан объект project с title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Создать задачу task1 с deadline = (datetime.now() + timedelta(days=1)).date()
  - Вызвать метод add_task с task1
  - Получить результат метода get_info
- **Ожидаемый результат**: Строка с информацией о проекте, включая информацию о задаче task1

#### Тест Б2.3.2 (положительный)
- **Начальное состояние**: Создан объект project с title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date(), выполнен add_task с task1 из теста Б2.3.1
- **Действия пользователя**:
  - Создать задачу task2 с deadline = (datetime.now() + timedelta(days=3)).date()
  - Вызвать метод add_task с task2
  - Получить результат метода get_info
- **Ожидаемый результат**: Строка с информацией о проекте, включая информацию о задачах task1 и task2

### Метод is_similar_tasks(self, new_task: Task) -> bool
#### Тест Б2.4.1 (положительный)
- **Начальное состояние**: Создан объект project с title = "Project 1", description = "Description 1", deadline = (datetime.now() + timedelta(days=8)).date(), выполнен add_task для task1 = Task("Task 1", "Description 1", (datetime.now() + timedelta(days=6)).date())
- **Действия пользователя**:
  - Создать задачу similar_task с title = "Task 1 New", description = "Description 1", deadline = (datetime.now() + timedelta(days=7)).date()
  - Вызвать метод is_similar_tasks с similar_task
- **Ожидаемый результат**: Метод возвращает True, так как similar_task похож на task1

#### Тест Б2.4.2 (негативный)
- **Начальное состояние**: Создан объект project с title = "Project 2", description = "Description 2", deadline = (datetime.now() + timedelta(days=8)).date(), выполнен add_task для task1 = Task("Task 1", "Description 1", (datetime.now() + timedelta(days=6)).date())
- **Действия пользователя**:
  - Создать задачу dissimilar_task с title = "New 3", description = "Description 3", deadline = (datetime.now() + timedelta(days=7)).date()
  - Вызвать метод is_similar_tasks с dissimilar_task
- **Ожидаемый результат**: Метод возвращает False, так как dissimilar_task не похож на task1

#### Тест Б2.4.3 (положительный)
- **Начальное состояние**: Создан объект project с title = "Project 2", description = "Description 2", deadline = (datetime.now() + timedelta(days=8)).date(), выполнен add_task для task1 = Task("Очень длинное название, много лишних слов не требуется чтобы описать всю боль", "Description 2", (datetime.now() + timedelta(days=6)).date())
- **Действия пользователя**:
  - Создать задачу similar_task с title = "Очень", description = "Description 3", deadline = (datetime.now() + timedelta(days=7)).date()
  - Вызвать метод is_similar_tasks с similar_task
- **Ожидаемый результат**: Метод возвращает True, так как все слова из title similar_task входят в title task1 

#### Тест Б2.4.4 (положительный)
- **Начальное состояние**: Создан объект project с title = "Project 2", description = "Description 2", deadline = (datetime.now() + timedelta(days=8)).date(), выполнен add_task для task1 = Task("угабуга", "Description 2", (datetime.now() + timedelta(days=6)).date())
- **Действия пользователя**:
  - Создать задачу similar_task с title = "Слшком много букав, ыыы, дааа, ееее, угабуга", description = "Description 3", deadline = (datetime.now() + timedelta(days=7)).date()
  - Вызвать метод is_similar_tasks с similar_task
- **Ожидаемый результат**: Метод возвращает True, так как все слова из title task1 входят в title similar_task

#### Тест Б2.4.5 (положительный)
- **Начальное состояние**: Создан объект project с title = "Project 2", description = "Description 2", deadline = (datetime.now() + timedelta(days=8)).date(), выполнен add_task для task1 = Task("^*^%&^%*слово*&$*^*^$*)(*)__0--", "Description 2", (datetime.now() + timedelta(days=6)).date())
- **Действия пользователя**:
  - Создать задачу similar_task с title = "слово", description = "Description 3", deadline = (datetime.now() + timedelta(days=7)).date()
  - Вызвать метод is_similar_tasks с similar_task
- **Ожидаемый результат**: Метод возвращает True, так как название задачи содержит существующую задачу с учетом различных символов

## Класс ProjectManagement
### Метод add_project(self, project: Project) -> None
#### Тест Б3.1.1 (положительный)
- **Начальное состояние**: Создан объект project_management
- **Действия пользователя**:
  - Создать проект project с title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
  - Вызвать метод add_project с project
- **Ожидаемый результат**: Проект добавлен в project_management, список проектов содержит один элемент, и его title равен "Test Project"

#### Тест Б3.1.2 (негативный)
- **Начальное состояние**: Создан объект project_management с одним проектом project с title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Создать проект с дублирующим title = "Test Project", но другим описанием и deadline
  - Вызвать метод add_project с новым проектом
- **Ожидаемый результат**: Возникновение исключения ValueError с сообщением "Проект с таким названием уже существует", project_management.projects не изменился

### Метод add_task_to_project(self, project_title: str, task: Task) -> None
#### Тест Б3.2.1 (положительный)
- **Начальное состояние**: Создан объект project_management с одним проектом project с title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Создать задачу task с title = "Test Task", description = "Task Description", deadline = (datetime.now() + timedelta(days=3)).date()
  - Вызвать метод add_task_to_project с project_title = "Test Project" и task
- **Ожидаемый результат**: Задача добавлена в проект "Test Project", список задач проекта содержит один элемент, и его title равен "Test Task"

#### Тест Б3.2.2 (негативный)
- **Начальное состояние**: Создан объект project_management с одним проектом project с title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Создать задачу task с title = "Test Task", description = "Task Description", deadline = (datetime.now() + timedelta(days=3)).date()
  - Вызвать метод add_task_to_project с project_title = "Nonexistent Project" и task
- **Ожидаемый результат**: Возникновение исключения ValueError с сообщением "Проект с названием Nonexistent Project не существует", список задач проекта не изменился

### Метод get_info(self) -> str
#### Тест Б3.4.1 (положительный)
- **Начальное состояние**: Создан объект project_management с двумя проектами:
  - project1 с title = "Project 1", description = "Description 1", deadline = (datetime.now() + timedelta(days=7)).date()
  - project2 с title = "Project 2", description = "Description 2", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Создать задачу task1 с title = "Task 1", description = "Task Description 1", deadline = (datetime.now() + timedelta(days=2)).date()
  - Создать задачу task2 с title = "Task 2", description = "Task Description 2", deadline = (datetime.now() + timedelta(days=4)).date()
  - Добавить задачу task1 в project1
  - Добавить задачу task2 в project2
- **Ожидаемый результат**: 
  - Строка с информацией о проектах и задачах присутствует в строке вывода функции
  - Проект "Project 1" содержит информацию о своем дедлайне и задаче task1
  - Проект "Project 2" содержит информацию о своем дедлайне и задаче task2
 
### Метод delete_project(self, title: str) -> None
#### Тест Б3.5.1 (положительный)
- **Начальное состояние**: Создан объект project_management с проектом project1: title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Удалить проект "Test Project"
- **Ожидаемый результат**: 
  - Список проектов пуст
  - Проект "Test Project" удален из списка проектов

#### Тест Б3.5.2 (негативный)
- **Начальное состояние**: Создан объект project_management с проектом project1: title = "Test Project", description = "Test Description", deadline = (datetime.now() + timedelta(days=5)).date()
- **Действия пользователя**:
  - Попытка удалить несуществующий проект "Nonexistent Project"
- **Ожидаемый результат**: 
  - Возникновение исключения ValueError с сообщением "Проект 'Nonexistent Project' не найден"
 
# Интеграционное тестирование
## Сценарий создания проекта, добавления задачи, изменения статуса и вывода информации
### Тест И1 (положительный)
- **Начальное состояние**: Создан объект project_management
- **Действия пользователя**:
  - Создать задачу с названием "Integration Task", описанием "Task Description" и дедлайном через 8 дней
  - Изменить статус задачи на "В работе"
  - Создать проект "Integration Project" с описанием "Integration Description" и дедлайном через 10 дней
  - Добавить задачу в проект
  - Изменить статус задачи на "Завершенная задача"
  - Добавить проект в project_management
  - Вывести информацию о проекте и задаче
- **Ожидаемый результат**: 
  - Статус задачи "Завершенная задача" отображается в информации о проекте в ProjectManagement

## Сценарий удаления проекта с задачами
### Тест И2 (положительный)
- **Начальное состояние**: Создан объект project_management
- **Действия пользователя**:
  - Создать проект "Delete Project" с описанием "Delete Description" и дедлайном через 15 дней
  - Добавить задачи "Task 1" и "Task 2" в проект
  - Добавить проект в ProjectManagement
  - Удалить проект "Delete Project" из project_management
- **Ожидаемый результат**: 
  - ProjectManagement не содержит проектов





