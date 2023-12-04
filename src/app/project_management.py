from project import Project
from datetime import datetime
from task import Task

class ProjectManagement:
    def __init__(self) -> None:
        self.projects = []  # Список проектов в системе

    def create_project(self, title: str, description: str, deadline: datetime) -> None:
        for project in self.projects:
            if project.title == title:
                raise ValueError("Название проекта должно быть уникальным")
            
        project = Project(title, description, deadline)
        self.projects.append(project)
        print(f"Проект '{title}' создан.")

    def add_task_to_project(self, project_title: str, task: Task) -> None:
        for project in self.projects:
            if project.title == project_title:
                project.add_task(task)
                print(f"Задача добавлена в проект '{project_title}'.")
                return
        print(f"Проект '{project_title}' не найден.")

    def show_project_list(self) -> None:
        print("Список проектов в системе:")
        for project in self.projects:
            print(f"Проект: {project.title}")
            f_deadline = project.deadline.strftime("%Y-%m-%d")
            print(f"Дедлайн: {f_deadline}")

            project.show_task_list()

            print("----")
    
    def delete_project(self, project_title: str) -> None:
        for project in self.projects:
            if project.title == project_title:
                self.projects.remove(project)
                print(f"Проект '{project_title}' удален.")
                return
        print(f"Проект '{project_title}' не найден.")


# Пример использования
if __name__ == "__main__":
    project_management = ProjectManagement()

    # Создаем проекты
    project_management.create_project("Основной проект", "Разработка нового продукта", datetime(2023, 12, 31))
    project_management.create_project("Второй проект", "Еще один проект", datetime(2023, 12, 15))

    # Создаем задачу
    task = Task("Разработка функционала", "Написать код для нового функционала", datetime(2023, 12, 15))

    # Добавляем задачу в проект
    project_management.add_task_to_project("Основной проект", task)

    # Выводим список проектов
    project_management.show_project_list()
