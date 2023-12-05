import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime, timedelta
if __name__ == '__main__':
    from app.project import Project
    from app.task import Task, StatusType
    from app.project_management import ProjectManagement
    import main  # Импортируем main.py для тестирования его функциональности
else:
    from .app.project import Project
    from .app.task import Task, StatusType
    from .app.project_management import ProjectManagement
    from . import main  # Импортируем main.py для тестирования его функциональности

class TestMainMethods(unittest.TestCase):
    """
    Аттестационное тестирование
    """
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

class TestTaskMethods(unittest.TestCase):
    """
    Модульное тестирование: класс Task
    """
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

class TestProjectMethods(unittest.TestCase):
    """
    Модульное тестирование: класс Project
    """
    def test_create_project(self):
        # Тест создания проекта с корректными параметрами
        project = Project("Test Project", "Test Description", (datetime.now() + timedelta(days=5)).date())
        self.assertEqual(project.title, "Test Project")
        self.assertEqual(project.description, "Test Description")
        self.assertEqual(project.deadline, (datetime.now() + timedelta(days=5)).date())
        self.assertEqual(project.tasks, [])

        # Тест создания проекта с некорректным deadline (должен быть datetime.date)
        with self.assertRaises(ValueError):
            Project("Invalid Deadline Project", "Test Description", datetime.now())

    def test_add_task(self):
        # Создаем проект
        project = Project("Test Project", "Test Description", (datetime.now() + timedelta(days=5)).date())

        # Создаем задачи
        task_before = Task("Task Before", "Test Description", (datetime.now() + timedelta(days=4)).date())
        task_after = Task("Task After", "Test Description", (datetime.now() + timedelta(days=6)).date())
        task_same = Task("Task Same", "Test Description", (datetime.now() + timedelta(days=5)).date())

        # Тест добавления задачи с дедлайном до дедлайна проекта
        project.add_task(task_before)
        self.assertIn(task_before, project.tasks)

        # Тест добавления задачи с дедлайном после дедлайна проекта
        with self.assertRaises(ValueError):
            project.add_task(task_after)

        # Тест добавления задачи с дедлайном равным дедлайну проекта
        project.add_task(task_same)
        self.assertIn(task_same, project.tasks)

    def test_get_info(self):
        # Создаем проект
        project = Project("Test Project", "Test Description", (datetime.now() + timedelta(days=5)).date())

        # Создаем задачи
        task1 = Task("Task 1", "Test Description", (datetime.now() + timedelta(days=1)).date())
        task2 = Task("Task 2", "Test Description", (datetime.now() + timedelta(days=3)).date())

        # Добавляем задачи в проект и проверяем их в get_info
        project.add_task(task1)
        result = project.get_info()
        self.assertIn(task1.get_info(), result)

        project.add_task(task2)
        result = project.get_info()
        self.assertIn(task1.get_info(), result)
        self.assertIn(task2.get_info(), result)
    
    def test_is_similar_tasks_true(self):
        project = Project("Project 1", "Description 1", (datetime.now() + timedelta(days=8)).date())
        task1 = Task("Task 1", "Description 1", (datetime.now() + timedelta(days=6)).date())
        project.add_task(task1)
        
        # Добавим задачу, которая похожа на существующую
        similar_task = Task("Task 1 New", "Description 1", (datetime.now() + timedelta(days=7)).date())
        self.assertTrue(project.is_similar_tasks(similar_task))

    def test_is_similar_tasks_false(self):
        project = Project("Project 2", "Description 2", (datetime.now() + timedelta(days=8)).date())
        task1 = Task("Task 1", "Description 2", (datetime.now() + timedelta(days=6)).date())
        project.add_task(task1)
        
        # Добавим задачу, которая не похожа на существующую
        dissimilar_task = Task("New 3", "Description 3", (datetime.now() + timedelta(days=7)).date())
        self.assertFalse(project.is_similar_tasks(dissimilar_task))

    def test_new_task_full_in_another_task(self):
        project = Project("Project 2", "Description 2", (datetime.now() + timedelta(days=8)).date())
        task1 = Task("Очень длинное название, много лишних слов не требуется чтобы описать всю боль",
                      "Description 2", (datetime.now() + timedelta(days=6)).date())
        project.add_task(task1)
        
        # Добавим задачу, название которой полностью копирует существующую
        similar_task = Task("Очень", "Description 3", (datetime.now() + timedelta(days=7)).date())
        self.assertTrue(project.is_similar_tasks(similar_task))

    def test_another_task_full_in_new_task(self):
        project = Project("Project 2", "Description 2", (datetime.now() + timedelta(days=8)).date())
        task1 = Task("угабуга", "Description 2", (datetime.now() + timedelta(days=6)).date())
        project.add_task(task1)
        
        # Добавим задачу
        similar_task = Task("Слшком много букав, ыыы, дааа, ееее, угабуга", "Description 3", (datetime.now() + timedelta(days=7)).date())
        self.assertTrue(project.is_similar_tasks(similar_task))

    def test_strange_symbols_similarity(self):
        project = Project("Project 2", "Description 2", (datetime.now() + timedelta(days=8)).date())
        task1 = Task("^*^%&^%*слово*&$*^*^$*)(*)__0--", "Description 2", (datetime.now() + timedelta(days=6)).date())
        project.add_task(task1)
        
        # Добавим задачу
        similar_task = Task("слово", "Description 3", (datetime.now() + timedelta(days=7)).date())
        self.assertTrue(project.is_similar_tasks(similar_task))

    def test_add_task_similar_task_not_added(self):
        project = Project("Project 3", "Description 3", (datetime.now() + timedelta(days=7)).date())
        task1 = Task("Task 1", "Description 3", (datetime.now() + timedelta(days=5)).date())
        project.add_task(task1)
        
        # Добавим похожую задачу, она не должна быть добавлена
        similar_task = Task("Task 1 New", "Description 3", (datetime.now() + timedelta(days=4)).date())
        project.add_task(similar_task)
        
        self.assertEqual(len(project.tasks), 1)

    def test_add_task_dissimilar_task_added(self):
        project = Project("Project 4", "Description 4", (datetime.now() + timedelta(days=8)).date())
        task1 = Task("Task 1", "Description 4", (datetime.now() + timedelta(days=6)).date())
        project.add_task(task1)
        
        # Добавим не похожую задачу, она должна быть добавлена
        dissimilar_task = Task("New 3", "Description 4", (datetime.now() + timedelta(days=7)).date())
        project.add_task(dissimilar_task)
        
        self.assertEqual(len(project.tasks), 2)

class TestProjectManagementMethods(unittest.TestCase):
    """
    Модульное тестирование: класс ProjectManagement
    """
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

class TestIntegrationMethods(unittest.TestCase):
    """
    Интеграционное тестирование
    """
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

if __name__ == "__main__":
    unittest.main()
