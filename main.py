import random
import emailGenerator
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

def main():
    option = 0
    print("Welcome to MMAS")
    while option !=6:
        print("MENU\n1. Add Employee \n2. Edit Employee name and password \n3. Search Employee \n4. Delete Employee \n5. List of employees \n6. Exit")
        option = int(input("Enter your favorite option: "))
        print("------------------------------------------------------------")
        match option:
            case 1:
                print("Add Employee")
                add()
            case 2:
                print("Edit Employee name")
                employeesList.showListOfEmployees(employees)
                editFun.edit(employees)
            case 3:
                print("Search Employee")
                employeesList.showListOfEmployees(employees)
                searchFun.search(employees)
            case 4:
                print("Delete Employee")
                employeesList.showListOfEmployees(employees)
                deleteFun.delete(employees, deletedEmployees)
            case 5:
                employeesList.showListOfEmployees(employees)
            case 6:
                print("Have a nice day!.")
                break
                
    
def add():
    name = input("Enter your name: ")
    lastName = input("Enter your last name: ")
    id  = random.randint(1000,9999)
    email = emailGenerator.generateEmail(name, lastName)
    password = input("Enter your password: ")
    employee = {
        'id': id,
        'name' : name,
        'lastName': lastName,
        'email': email,
        'password' : password
        }
    employees.append(employee)
    print("Employee succesfully added")
    print("------------------------------------------------------------")
    




if __name__=="__main__":main()
