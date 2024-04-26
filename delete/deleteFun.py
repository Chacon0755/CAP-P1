def delete(employees, deletedEmployees, employeeToDelete):
    # for employee in employees:
    #     if employee['id'] == employeeToEdit:
    #         print(f"Deleting employee {employee['id']}, {employee['name']}")
    #         deletedEmployees.append(employee)
    #         employees.remove(employee)
    #         print(f"Employee deleted")
    print(f"Deleting employee {employees[employeeToDelete]['id']}, {employees[employeeToDelete]['name']}")
    deletedEmployees.append(employees[employeeToDelete])
    # print(deletedEmployees)
    # print(employeeToDelete)
    employees.pop(employeeToDelete)
    # print(employees)

    print("Employee deleted")
    return employees, deletedEmployees