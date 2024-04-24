import random
import string
def edit(employees, employeeToEdit):
    for employee in employees:
        if employee['id'] == employeeToEdit:
            newName = input("Enter the new name: ")
            newLastName = input("Enter the new last name: ")
            employee['name'] = newName
            employee['lastName'] = newLastName
            employee['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(8))
            find  = True
            print(f"New Password: {employee['password']}")
            print("Name and password succesfully updated")
    return employees

