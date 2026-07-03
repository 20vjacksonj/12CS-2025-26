'''
creates tables in the schema but drops them if they arleady exist
'''


import sqlite3

# define connection to database and establish a cursor for accessing data
connection = sqlite3.connect("myDatabase.db")
cursor = connection.cursor()


def createTables():

	""" create db tables in schema"""
	
	createStmt = "CREATE TABLE student(studentid INTEGER PRIMARY KEY, studentname VARCHAR(20), studentage INTEGER);"
	cursor.execute(createStmt)

	createStmt = "CREATE TABLE course(courseid INTEGER PRIMARY KEY, coursename VARCHAR(20), coursestart DATE);"	
	cursor.execute(createStmt)

	# we have a composite key on studentd id + course id
	createStmt = "CREATE TABLE studentoncourse(studentid INTEGER, courseid INTEGER, PRIMARY KEY (studentid, courseid) );"
	cursor.execute(createStmt)
	
	print("Empty Tables created")
	
#end def


def dropTables():
	
	""" remove tables from db schema - IF THEY EXIST """
	
	deleteStmt = "DROP table IF EXISTS student;"
	cursor.execute(deleteStmt)
	
	deleteStmt = "DROP table IF EXISTS course;"
	cursor.execute(deleteStmt)
	
	deleteStmt = "DROP table IF EXISTS studentoncourse;"
	cursor.execute(deleteStmt)

	print("Existing Tables dropped")

#end def


def insertCourseRecord(courserecord):

	print("\tinserting course",courserecord)
	query = 'INSERT INTO course (courseid, coursename, coursestart) VALUES (?,?,?)'
	params = (courserecord[0], courserecord[1], courserecord[2])
	cursor.execute(query, params)
	
#end def


def insertStudentRecord(studentrecord):

	print("\tinserting student", studentrecord)
	query = 'INSERT INTO student (studentid, studentname, studentage) VALUES (?,?,?)'
	params = (studentrecord[0], studentrecord[1], studentrecord[2])
	cursor.execute(query, params)

#end def


def processStudentFile():

	print("Importing data from 'students.txt' file")
	
	studentfile = open("students.txt","r")
	while True:
		studentrecord = studentfile.readline().strip()
		if studentrecord == "":
			break
		else:
			studentrecord = studentrecord.split(",")
			insertStudentRecord(studentrecord)
		#endif
	#endwhile
	studentfile.close()

#end def


def processCourseFile():

	print("Importing data from 'courses.txt' file")

	coursefile = open("courses.txt","r")
	while True:
		courserecord = coursefile.readline().strip()
		if courserecord == "":
			break
		else:
			courserecord = courserecord.split(",")
			insertCourseRecord(courserecord)
		#endif
	#endwhile
	coursefile.close()

#end def


# main starts here
dropTables()
createTables()
processStudentFile()
processCourseFile()

connection.commit()	# make sure all changes are committed to the DB
connection.close()