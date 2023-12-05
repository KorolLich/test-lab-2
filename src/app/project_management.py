from .project import Project
from datetime import datetime
from .task import Task

class ProjectManagement:
    def __init__(self) -> None:
        self.projects = []  # Список проектов в системе

    def add_project(self, project: Project) -> None:
        for existing_project in self.projects:
            if existing_project.title == project.title:
                raise ValueError("Название проекта должно быть уникальным")
        
        self.projects.append(project)
        print(f"Проект '{project.title}' добавлен.")

    def add_task_to_project(self, project_title: str, task: Task) -> None:
        for project in self.projects:
            if project.title == project_title:
                project.add_task(task)
                print(f"Задача добавлена в проект '{project_title}'.")
                return
        raise ValueError(f"Проекта с названием {project_title} не существует")

    def get_info(self) -> str:
        result = "Список проектов в системе:\n"
        for project in self.projects:
            result += f"Проект: {project.title}\n"
            result += f"Дедлайн: {project.deadline}\n"
            result += project.get_info() + "\n-------------------------\n"
        return result

    
    def delete_project(self, project_title: str) -> None:
        for project in self.projects:
            if project.title == project_title:
                self.projects.remove(project)
                print(f"Проект '{project_title}' удален.")
                return
        raise ValueError(f"Проекта с названием {project_title} не существует")
