'''
hash a value and place the data in a specific position in an array/list
if occupied, rehash to next position and repeat
'''

student_names = [None]*10

def hash_name(name):

    hash_total = 0
    for char in name:
        hash_total += ord(char)
    #end for

    # mod for position
    hash_position = hash_total % len(student_names) 

    num_attempts = len(student_names)

    placed = False
    while (not placed) and (num_attempts) > 0:
        
        # check if space occupied
        if student_names[hash_position] == None:
            placed = True
        else: 

            print(f"Position {hash_position} already occupied")

            if hash_position == len(student_names) - 1:
                hash_position = 0
            else:
                hash_position += 1
            #end if
            num_attempts -=1

        #end if 

    #end while

    return hash_position, num_attempts

#end def

# main here

def main():

    exit = False
    while not exit:

        name = input("First Name > ").lower().strip()
        if name == "":
            print("Try again")
        else:
            hash_position, rehashes = hash_name(name)
            #print(hash_position, rehashes)

            if student_names[hash_position] == None:
                student_names[hash_position] = name
            else:
                if rehashes == 0:
                    print("Could not place, array is full..exiting")
                    exit = True
                else:
                    print(hash_position)
                #end if
        #endif

    #end while

#end def

if __name__ == "__main__":
    main()