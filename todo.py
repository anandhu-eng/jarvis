
import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")
option=int(input("1 for adding task, 2 for viewing all the task:"))
if(option==1):
    task=input("Enter the task:")
    inst="INSERT INTO tasks (Task) VALUES ('{task}');".format(task=task)
    conn.execute("INSERT INTO tasks (Task) VALUES ('{task}');".format(task=task))
    conn.commit()
    print("task successfully added!",inst)
else:
    cursor = conn.execute("SELECT Number, Task from tasks")
    for i in cursor:
        print(i[1])


conn.close()