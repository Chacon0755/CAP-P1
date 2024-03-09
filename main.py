employees = {}

def main():
    print("Welcome to MMAS")
    print("MENU\n1. Add Employee \n2.Edit Employee \n3.Search Employee \n4. Delete Employee")
    option = int(input("Enter your favorite option"))
    match option:
        case 1:
            print("Add Employee")
        case 2:
            print("Edit Employee")
        case 3:
            print("Search Employee")
        case 4:
            print("Delete Employee")
    
    




if __name__=="__main__":main()
