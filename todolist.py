import os, sys
import sqlite3
from tabulate import tabulate 
from datetime import datetime
from termcolor import colored
status = True

DEFAULT_PATH = os.path.join(os.path.dirname(__file__),
'database.sqlite3')
#conn default_path will connected to sqlite3
conn = sqlite3.connect(DEFAULT_PATH)
# cur communicate between sql and python
cur = conn.cursor()


# create tables
sql = """
    CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY,
        body TEXT NOT NULL,
        date TEXT NOT NULL,
        status TEXT DEFAULT "incomplete"
    )
"""

cur.execute(sql)
conn.commit()

# sql = """
#     CREATE TABLE IF NOT EXISTS 
# """


def show():
    sql = """
    SELECT * FROM todos
    """
    cur.execute(sql)
    result = cur.fetchall()
    print("\033c")
    print('count: ',len(result))
    print(colored(tabulate(result, headers = ['id','body','date','status'],tablefmt='grid'),'green'))
    


def add():
    print("add body:")
    body = input()
    date = datetime.now()
    sql ="""
    INSERT INTO todos
    (body,date)
    VALUES (?,?)
    """
    cur.execute(sql,(body, date))
    conn.commit()
    print("\033c")
    show()

def update():
    show()
    print("which id you want to change:")
    todo_id = int(input())
    print("body: ")
    body = input()
    print("Did this task complete or incomplete ?")
    status = input()
    date = datetime.now()
    if status == "complete":
        action = "complete"
    if status == "incomplete":
        action = "incomplete"
    sql = """
        UPDATE todos set status = (?), body = (?), date = (?) WHERE id = (?)
    """
    cur.execute(sql,(action,body,date,todo_id))
    conn.commit()
    print('\033c')
    show()

def remove():
    show()
    print("what todo you want to delete?")
    todo_id = int(input())
    sql ="""
    DELETE FROM todos WHERE id = (?)
    """
    cur.execute(sql,(todo_id,))
    conn.commit()
    show()

def returnn():
    list_question()

def incomplete_task():
    sql = """
    SELECT * FROM todos WHERE status="incomplete" 
    """
    cur.execute(sql)
    result = cur.fetchall()
    print('\033c')
    print('incomplete task:',len(result))
    print(colored(tabulate(result, headers = ['id','body','date','status'],tablefmt='grid'),'green'))

def complete_task():
    sql="""
    SELECT * FROM todos WHERE status="complete"
    """
    cur.execute(sql)
    result = cur.fetchall()
    print('\033c')
    print('complete task',len(result))
    print(colored(tabulate(result, headers = ['id','body','date','status'],tablefmt='grid'),'green'))

def list_question():
    global status
    print(colored('1. show table','magenta'))

    print(colored('2. add','magenta'))
    print(colored('3. update','magenta'))
    print(colored('4. remove','magenta'))
    print(colored('5. return','magenta'))
    print(colored('6. incomplete task','magenta'))
    print(colored('7. complete task','magenta'))
    print(colored('8. close','magenta'))
    print(colored("choose 1 option:",'magenta'))
    option = input()
    if option == "1":
        show()
    elif option == "2":
        add()
    elif option == "3":
        update()
    elif option == "4":
        remove()
    elif option == "5":
        returnn()
    elif option == "6":
        incomplete_task()
    elif option == "7":
        complete_task()
    elif option == "8":
        status = False
  



if __name__ == "__main__":
    try:
        print('Please input your name!')
        name = input()
        print(colored('Hello ,' ,'red'), name)
        print('------todolist-------')
        while status:      
            list_question()
    except:
        print('invalid!')
        list_question()