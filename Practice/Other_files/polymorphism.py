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

