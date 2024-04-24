
def search(employees, employeeToSearch):
    for employee in employees:
        if employee['id'] == employeeToSearch:
            print(f"Name: {employee['name']}")
            print(f"Last Name: {employee['lastName']}")
            print(f"Email: {employee['email']}")
            print(f"{employee['seniority']} years seniority")