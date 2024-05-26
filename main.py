import random
import emailGenerator
from colorama import init
init()
from termcolor import colored
import sys
import threading
sys.path.append("CAP-P1\\delete")
from delete import deleteFun
sys.path.append("CAP-P1\\edit")
from edit import editFun
sys.path.append("CAP-P1\\search")
from search import searchFun
sys.path.append("CAP-P1\\listOfEmployees")
from listOfEmployees import employeesList
sys.path.append("CAP-P1\\validateEmployee")
from validateEmployee import validateFun

employees = []
deletedEmployees = []
verification = True

def assign_id(employee):
    employee['id'] = random.randint(1000, 9999)

def generate_email(employee):
    employee['email'] = emailGenerator.generateEmail(employee['name'], employee['lastName'])

def assign_seniority(employee):
    employee['seniority'] = random.randint(1, 49)

def main():
    option = 0
    print(colored("Welcome to MMAS", "blue"))
    while option != 6:
        print(colored("MENU\n1. Add Employee \n2. Edit Employee name and password \n3. Search Employee \n4. Delete Employee \n5. List of employees \n6. Exit", "green"))
        optionStr = input("Enter your favorite option: ")
        if optionStr.isdigit():
            option = int(optionStr)
            if 1 <= option <= 6:
                print("------------------------------------------------------------")
                match option:
                    case 1:
                        print(colored("Add Employee", "blue"))
                        add()
                    case 2:
                        print(colored("Edit Employee name", "blue"))
                        if employees:
                            employeesList.showListOfEmployees(employees)
                            employeeToEdit = validateFun.validateEmployee(employees)
                            if employeeToEdit is not None:
                                editFun.edit(employees, employeeToEdit)
                        else:
                            print(colored("The employee list is empty.", "red"))
                    case 3:
                        print(colored("Search Employee", "blue"))
                        if employees:
                            employeesList.showListOfEmployees(employees)
                            employeeToSearch = validateFun.validateEmployee(employees)
                            if employeeToSearch is not None:
                                searchFun.search(employees, employeeToSearch)
                        else:
                            print(colored("The employee list is empty.", "red"))
                    case 4:
                        print(colored("Delete Employee", "blue"))
                        if employees:
                            employeesList.showListOfEmployees(employees)
                            employeeToDelete = validateFun.validateEmployee(employees)
                            if employeeToDelete is not None:
                                deleteFun.delete(employees, deletedEmployees, employeeToDelete)
                        else:
                            print(colored("The employee list is empty.", "red"))
                    case 5:
                        if employees:
                            employeesList.showListOfEmployees(employees)
                        else:
                            print(colored("The employee list is empty.", "red"))
                    case 6:
                        print(colored("Have a nice day!.", "magenta"))
                        break
            else:
                print(colored("The option inputted must be between 1 and 6", "red"))
        else:
            print(colored("The input must be numeric", "red"))

def add():
    nameImputed = input(colored("Enter your name: ", "cyan"))
    while True:
        if len(nameImputed) > 0 and not nameImputed.isdigit():
            name = nameImputed
            break
        print(colored("Enter a valid name", "red"))
        nameImputed = input(colored("Enter your name: ", "cyan"))

    lastNameInputed = input(colored("Enter your last name: ", "cyan"))
    while True:
        if len(lastNameInputed) > 0 and not lastNameInputed.isdigit():
            lastName = lastNameInputed
            break
        print(colored("Enter a valid lastName", "red"))
        lastNameInputed = input(colored("Enter your last name: ", "cyan"))

    password = input(colored("Enter your password of at least 8 characters: ", "cyan"))
    while True:
        if len(password) >= 8:
            break
        print(colored("The password must contain at least 8 characters", "red"))
        password = input(colored("Enter your password: ", "cyan"))

    employee = {
        'name': name,
        'lastName': lastName,
        'password': password
    }

    # Create threads for ID, email, and seniority
    threads = []
    threads.append(threading.Thread(target=assign_id, args=(employee,)))
    threads.append(threading.Thread(target=generate_email, args=(employee,)))
    threads.append(threading.Thread(target=assign_seniority, args=(employee,)))

    # Start all threads
    for thread in threads:
        thread.start()

    # Ensure all threads have finished
    for thread in threads:
        thread.join()

    employees.append(employee)
    print(colored("Employee successfully added", "green"))
    print("------------------------------------------------------------")

def validateEmployee(employees):
    while True:
        employeeStr = input("Enter the employee ID: ")
        if employeeStr.isdigit():
            employeeInputed = int(employeeStr)
            for employeeIndex, employee in enumerate(employees):
                if employee['id'] == employeeInputed:
                    return employeeIndex
        else:
            print("The input must be numeric")
        print("Enter a valid ID")

if __name__ == "__main__":
    main()