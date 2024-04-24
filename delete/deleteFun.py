def delete(employees, deletedEmployees, employeeToEdit):
    for employee in employees:
        if employee['id'] == employeeToEdit:
            print(f"Deleting employee {employee['id']}, {employee['name']}")
            deletedEmployees.append(employee)
            employees.remove(employee)
            print(f"Employee deleted")
    return employees, deletedEmployees