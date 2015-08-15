# project/db_create.py
from views import db
from models import Task
from datetime import date

# create the databse and the db table
db.create_all()

# insert data
db.session.add(Task("Finish this tutorial", date(2015, 20, 9), 10, 1))
db.session.add(Task("Finish Real Python", date(2015, 20, 12), 10, 1))
db.session.add(Task("Database Menagement", date(2015, 15, 9), 1, 1))
db.session.add(Task("User Registration", date(2015, 16, 9), 2, 1))
db.session.add(Task("User Login/Authentication", date(2015, 17, 9), 3, 1))
db.session.add(Task("Database Relationships", date(2015, 18, 9), 4, 1))

# commit the changes
db.session.commit()
