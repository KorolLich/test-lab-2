import unittest
from datetime import datetime, timedelta
from app.task import Task, StatusType
from app.project import Project
from app.project_management import ProjectManagement

class TestIntegrationMethods(unittest.TestCase):

    def test_create_project_add_task_show_info(self):
        project_management = ProjectManagement()

        # Создаем задачу
        task = Task("Integration Task", "Task Description", (datetime.now() + timedelta(days=8)).date())
        
        # Изменяем статус задачи
        task.change_status(StatusType.IN_PROGRESS)

        # Создаем проект и добавляем в него задачу
        project = Project("Integration Project", "Integration Description", (datetime.now() + timedelta(days=10)).date())
        project.add_task(task)
        
        # Проверка, что информация о проекте и задаче присутствует в выводе
        result = project.get_info()
        self.assertIn("Integration Project", result)
        self.assertIn("Integration Task", result)
        self.assertIn("Статус: " + StatusType.IN_PROGRESS.value, result)
        self.assertEqual(len(project.tasks), 1)

        # Изменяем снова статус задачи
        task.change_status(StatusType.COMPLETE_TASK)

        # Добавляем проект в ProjectManagement
        project_management.add_project(project)

        # Проверяем, что project_management.projects не пустой
        self.assertEqual(len(project_management.projects), 1)

        # Проверяем, что вновь измененный статус задачи присутствует в project_management.get_info()
        result_management = project_management.get_info()
        self.assertIn("Проект: Integration Project", result_management)
        self.assertIn("Дедлайн: ", result_management)
        self.assertIn("Integration Task", result_management)
        self.assertIn("Статус: " + StatusType.COMPLETE_TASK.value, result_management)

    def test_delete_project_with_tasks(self):
        project_management = ProjectManagement()

        # Создаем проект и добавляем в него задачи
        project = Project("Delete Project", "Delete Description", (datetime.now() + timedelta(days=15)).date())
        task1 = Task("Task 1", "Task Description 1", (datetime.now() + timedelta(days=10)).date())
        task2 = Task("Task 2", "Task Description 2", (datetime.now() + timedelta(days=12)).date())
        project.add_task(task1)
        project.add_task(task2)

        # Удаляем проект с задачами
        project_management.add_project(project)
        project_management.delete_project("Delete Project")

        # Проверяем, что проект удален и не присутствует в списке проектов в ProjectManagement
        self.assertEqual(len(project_management.projects), 0)
