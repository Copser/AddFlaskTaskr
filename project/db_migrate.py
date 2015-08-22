# project/db_migrate.py
from views import db
from _config import DATABASE_PATH

import sqlite3
# from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # temporarily change the name of tasks table
    c.execute("""ALTER TABLE users RENAME TO old_users""")

    # recreate a new tasks table with update schema
    db.create_all()

    # retrieve data from old_tasks table
    c.execute("""SELECT name, email, password FROM old_users ORDER BY id ASC""")

    # save all rows as a list of tuples; set posted_data to now and user_id to 1
    data = [(row[0], row[1], row[2], 'user') for row in c.fetchall()]
    # insert data to tasks table
    c.executemany("""INSERT INTO users (name, email, password, role)
        VALUES (?, ?, ?, ?)""", data)

    # delete old_tasks table
    c.execute("DROP TABLE old_users")
