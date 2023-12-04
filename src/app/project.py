from datetime import datetime, timedelta, date
from .task import Task

class Project:
    def __init__(self, title: str, description: str, deadline: date) -> None:
        self.title = title
        self.description = description
        
        if not isinstance(deadline, date) or isinstance(deadline, datetime):
            raise ValueError("deadline должен быть производным от класса datetime.date")
    
        # Проверка, что дедлайн как минимум на один день больше сегодняшней даты
        if deadline < (datetime.now() + timedelta(days=1)).date():
            raise ValueError("Дедлайн должен быть как минимум на один день больше сегодняшней даты.")
        
        self.deadline = deadline
        self.tasks = []  # Список задач внутри проекта

    def add_task(self, task: Task) -> None:
        if task.deadline > self.deadline:
            raise ValueError(f"""Дедлайн для задачи {task.title} больше, 
                             чем дедлайн проекта {self.title} 
                             ({task.deadline} > {self.deadline})""") 
        self.tasks.append(task)

    def get_info(self) -> str:
        result = f"Список задач в проекте '{self.title}':\n"
        for index, task in enumerate(self.tasks):
            result += f'Номер задачи: {index}\n'
            result += task.get_info() + '\n----\n'
        return result


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр проекта
    project1 = Project("Основной проект", "Разработка нового продукта", datetime(2023, 12, 31))

    # Создаем экземпляры задач для проекта
    task1 = Task("Разработка функционала", "Написать код для нового функционала", datetime(2023, 12, 15))
    task2 = Task("Тестирование", "Провести тестирование нового функционала", datetime(2023, 12, 25))

    # Добавляем задачи в проект
    project1.add_task(task1)
    project1.add_task(task2)

    # Выводим информацию о задачах в проекте
    print(project1.get_info())
