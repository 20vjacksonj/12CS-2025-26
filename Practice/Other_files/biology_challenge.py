'''
simple program to practice OO with inheritance - super- and sub- classing
NB:
. the term class in heirarchy is not class in OO
. may be difficult to indentify common attributes and specialoised attributes that distinguish species
context:
. biological field
. for simplicity we will lower levels of heirarchy and use recognisable information
'''

class carcharodon(): #genus

    def __init__(self):
        self.fins = True
        self.num_fins = 7
        self.teeth = 300
    #end def

    def hunt(self):
        print("I can hunt anything")
    #end def

    def swim(self):
        print("i can swim anywhere")
    #end def

#end class


class carcharias(carcharodon): #species

    def __init__(self):
        super().__init__()
        self.humans_eaten = 1
        self.prey_list = []
    #end def

    def eat_human(self):
        self.humans_eaten += 1
    #end def

    def add_prey(self, prey):
        self.prey_list.append(prey)
    #end def

    def hunt(self):
        print("I LIKE SEALS")
#end class


#main starts here
GreatWhiteShark = carcharias()

#list prey of great white shark
GreatWhiteSharkPrey = GreatWhiteShark.prey_list

#print prey list
print(GreatWhiteSharkPrey)

#add rubber dingy to diet
GreatWhiteShark.add_prey("rubber dingy")

#check if added
print(GreatWhiteShark.prey_list)

#harry's challenge - print out the super class / parent attributes 
print(GreatWhiteShark.fins)
print(GreatWhiteShark.num_fins)
print(GreatWhiteShark.teeth)

GreatWhiteShark.hunt()