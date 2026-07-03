'''
provides ability to see what data is in a table
'''

import sqlite3

# define connection to database and establish a cursor for accessing data
connection = sqlite3.connect("myDatabase.db")
cursor = connection.cursor()

# select and print data from student table
selectStmt = "SELECT * from student;"
students = cursor.execute(selectStmt)
for student in students:
  print(student)

# select and print data from course table
selectStmt = "SELECT * from course;"
courses = cursor.execute(selectStmt)
for course in courses:
  print(course)

selectStmt = "SELECT * from studentoncourse;"
sonc = cursor.execute(selectStmt)
for s in sonc:
  print(s)

connection.commit()
connection.close()
