class Department:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

class Employee:
    def __init__(self, id: int, name: str, salary: float):
        self._id = id
        self._name = name
        self._salary = salary

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

class DepartmentEmployee:
    def __init__(self, department_id: int, employee_id: int):
        self._department_id = department_id
        self._employee_id = employee_id

    @property
    def department_id(self):
        return self._department_id

    @property
    def employee_id(self):
        return self._employee_id



def task1_modified(Departments, Employees, DepartmentEmployees):
    print("Запрос 1 ")
    data = [(d, [e for de in DepartmentEmployees for e in Employees if de.department_id == d.id and de.employee_id == e.id])
            for d in Departments if "отдел" in d.name.lower()]
    for department, employees in data:
        print(department.name)
        for employee in employees:
            print(f"  {employee.name}")

def task2_modified(Departments, Employees, DepartmentEmployees):
    print("Запрос 2 ")
    data = {}
    for department in Departments:
        employees = [e for de in DepartmentEmployees for e in Employees if de.department_id == department.id and de.employee_id == e.id]
        if employees:
            avg_salary = round(sum(e.salary for e in employees) / len(employees), 2)
            data[department.name] = avg_salary
    for department, avg_salary in sorted(data.items(), key=lambda x: x[1]):
        print(f"{department}: {avg_salary}")

def task3_modified(Departments, Employees, DepartmentEmployees):
    print("Запрос 3 ")
    data = [(e, [d for de in DepartmentEmployees for d in Departments if de.department_id == d.id and de.employee_id == e.id])
            for e in Employees if e.name.startswith("А")]
    for employee, departments in data:
        print(f"{employee.name}:")
        for department in departments:
            print(f"  {department.name}")

def main():
    # Создаем экземпляры классов для заполнения данными
    departments = [
        Department(1, "Отдел разработки"),
        Department(2, "Отдел маркетинга"),

    ]
    employees = [
        Employee(1, "Иванов Иван Иванович", 50000),
        Employee(2, "Петрова Мария Петровна", 60000),

    ]
    department_employees = [
        DepartmentEmployee(1, 1),  # Иванов в отделе разработки
        DepartmentEmployee(2, 2),  # Петрова в отделе маркетинга

    ]

    # Вызываем функции для выполнения задач
    task1_modified(departments, employees, department_employees)
    task2_modified(departments, employees, department_employees)
    task3_modified(departments, employees, department_employees)

if __name__ == "__main__":
    main()
