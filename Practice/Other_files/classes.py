'''
first program
'''

print("HELLO WORLD")

#a class is a blueprint for an object
class Animal():
    def __init__(self, name, speed, num_legs):   #constructor method, pseudo is new method
        self.name = name
        self.speed = speed
        self.num_legs = num_legs
    #end def

    def set_name(self, new_name):    #setter method
        self.name = new_name
    #end def

    def get_name(self): #getter method
        return self.name
    #end def

#end class

#main starts here
tiger = Animal(name = "Tiger", speed = 30, num_legs = 5)    #this instantiates an object from the class using the constructor method
print(tiger.get_name())

#write a call to animal object to change name to something different 

tiger.set_name("Dopey tiger")
print(tiger.get_name())