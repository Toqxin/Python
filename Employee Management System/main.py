import pyodbc
import time

server = 'server-name'
database = 'database-name'

connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()


def show_employee():
    cursor.execute("SELECT * FROM yourtable")
    rows = cursor.fetchall()

    print("Id      Name                            Surname                         Job                                                     Salary")
    print("-"*140)
    for row in rows:
        print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}')


print("[EMPLOYEE TABLE]-->")
show_employee()


def add_employee():
    empId = input("Enter employee Id : ")
    cursor.execute("SELECT Id FROM yourtable WHERE Id=?", (empId,))
    existing_employee = cursor.fetchone()

    if existing_employee:
        print("Employee with the same Id already exists. Cannot add.")

    else:
        empName = input("Enter employee name : ")
        empSurname = input("Enter employee surname : ")
        empJob = input("Enter employee job : ")
        empSalary = input("Enter employee salary : ")
        cursor.execute("INSERT INTO yourtable (Id,Name,Surname,Job,Salary)VALUES(?,?,?,?,?)",
                       (empId, empName, empSurname, empJob, empSalary))
        connection.commit()
        print("Adding...")
        time.sleep(2)
        print("Employee added successfully.")


def update_employee():
    try:
        empId = input("The identity of the employee to be updated : ")
        empName = input("New enter employee name : ")
        empSurname = input("New enter employee surname : ")
        empJob = input("New enter employee job : ")
        empSalary = input("New enter employee salary : ")
        cursor.execute("UPDATE yourtable SET Id=?, Name=?, Surname=?, Job=?, Salary=? WHERE Id=?",
                       (empId, empName, empSurname, empJob, empSalary, empId))
        connection.commit()
        print("Updating...")
        time.sleep(2)
        print("Employee updated successfully.")

    except Exception as e:
        print(f"An error occurred : {str(e)}")


def delete_employee():
    empId = input("Enter the employee id to be deleted : ")
    cursor.execute("DELETE FROM yourtable WHERE Id=?", (empId))
    connection.commit()
    print("Deleting...")
    time.sleep(2)
    print("Employee deleted successfully.")


while True:
    print("-"*140)
    print("1 : Show Employee\n2 : Add Employee\n3 : Update Employee\n4 : Delete Employee\n5 : Quit -> q")
    process = input("Please select a process : ")

    if process == 'q':
        print("Exiting...")
        time.sleep(2)
        break

    elif process == '1':
        print("Showing employees...")
        time.sleep(2)
        print("[EMPLOYEE TABLE]-->")
        show_employee()

    elif process == '2':
        print("Loading...")
        time.sleep(2)
        add_employee()

    elif process == '3':
        print("Loading...")
        time.sleep(2)
        update_employee()

    elif process == '4':
        print("Loading...")
        time.sleep(2)
        delete_employee()

    else:
        print("There was an error please try again.")

connection.close()
