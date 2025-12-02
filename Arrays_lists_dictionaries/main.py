'''
practice with following data structures:
- arrays = lists in python, 1D and 2D
- dictionaries = {key, value} pairing

LISTS in programming theory are usually linked lists that use nodes of data and pointers between nodes to show relationships 
'''

#create a 1D list of subjects
subjects = ["maths", "computer science", "geography"]
students = []

print(f"Length of list: {len(subjects)}")

print(f"middle item is {subjects[1]}")


#create a class called student
class student():

    #constructor method
    def __init__(self, name, age):
        self.name = name        #set attribute name to parameter name
        self.age = age      #set atribute age to parameter age
    #end def

    def get_name(self):
        return self.name
    #end def

    def set_age(self, new_age):
        self.age = new_age
    #end def

    def get_age(self):
        return self.age
    #end def
    
#end class


#main starts here
#instantiate a class as an object for student
james = student(name = "James", age = 75)

#get name from object called james
student_name = james.get_name()
print(student_name)

#add student object to array
students.append(james)      #add to end of list
print(students[0])

#lets get age from list for the first student 
age = students[0].get_age()
print(age)


#write a loop to collect name and ages 
#exit when name = x
#add each name age combo to the list as an object
#when loop finishes, print out each name of student from array
while True:

    name = input("Enter name or X to exit: ")

    if name in "xX":
        print("")
        break

    else:

        try:
            age = int(input("Enter age of this student: "))
        except ValueError:
            print("Need a number")
        
        if age < 5 or age > 20:
            print("Need to be between 5 and 20")
            print("")
            continue

        else:
            print("")
            new_student = student(name,age)
            students.append(new_student)
#endwhile

for student in students:
    print(student.get_name(), student.get_age())
#endfor

