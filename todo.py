
import sqlite3
from speech_commands import say


#print("Opened database successfully")
#option=int(input("1 for adding task, 2 for viewing all the task:"))
#if(option==1):
#    task=input("Enter the task:")
#    inst="INSERT INTO tasks (Task) VALUES ('{task}');".format(task=task)
#    conn.execute("INSERT INTO tasks (Task) VALUES ('{task}');".format(task=task))
#    conn.commit()
#    print("task successfully added!",inst)
#else:
#    cursor = conn.execute("SELECT Number, Task from tasks")
#    for i in cursor:
#        print(i[0],i[1])

#funcion to know the remaining task
def pending_task():
    conn = sqlite3.connect('test.db')
    cursor = conn.execute("SELECT Number, Task from tasks")
    for i in cursor:
        tosay=str(i[0])+" "+i[1]
        say(tosay)
        #print(i[0],i[1])
    conn.close()
