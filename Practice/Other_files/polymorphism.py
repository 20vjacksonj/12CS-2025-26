class Animal:
    def __init__(self, name, weight, legs):
        self.name = name
        self.weight = weight
        self.legs = legs
    #enddef
#endclass 

class Rabbit(Animal):
    def __init__(self, name, weight, legs, fur):
        super().__init__(name, weight, legs)
        self.fur = True 
    #enddef
#endclass


#polymorphism is the ability to change attributes within an instance of a class, can have differnet behaviours eg furless rabbit maybe