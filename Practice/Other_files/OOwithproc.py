'''
I need to use OO - constructor, instantiate, inheritence 
I need to use a procedure that takes parameters

context - garden layout for plants 
'''

class GardenItem:

    def __init__(self, itemName, length, width):
        self.__itemName = itemName
        self.__length = length
        self.__width = width
    #enddef

    def _getItemName(self):
        return self.__itemName
    #enddef
#endclass


class Tree(GardenItem):

    def __init__(self, itemName, length, width, height, sun, shade):
        super().__init__(itemName, length, width)
        self.__height = height
        self.__sun = sun 
        self.__shade = shade
    #enddef
#endclass


firstTree = Tree("Common Oak", 40,40,40,True,True)

print(firstTree._getItemName())