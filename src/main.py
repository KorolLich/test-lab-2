if __name__ == '__main__':
    import unittest
    from tests.test_task import TestTaskMethods
    from tests.test_project import TestProjectMethods
    
    # Создаем тестовые наборы для обоих классов
    task_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskMethods)
    project_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestProjectMethods)

    # Создаем общий тестовый набор
    all_test_suite = unittest.TestSuite([task_test_suite, project_test_suite])

    # Запускаем все тесты
    unittest.TextTestRunner().run(all_test_suite)