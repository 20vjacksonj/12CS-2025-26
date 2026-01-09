'''
aim: write a program to usea 2D array to create a RECORD to store in an OBJECT
'''


class SONGS():
    def __init__(self):
        self.SONGS = []     #initialise empty array/ list
    #end def

    def add_song(self):
        pass
    #end def

    def remove_song(self):
        pass
    #end def

    def update_song_likes(self):
        pass
    #end def

#end class



def get_song_name():

    song_name_not_valid = True
    
    while song_name_not_valid:
        song_name = input("Enter song name or X to exit: ")

        #validate song name
        if song_name == "":
            print("Enter a song name")
        #endif
        elif song_name in "xX":
            print("Good Bye")
            break
       
#end def



#main starts here

def main():

    song_name = get_song_name()
    print(song_name)
    #end if

#end def

if __name__ == "__main__":
    main()
