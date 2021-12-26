
import sqlite3
from speech_commands import say


#since the table and the columns are predefined on the database file test.db
#which is not pushed to the github repo, additional commands for creating table
#and columns are not given.

#funcion to know the remaining task
def pending_task():
    conn = sqlite3.connect('test.db')
    cursor = conn.execute("SELECT Number, Task from tasks")
    for i in cursor:
        tosay=str(i[0])+" "+i[1]
        say(tosay)
        #print(i[0],i[1])
    conn.close()

#function to add new task
def add_task(task):
    conn = sqlite3.connect('test.db')
    conn.execute("INSERT INTO tasks (Task) VALUES ('{task}');".format(task=task))
    conn.commit()
    msg="task "+task+" added successfully"
    say(msg)
    conn.close()