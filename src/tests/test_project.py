import unittest
from datetime import datetime, timedelta, date
from app.task import Task
from app.project import Project

class TestProjectMethods(unittest.TestCase):

    def test_create_project(self):
        # Тест создания проекта с корректными параметрами
        project = Project("Test Project", "Test Description", datetime(2023, 12, 31).date())
        self.assertEqual(project.title, "Test Project")
        self.assertEqual(project.description, "Test Description")
        self.assertEqual(project.deadline, date(2023, 12, 31))
        self.assertEqual(project.tasks, [])

        # Тест создания проекта с некорректным deadline (должен быть datetime.date)
        with self.assertRaises(ValueError):
            Project("Invalid Deadline Project", "Test Description", datetime.now().date())

    def test_add_task(self):
        # Создаем проект
        project = Project("Test Project", "Test Description", datetime(2023, 12, 31).date())

        # Создаем задачи
        task_before = Task("Task Before", "Test Description", datetime(2023, 12, 15).date())
        task_after = Task("Task After", "Test Description", datetime(2024, 1, 1).date())
        task_same = Task("Task Same", "Test Description", datetime(2023, 12, 31).date())

        # Тест добавления задачи с дедлайном до дедлайна проекта
        project.add_task(task_before)
        self.assertIn(task_before, project.tasks)

        # Тест добавления задачи с дедлайном после дедлайна проекта
        with self.assertRaises(ValueError):
            project.add_task(task_after)

        # Тест добавления задачи с дедлайном равным дедлайну проекта
        project.add_task(task_same)
        self.assertIn(task_same, project.tasks)

if __name__ == '__main__':
    unittest.main()
