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
