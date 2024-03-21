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

employees = []
deletedEmployees = []
verification = True

def main():
    option = 0
    print(colored("Welcome to MMAS", "blue"))
    while option !=6:
        print(colored("MENU\n1. Add Employee \n2. Edit Employee name and password \n3. Search Employee \n4. Delete Employee \n5. List of employees \n6. Exit", "green"))
        option = int(input("Enter your favorite option: "))
        print("------------------------------------------------------------")
        match option:
            case 1:
                print(colored("Add Employee","blue"))
                add()
            case 2:
                print(colored("Edit Employee name", "blue"))
                employeesList.showListOfEmployees(employees)
                editFun.edit(employees)
            case 3:
                print(colored("Search Employee", "blue"))
                employeesList.showListOfEmployees(employees)
                searchFun.search(employees)
            case 4:
                print(colored("Delete Employee", "blue"))
                employeesList.showListOfEmployees(employees)
                deleteFun.delete(employees, deletedEmployees)
            case 5:
                employeesList.showListOfEmployees(employees)
            case 6:
                print(colored("Have a nice day!.", "magenta"))
                break
                
    
def add():
    name = input(colored("Enter your name: ", "cyan"))
    lastName = input(colored("Enter your last name: ", "cyan"))
    id  = random.randint(1000,9999)
    email = emailGenerator.generateEmail(name, lastName)
    password = input(colored("Enter your password of at least 8 characters: ", "cyan"))
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
        'password' : password
        }
    employees.append(employee)
    print(colored("Employee succesfully added", "green"))
    print("------------------------------------------------------------")
    




if __name__=="__main__":main()

