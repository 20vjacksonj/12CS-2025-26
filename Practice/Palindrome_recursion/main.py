class Palindrome:

    def __init__(self):
        self.ask_list = []
        self.reverse_list = []
    #enddef

    def check_palindrome(self):

        self.ask = input("Enter string: ")


        for char in self.ask:       #APPENDS ALL CHARACTERS IN INPUT TO A LIST
            self.ask_list.append(char.lower())      #.lower() AS VALIDATION
        #endfor


        for i in range(len(self.ask_list)):         #FOR EVERY CHARACTER IN THE INPUT LIST
            self.index = len(self.ask_list) -(i+1)          #FINDS INDEX OF LAST CHARACTER IN INPUT LIST, -1 FOR EACH LOOP 
            self.last_char = self.ask_list[self.index]          #FINDS LAST CHARACTER OF INPUT STRING USING INDEX
            self.reverse_list.append(self.last_char)            #APPENDS THIS TO THE REVERSE LIST
        #endfor


        if self.ask_list == self.reverse_list:      #COMPARES INPUT LIST TO REVERSE LIST 
            print(f"{self.ask} is a palindrome\n")
        else:
            print(f"{self.ask} is not a palindrome\n")
        #endif

    #enddef

#endclass


if __name__ == "__main__":
    app = Palindrome()
    while True:
        app.check_palindrome()