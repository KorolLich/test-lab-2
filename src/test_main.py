if __name__ == '__main__':
    import unittest
    from tests.test_task import TestTaskMethods
    from tests.test_project import TestProjectMethods
    from tests.test_project_management import TestProjectManagementMethods
    from tests.integration_tests import TestIntegrationMethods
    from tests.attestation_tests import TestMainMethods

    # Создаем тестовые наборы для обоих классов
    task_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskMethods)
    project_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestProjectMethods)
    project_management_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestProjectManagementMethods)
    integration_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestIntegrationMethods)
    attestation_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMainMethods)

    # Создаем общий тестовый набор
    all_test_suite = unittest.TestSuite([task_test_suite, 
                                         project_test_suite, 
                                         project_management_test_suite,
                                         integration_test_suite,
                                         attestation_test_suite])

    # Запускаем все тесты
    unittest.TextTestRunner().run(all_test_suite)