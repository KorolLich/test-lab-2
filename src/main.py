if __name__ == '__main__':
    import unittest
    from tests.test_task import TestTaskMethods

    # Создаем тестовый набор
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskMethods)

    # Запускаем тесты
    unittest.TextTestRunner().run(test_suite)