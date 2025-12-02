'''
hash a value and place the data in a specific position in an array/list
if occupied, rehash to next position and repeat
'''

# 3 x 10 --> 
COLUMNS = 3 # for overflow
ROWS = 10   # for first entry

# populate 2d grid ==> COL 0 = main entry COLS 1,2 = overflow
student_names = [ [None] * COLUMNS for i in range(ROWS) ]
print(student_names)


def rehash(hash_row, name):

    placed = False
    hash_col = 1

    while not placed and hash_col < len(student_names[hash_row][0])-1:
        print(student_names[hash_row][hash_col])
        if student_names[hash_row][hash_col] == None:
            student_names[hash_row][hash_col] = name
            placed = True
        else:
            hash_col +=1
        #end if
    #end while

    if not placed:
        print("Overflow is full")
    else:
        print("stdent placed in overflow")
    #end if

#end def


def hash_name(name):

    hash_total = 0
    for char in name:
        hash_total += ord(char)
    #end for

    # mod for position
    hash_row = hash_total % (ROWS - 1) 
    print(student_names[hash_row][0])

    if student_names[hash_row][0] == None:
        student_names[hash_row][0] = name
        print(f"Student {name} hashed to {hash_row}")
    else:
        print(f"Position {hash_row} already occupied")

        success = rehash(hash_row, name)

    #end if 

    return hash_row

#end def

# main here

def main():

    exit = False
    while not exit:

        name = input("First Name or p to print, x to exit > ").lower().strip()
        if name == "":
            print("Try again")
        elif name == "p":
            print(student_names)
        elif name == "x":
            exit = True
        else:

            hash_row = hash_name(name)

        #endif

    #end while

#end def

if __name__ == "__main__":
    main()