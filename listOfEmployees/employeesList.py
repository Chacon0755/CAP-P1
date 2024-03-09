def showListOfEmployees(employees):
    for  employee in employees:
        print(f"Employee: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Last name: {employee['lastName']}")
        print(f"Email: {employees['email']}")
        print(f"Password: {employees['password']}")
        print()