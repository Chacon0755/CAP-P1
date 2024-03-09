def delete(employees, deletedEmployees):
    employeeToEdit = int(input("Enter the employee id of the employee that you want to delete: "))
    find = False
    for employee in employees:
        if employee['id'] == employeeToEdit:
            print(f"Deleting employee {employee['id']}, {employee['name']}")
            deletedEmployees.append(employee)
            employees.remove(employee)
            find = True
            print(f"Employee deleted")
        if not find:
            print("Employee not found")
    return employees, deletedEmployees