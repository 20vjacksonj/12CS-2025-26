import sqlite3

# define connection to database and establish a 'cursor' for accessing data
connection = sqlite3.connect("admin/myDatabase.db")
cursor = connection.cursor()


def display_students():

	""" display student details """
	selectStmt = "SELECT * from student;"
	students = cursor.execute(selectStmt)
	for student in students:
		print(f"\n{student}")
	#end for

#end def


def display_courses():

	""" display courses avaialble """
	
	selectStmt = "SELECT * from course;"
	courses = cursor.execute(selectStmt)
	for course in courses:
		print(f"\n{course}")
	#end for

#end def


def assign_student_to_course():

	""" assign student to course on 'link table' studentoncourse """
	
	#get student number
	while True:
		try:		
			studentid = int(input("Student ID? :"))
			break
		except ValueError:
			print("Integer required for Student ID")
		#end except
	#end while

	#get course number
	while True:
		try:		
			courseid = int(input("Course ID? :"))
			break
		except ValueError:
			print("Integer required for Course ID")
		#end except
	#end while
			
	insertStmt = "INSERT INTO studentoncourse (courseid,studentid) VALUES (?,?)"
	params = (courseid, studentid)
	cursor.execute(insertStmt, params)

#end def


def menu_select():

	print("\n1. Display Students")
	print("2. Display Courses")
	print("3. Assign Student to Course")
	print("9. Exit\n")

	while True:
		choice = input(">")
		if choice in "1239":
			break
		#end if		
	#end while
	return choice
	
#end def

	
# main starts here -massign student to course
while True:

	""" select and print data from student table """
	
	menu = menu_select()
	if menu == "9":
		break
	elif menu == "1":
		display_students()
	elif menu == "2":
		display_courses()
	else:
		assign_student_to_course()
	#end if

#end while