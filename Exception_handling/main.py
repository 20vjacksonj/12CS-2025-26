'''
Handling exceptions which are unexpected events in our code such as:
- user input or data conversions that stop things suddenly 
- file handling issues such as:
    - file not found in place expected
    - file name wrong
    - file opened in wrong mode (r,w,a, etc)
    - file empty 
'''




'''
while loop to ask user for number
'''

exit = False
while not exit:

    try:
        num = int(input("Enter a number: "))    #only one thing at a time in a try
    except ValueError:
        print("Need a whole number please\n")
        continue
    except KeyboardInterrupt:
        print("\nStop trying to break the system!\n")
        continue
    #endexcept
    exit = True

#endwhile



'''
open the file for reading
'''

myfile = open("H:/github/12CS-2025-26/Exception_handling/results.txt", "r")

exit = False
while not exit:

    textline = myfile.readline().strip()

    if textline == "":   #EOF reached
        exit = True
    else:
        print(textline)
    #endif

#endwhile
