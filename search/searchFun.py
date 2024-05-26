
def search(employees, employeeToSearch):
    # for employee in employees:
    #     if employee['id'] == employeeToSearch:
    #         print(f"Name: {employee['name']}")
    #         print(f"Last Name: {employee['lastName']}")
    #         print(f"Email: {employee['email']}")
    #         print(f"{employee['seniority']} years seniority")
    try:
        print(f"Name: {employees[employeeToSearch]['name']}")
        print(f"Last Name: {employees[employeeToSearch]['lastName']}")
        print(f"Email: {employees[employeeToSearch]['email']}")
        print(f"{employees[employeeToSearch]['seniority']} years seniority")
        
    except EOFError:
        print(colored(" ╔══════════════════════════╗ ","red"))
        print(colored(" ║     Error: Void list     ║  ","red"))
        print(colored(" ╚══════════════════════════╝ ","red"))