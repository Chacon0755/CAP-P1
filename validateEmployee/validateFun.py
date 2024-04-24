def validateEmployee(employees):
    if len(employees) == 0:
        return 
    while True:
        employeeStr = input("Enter the employee ID: ")
        if employeeStr.isdigit():
            employeeInputed = int(employeeStr)
            for employee in employees:
                if employee['id'] == employeeInputed:
                    return employeeInputed
        else:
            print("The input must be numeric")
            continue
        print("Enter a valid ID")
        