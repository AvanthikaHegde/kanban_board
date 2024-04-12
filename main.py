import sqlite3
connection = sqlite3.connect("kanbanBoard.db")#creating and estb a connecting object.
cursor =connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS kanban(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
               "Kanban_id INTEGER,Task_Name TEXT,Status TEXT,User TEXT,Priority TEXT)")

#cursor.execute("DELETE FROM kanban")
#connection.commit()
#FUNCTION TO ADD THE TASK
def add_Task():
    kid = int(input("Enter the Kanban Id"))
    task_name = input("Enter the Task name")
    status="TODO"
    user=""
    priority=input("Enter the Task priority")

    cursor.execute("INSERT INTO kanban(Kanban_id,Task_Name,Status,User,Priority) "
                   "VALUES (?,?,?,?,?)", (kid, task_name, status, user, priority))
    connection.commit()


#THIS IS A FUNCTION TO ASSIGN THE PROJECT MEMBERS
def assign_Task():
    print("Printing Kanban Board for reference")
    view_Kanban()
    print("Enter the task id of the task you want to assign")
    taskId = int(input())
    cursor.execute("SELECT * FROM kanban WHERE ID=?", (taskId,))
    result=cursor.fetchone()
    #Updating the table and inserting the name of user for that task

    if result:
        member_name = input("Enter the Project Member you want to assign the task to: ")
        # Updating the table and inserting the name of the user for that task
        cursor.execute("UPDATE kanban "
                       "SET User=? "
                       "WHERE ID=?", (member_name, taskId))
        connection.commit()
        print(f"Task {taskId} has been assigned to {member_name}")
    else:
        print(f"Task with ID {taskId} not found.")

#THIS FUNCTION IS TO CHANGE STATUS
def change_Status():
    print("Printing Kanban Board for reference")
    view_Kanban()
    taskID=int(input("Enter the task ID of the task to be shifted"))
    #Changing the task status
    cursor.execute("SELECT * FROM kanban WHERE ID=?",(taskID,))
    result=cursor.fetchone()
    if result:
        status = input("Enter the new status")
        cursor.execute("UPDATE kanban "
                       "SET Status=? "
                       "WHERE ID=?", (status, taskID))
        connection.commit()

    else:
        print(f"Task with ID {taskId} not found.")


#THIS FUNCTION IS TO VIEW  KANBAN BOARD
def view_Kanban():
    print("TODO")
    cursor.execute("SELECT ID,Task_Name,User,Priority FROM kanban WHERE Status=?",('TODO',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("IN PROGRESS")
    cursor.execute("SELECT ID,Task_Name,User,Priority FROM kanban WHERE Status=?", ('IN PROGRESS',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print("DONE")
    cursor.execute("SELECT ID,Task_Name,User,Priority FROM kanban WHERE Status=?", ('DONE',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)





# Main menu(driver code)
print("Welcome to Kanban Board,This is an empty Board")
#taking user input for functions
while (True):
    inp = int(input(
        "Enter\n1 for adding a task\n2 for assigning a task\n3 for changing status\n4 for veiwing the Kanban Board\n5 for exiting\n"))
    if (inp == 1):
        add_Task()
    elif (inp == 2):

        assign_Task()
    elif (inp == 3):
        change_Status()
    elif (inp == 4):
        view_Kanban()
        print(dict)
    elif (inp == 5):
        break
    else:
        print("Invalid Input")
        break



