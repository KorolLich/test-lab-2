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

## Тест А8 (негативный)
- **Начальное состояние**: Запущена консольная программа `python main.py`
- **Действия пользователя**:
  - Вводит "9" (некорректный выбор) и нажимает Enter
- **Ожидаемый результат**: Выводится сообщение: "Неверный выбор. Попробуйте снова.".

