import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime, timedelta
from app.project import Project
from app.task import Task, StatusType
from app.project_management import ProjectManagement
import main  # Импортируем main.py для тестирования его функциональности

class TestMainMethods(unittest.TestCase):
    def setUp(self):
        self.project_management = ProjectManagement()

    def tearDown(self):
        self.project_management = None

    @patch("builtins.input", side_effect=["Test Project", "Test Description", "2023-12-31"])
    def test_create_project(self, mock_input):
        main.create_project(self.project_management)
        self.assertEqual(len(self.project_management.projects), 1)

    @patch("builtins.input", side_effect=["Test Project", "Test Description", "2023-12-31"] * 2)
    def test_create_duplicate_project(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.create_project(self.project_management)
            main.create_project(self.project_management)
        self.assertIn("Ошибка", mock_stdout.getvalue().strip())

    @patch("builtins.input", side_effect=["Test Project", "Test Description", "2023-12-31"])
    def test_add_task_to_project(self, mock_input):
        main.create_project(self.project_management)
        with patch("builtins.input", side_effect=["Test Project", "Test Task", "Task Description", "2023-12-15"]):
            main.add_task_to_project(self.project_management)
        self.assertEqual(len(self.project_management.projects[0].tasks), 1)

    @patch("builtins.input", side_effect=["Test Project", "Test Task", "Task Description", "2023-12-15"])
    def test_add_task_to_nonexistent_project(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.add_task_to_project(self.project_management)
        self.assertIn("Ошибка", mock_stdout.getvalue().strip())

    @patch("builtins.input", side_effect=["Test Project", "Test Description", "2023-12-31"])
    def test_delete_project(self, mock_input):
        main.create_project(self.project_management)
        with patch("builtins.input", side_effect=["Test Project"]):
            main.delete_project(self.project_management)
        self.assertEqual(len(self.project_management.projects), 0)

    @patch("builtins.input", side_effect=["Test Project"])
    def test_delete_nonexistent_project(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.delete_project(self.project_management)
        self.assertIn("Ошибка", mock_stdout.getvalue().strip())

    @patch("builtins.input", side_effect=["ы", "уга-бугу", "5"])
    def test_invalid_choice(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.main()
            self.assertIn("Неверный выбор. Попробуйте снова.", mock_stdout.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
