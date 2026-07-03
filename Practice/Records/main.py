'''
aim: write a program to usea 2D array to create a RECORD to store in an OBJECT
'''


class SONGS():
    def __init__(self):
        self.songs = []     #initialise empty array/ list
    #enddef

    def add_song(self, sname, sartist, slikes, sfavourite):
        self.song = []
        self.song = [sname, sartist, slikes, sfavourite]
        self.songs.append(self.song)
    #enddef

    def remove_song(self):
        pass
    #enddef

    def update_song_likes(self):
        pass
    #enddef

#endclass



def get_song_name():

    song_name_not_valid = True
    
    while song_name_not_valid:
        song_name = input("Enter song name or X to exit: ")

        #validate song name
        if song_name == "":
            print("Enter a song name")

        elif song_name in "xX":
            print("Good Bye")
            break

        else:
            return song_name
        #endif

    #endwhile

#enddef



def get_artist_name():

    artist_name_not_valid = True

    while artist_name_not_valid:
        artist_name = input("Enter artist name: ")

        #validate artist name
        if artist_name == "":
            print("Enter an artist name")

        else:
            return artist_name
        #endif

    #endwhile

#enddef



def get_song_likes():

    song_likes_not_valid = True

    while song_likes_not_valid:
        song_likes = input("Enter amount of likes: ")

        #validate song likes
        if song_likes.isdigit() == False:
            print("Need a number")

        else:
            return song_likes
        #endif

    #endwhile

#enddef





def is_favourite():

    favourite_not_valid = True

    while favourite_not_valid:
        favourite = input("Is the song favourited? (Y/N): ").upper()

        if favourite not in "YN" or favourite == "":
            print("Enter either Y or N")

        elif favourite == "Y":
            return True

        elif favourite == "N":
            return False
        #endif

    #endwhile

#enddef



#main starts here

def main():

    mySONGS = SONGS()

    #ask for inputs
    song_name = get_song_name()
    artist_name = get_artist_name()
    song_likes = get_song_likes()
    favourite = is_favourite()

    #create song record in SONGS object, call song method
    mySONGS.add_song(sname = song_name,
                    sartist = artist_name,
                    slikes = song_likes,
                    sfavourite = favourite
                      )
    

    print(mySONGS.songs)

#enddef

if __name__ == "__main__":
    main()
#endif