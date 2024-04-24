def showListOfEmployees(employees):
    if len(employees) == 0:
        print("There are no employees registered")
        return
    for employee in employees:
        print(f"Employee id: {employee['id']}. Name: {employee['name']}.")
    print()