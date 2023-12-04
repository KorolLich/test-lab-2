from datetime import datetime, timedelta
from task import Task

class Project:
    def __init__(self, title: str, description: str, deadline: datetime) -> None:
        self.title = title
        self.description = description
        # Проверка, что дедлайн как минимум на один день больше сегодняшней даты
        if deadline < datetime.now() + timedelta(days=1):
            raise ValueError("Дедлайн должен быть как минимум на один день больше сегодняшней даты.")
        
        self.deadline = deadline
        self.tasks = []  # Список задач внутри проекта

    def add_task(self, task: Task) -> None:
        if task.deadline > self.deadline:
            f_task_deadline = task.deadline.strftime("%Y-%m-%d")
            f_project_deadline = self.deadline.strftime("%Y-%m-%d")
            raise ValueError(f"""Дедлайн для задачи {task.title} больше, 
                             чем дедлайн проекта {self.title} 
                             ({f_task_deadline} > {f_project_deadline})""") 
        self.tasks.append(task)

    def show_task_list(self) -> None:
        print(f"Список задач в проекте '{self.title}':")
        for index, task in enumerate(self.tasks):
            print('Номер задачи: ', index)
            print(task.get_info())
            print("----")

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
    project1.show_task_list()
