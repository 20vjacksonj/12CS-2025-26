'''
A text-based computer game allows a user to dig for treasure on an island. The island is designed as a grid with
10 rows and 20 columns to store the treasure. Each square is given an x and y coordinate. Some of the squares
in the grid store the name of a treasure object. Each treasure object has a value, e.g. 100 and a level, e.g.
"Bronze."

The treasure game is being programmed using an object-oriented paradigm.
A class, Treasure, is used to store the treasure objects.

The design for the Treasure class, its attributes and methods is shown here.

class: Treasure
attributes:
private value : integer
private level : string
methods:
new()
function getValue()
function getLevel()
'''

# declare 2d array / lists to hold grid position 
# declare classes

grid_positions = [
    
]

for i in range(10):
    grid_positions.append([None])
    for k in range(20):
        grid_positions.append([None])

print(grid_positions)

class treasure:

    def __init__(self, value, level):
        self.value = value 
        self.level = level
    #enddef

    def new(self):
        pass

    def getValue(self):     #getter method
        return self.value
    #enddef

    def getLevel(self):     #getter method
        return self.level 
    #enddef

#endclass