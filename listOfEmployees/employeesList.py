def showListOfEmployees(employees):
    for employee in employees:
        print(f"Employee id: {employee['id']}. Name: {employee['name']}.")
    print()