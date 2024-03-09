import random
import string
def edit(employees):
    employeeToEdit = int(input("Enter the employee id of the employee that you want to edit: "))
    find = False
    for employee in employees:
        if employee['id'] == employeeToEdit:
            newName = input("Enter the new name: ")
            employee['name'] = newName
            employee['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(8))
            find  = True
            print(f"New Password: {employee['password']}")
            print("Name and password succesfully updated")
            break
        if not find:
            print("Employee not found")
    return employees

