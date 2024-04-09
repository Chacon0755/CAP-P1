import random
def search(employees):
    employeeToSearch = int(input("Enter the employee id of the employee that you want to view: "))
    find = False
    for employee in employees:
        if employee['id'] == employeeToSearch:
            print(f"Name: {employee['name']}")
            print(f"Last Name: {employee['lastName']}")
            print(f"Email: {employee['email']}")
            print(f"{employee['seniority']} years seniority")