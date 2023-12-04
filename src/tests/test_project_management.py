import unittest
from datetime import datetime, timedelta, date
from app.task import Task
from app.project import Project
from app.project_management import ProjectManagement

class TestProjectManagementMethods(unittest.TestCase):

    def test_add_project(self):
        project_management = ProjectManagement()

        # Тест добавления проекта с корректными параметрами
        project = Project("Test Project", "Test Description", (datetime.now() + timedelta(days=5)).date())
        project_management.add_project(project)
        self.assertEqual(len(project_management.projects), 1)
        self.assertEqual(project_management.projects[0].title, "Test Project")

        # Тест добавления проекта с некорректным названием (дублирование)
        with self.assertRaises(ValueError):
            project_management.add_project(Project("Test Project", "Duplicate Description", (datetime.now() + timedelta(days=4)).date()))
        
        self.assertEqual(len(project_management.projects), 1)  # Новый проект не должен быть добавлен из-за ошибки

    def test_add_task_to_project(self):
        project_management = ProjectManagement()

        # Создаем проект
        project_management.add_project(Project("Test Project", "Test Description", (datetime.now() + timedelta(days=5)).date()))

        # Создаем задачу
        task = Task("Test Task", "Task Description", (datetime.now() + timedelta(days=3)).date())

        # Тест добавления задачи в проект
        project_management.add_task_to_project("Test Project", task)
        self.assertEqual(len(project_management.projects[0].tasks), 1)
        self.assertEqual(project_management.projects[0].tasks[0].title, "Test Task")

        # Тест добавления задачи в несуществующий проект
        with self.assertRaises(ValueError):
            project_management.add_task_to_project("Nonexistent Project", task)
        
        self.assertEqual(len(project_management.projects[0].tasks), 1)  # Задача не должна быть добавлена из-за ошибки

    def test_get_info(self):
        project_management = ProjectManagement()

        # Создаем проекты
        project_management.add_project(Project("Project 1", "Description 1", (datetime.now() + timedelta(days=7)).date()))
        project_management.add_project(Project("Project 2", "Description 2", (datetime.now() + timedelta(days=5)).date()))

        # Создаем задачи
        task1 = Task("Task 1", "Task Description 1", (datetime.now() + timedelta(days=2)).date())
        task2 = Task("Task 2", "Task Description 2", (datetime.now() + timedelta(days=4)).date())

        # Добавляем задачи в проекты
        project_management.add_task_to_project("Project 1", task1)
        project_management.add_task_to_project("Project 2", task2)

        # Проверяем, что все задачи действительно в этих проектах
        cnt_task = 0
        for project in project_management.projects:
            if project.title == "Project 1":
                cnt_task += 1
                self.assertIn(task1, project.tasks)
            elif project.title == "Project 2":
                self.assertIn(task2, project.tasks)
                cnt_task += 1
        self.assertEqual(cnt_task, 2)

        # Проверяем, что строки с информацией о проектах и задачах присутствуют в выводе
        result = project_management.get_info()
        self.assertIn("Проект: Project 1", result)
        self.assertIn("Дедлайн: ", result)
        self.assertIn(task1.get_info(), result)

        self.assertIn("Проект: Project 2", result)
        self.assertIn("Дедлайн: ", result)
        self.assertIn(task2.get_info(), result)

    def test_delete_project(self):
        project_management = ProjectManagement()

        # Создаем проект
        project_management.add_project(Project("Test Project", "Test Description", (datetime.now() + timedelta(days=5)).date()))

        # Тест удаления существующего проекта
        project_management.delete_project("Test Project")
        self.assertEqual(len(project_management.projects), 0)

        # Тест удаления несуществующего проекта
        with self.assertRaises(ValueError):
            project_management.delete_project("Nonexistent Project")

if __name__ == '__main__':
    unittest.main()
