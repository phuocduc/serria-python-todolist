Install environment python on window
- download and install python
- pip install virtualenv
- pip install virtualenvwrapper-win


R.E.P.L. Setup

1. mkdir p-todolist
2. cd p-todolist
3. virtualenv -p python3 venv  
4. source venv/bin/activate   
5. Import libraries

import os
import sqlite3
from termcolor import colored

6. Define root path
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

7. Define SQLITE conn & cur
conn = sqlite3.connect(DEFAULT_PATH)
cur = conn.cursor()

8. Setup DB with first sql query

sql = """
  CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY,
    body TEXT NOT NULL,
    user_id INTEGER,
  )
"""

cur.execute(sql)
conn.commit()
9. Demonstrate sql in sidebar˛

10. Define R.E.P.L.

if __name__ == '__main__':
try:
    while True:

  except IndexError:
    print_menu()


Note: to create tables link together follow link below,
https://stackabuse.com/a-sqlite-tutorial-with-python/