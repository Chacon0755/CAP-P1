import random
import emailGenerator
from termcolor import colored
import sys
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

def main():
    option = 0
    print(colored("Welcome to MMAS", "blue"))
    while option !=6:
        print(colored("MENU\n1. Add Employee \n2. Edit Employee name and password \n3. Search Employee \n4. Delete Employee \n5. List of employees \n6. Exit", "green"))
        optionStr = input("Enter your favorite option: ")
        if optionStr.isdigit():
            option = int(optionStr)
            if  1 <= option <= 6:
                print("------------------------------------------------------------")
                match option:
                    case 1:
                        print(colored("Add Employee","blue"))
                        add()
                    case 2:
                        print(colored("Edit Employee name", "blue"))
                        employeesList.showListOfEmployees(employees)
                        employeeToEdit = validateFun.validateEmployee(employees)
                        editFun.edit(employees, employeeToEdit)
                    case 3:
                        print(colored("Search Employee", "blue"))
                        employeesList.showListOfEmployees(employees)
                        employeeToSearch = validateFun.validateEmployee(employees)
                        searchFun.search(employees, employeeToSearch)
                    case 4:
                        print(colored("Delete Employee", "blue"))
                        employeesList.showListOfEmployees(employees)
                        employeeToDelete = validateFun.validateEmployee(employees)
                        deleteFun.delete(employees, deletedEmployees, employeeToDelete)
                    case 5:
                        employeesList.showListOfEmployees(employees)
                    case 6:
                        print(colored("Have a nice day!.", "magenta"))
                        break
            else:
                print(colored("The option inputed must be between 1 and 6", "red"))
        else:
            print(colored("The input must be numeric ", "red"))
            
                

def add():
    name = input(colored("Enter your name: ", "cyan"))
    lastName = input(colored("Enter your last name: ", "cyan"))
    id  = random.randint(1000,9999)
    email = emailGenerator.generateEmail(name, lastName)
    password = input(colored("Enter your password of at least 8 characters: ", "cyan"))
    seniority = random.randint(1,49)
    while True:
        if len(password) >= 8:
            break
        print(colored("The password must contain at least 8 characters", "red"))
        password = input(colored("Enter your password: ", "cyan"))
    employee = {
        'id': id,
        'name' : name,
        'lastName': lastName,
        'email': email,
        'password' : password,
        'seniority' : seniority
        }
    employees.append(employee)
    print(colored("Employee succesfully added", "green"))
    print("------------------------------------------------------------")
    




if __name__=="__main__":main()

