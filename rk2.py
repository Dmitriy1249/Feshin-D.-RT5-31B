import unittest
from rk1 import Department, Employee, DepartmentEmployee, task1_modified, task2_modified, \
    task3_modified  # Замените 'your_module' на имя вашего файла


class TestTasks(unittest.TestCase):

    def test_task1_filter_departments_with_employees(self):
        # Arrange (подготовка данных)
        departments = [
            Department(1, "Отдел разработки"),
            Department(2, "Отдел маркетинга"),
            Department(3, "Другой отдел")
        ]
        employees = [
            Employee(1, "Иванов Иван", 50000),
            Employee(2, "Петрова Мария", 60000),
            Employee(3, "Сидоров Антон", 70000)
        ]
        department_employees = [
            DepartmentEmployee(1, 1),
            DepartmentEmployee(1, 3),
            DepartmentEmployee(2, 2),
        ]
        # Act (вызов функции)
        result = task1_modified(departments, employees, department_employees)

        # Assert (проверки)
        self.assertIn("Отдел разработки", result)
        self.assertIn("Иванов Иван", result)
        self.assertIn("Сидоров Антон", result)
        self.assertNotIn("Отдел маркетинга", result)

    def test_task2_calculate_average_salaries(self):
        # Arrange
        departments = [
            Department(1, "Отдел разработки"),
            Department(2, "Отдел маркетинга")
        ]
        employees = [
            Employee(1, "Иванов Иван", 50000),
            Employee(2, "Петрова Мария", 60000),
            Employee(3, "Сидоров Антон", 70000)
        ]
        department_employees = [
            DepartmentEmployee(1, 1),
            DepartmentEmployee(1, 3),
            DepartmentEmployee(2, 2),
        ]
        # Act
        result = task2_modified(departments, employees, department_employees)

        # Assert
        self.assertIn("Отдел разработки: 60000.0", result)
        self.assertIn("Отдел маркетинга: 60000.0", result)

    def test_task3_find_departments_by_employee_name(self):
        # Arrange
        departments = [
            Department(1, "Отдел разработки"),
            Department(2, "Отдел маркетинга"),
            Department(3, "Другой отдел")
        ]
        employees = [
            Employee(1, "Анна Иванова", 50000),
            Employee(2, "Петрова Мария", 60000),
            Employee(3, "Александр Сидоров", 70000)
        ]
        department_employees = [
            DepartmentEmployee(1, 1),
            DepartmentEmployee(2, 1),
            DepartmentEmployee(3, 3),
        ]
        # Act
        result = task3_modified(departments, employees, department_employees)

        # Assert
        self.assertIn("Анна Иванова:", result)
        self.assertIn("Отдел разработки", result)
        self.assertIn("Отдел маркетинга", result)
        self.assertIn("Александр Сидоров:", result)
        self.assertIn("Другой отдел", result)


if __name__ == '__main__':
    unittest.main()