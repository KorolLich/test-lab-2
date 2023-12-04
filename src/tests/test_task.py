import unittest
from datetime import datetime, timedelta
import time

# import sys
# sys.path.append('../')
# import app
from app.task import Task, StatusType

class TestTaskMethods(unittest.TestCase):

    def test_create_task(self):
        title = "Test Task"
        description = "Test Description"
        deadline = (datetime.now() + timedelta(days=7)).date()

        task = Task(title, description, deadline)

        self.assertEqual(task.title, title)
        self.assertEqual(task.description, description)
        self.assertEqual(task.deadline, deadline)
        self.assertEqual(task.status, StatusType.NEW_TASK)

    def test_try_using_datetime_instead_date(self):
        deadline = datetime.now() + timedelta(days=7)

        with self.assertRaises(ValueError):
            task = Task('Datetime вместо datetime.date ', 'description', deadline)

    def test_change_status(self):
        task = Task("Test Task", "Test Description", (datetime.now() + timedelta(days=7)).date())

        self.assertTrue(task.change_status(StatusType.IN_PROGRESS))
        self.assertEqual(task.status, StatusType.IN_PROGRESS)

        # Попытка присвоить статус "Новая"
        self.assertFalse(task.change_status(StatusType.NEW_TASK))
        self.assertEqual(task.status, StatusType.IN_PROGRESS)  # Статус не должен измениться

    def test_invalid_deadline_task(self):
        deadline = (datetime.now() - timedelta(days=1)).date()

        with self.assertRaises(ValueError):
            task = Task("Expired Task", "Test Description", deadline)
        
        with self.assertRaises(ValueError):
            task = Task("Expired Task", "Test Description", datetime.now().date())

    def test_get_1_days_before_deadline(self):
        deadline = (datetime.now() + timedelta(days=1)).date()
        task = Task("Test Task", "Test Description", deadline)

        days_before_deadline = task.get_days_before_deadline()

        self.assertEqual(days_before_deadline, 1)

    def test_get_info(self):
        task = Task("Test Task", "Test Description", (datetime.now() + timedelta(days=7)).date())

        info = task.get_info()

        self.assertIn("Название задачи: Test Task", info)
        self.assertIn("Описание: Test Description", info)
        self.assertIn("Статус: Новая задача", info)

if __name__ == '__main__':
    unittest.main()
