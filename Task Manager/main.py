import datetime
import os

def user_info(username, password):
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    age = input("Enter your age : ")

    filename = f"{username}_task.txt"

    try:
        with open(filename, 'a') as f:
            f.write(f"Password: {password}\n")
            f.write(f"Name: {name}\n")
            f.write(f"Address: {address}\n")
            f.write(f"Age: {age}\n")
        print("Informations saved.")
    except Exception as e:
        print(f"Error: {e}")

def sign_up():
    user = input("Enter username : ")
    pas = input("Enter password : ")
    user_info(user, pas)
    print("You can login now.")
    log_in()

def log_in():
    user_log = input("Username : ")
    pas_log = input("Password : ")
    user_file = f"{user_log}_task.txt"

    if os.path.exists(user_file):
        try:
            userlog = f"{user_log}_task.txt"
            with open(userlog, 'r') as f_:
                k = f_.readlines()
                if k and pas_log == k[0].strip().split(":")[1].strip():
                    print("Logging in...")
                    
                    while True:
                        print(
                        "1--View user information\n2--Add task\n3--Update task\n4--Quit")
                        tsk = input("Choose : ")
                        if tsk == '1':
                            show_data(userlog)
    
                        elif tsk == '2':
                            task_info(userlog)
    
                        elif tsk == '3':
                            task_update(user_log)
    
                        elif tsk == '4':
                            print("Exiting...")
                            exit()
                            
                        else:
                            print("Try again.")
    
                        print("-"*50)
                else:
                    print("Username or password is incorrect.")
                    log_in()
        except Exception as e:
            print(e)
    else:
        print("Username not found. Try again.")
        log_in()

def show_data(user):
    print("-"*50)
    with open(user, 'r') as fl:
        print(fl.read())

def task_info(user):
    print("-"*50)
    x = int(input("How many tasks would you like to add? : "))
    with open(user, 'a') as fk:
        for i in range(1, x + 1):
            task = input(f"Task {i} : ")
            time = input(f"Time {i} : ")
            t = f"TASK : {task} --> {time}\n"
            fk.write(t)

        
def task_update(user):
    print("-"*50)
    user_file = f"{user}_task.txt"
    task_ok = input("Enter complated task : ")
    task_not_ok = input("Enter the task that has not yet been started : ")

    with open(user_file, 'a') as fz:
        DT = str(datetime.datetime.now())
        fz.write(DT)
        fz.write("\n")
        fz.write("COMPLETED TASK \n")
        fz.write(task_ok)
        fz.write("\n")
        fz.write("NOT YET STARTED\n")
        fz.write(task_not_ok)
        fz.write("\n")

print("TASK MANAGER")

while True:
    a = input("Sign up -> 1\nSign in -> 0\nEnter : ")
    if a == '1':
        sign_up()
    elif a == '0':
        log_in()
    else:
        print("Invalid login!")
