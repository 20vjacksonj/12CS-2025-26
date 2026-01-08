'''
functionality - ALT Z
read paragraph from mybook.txt and validate for errors
program searches text and makes a dictionary of unique words
each time the word is found it adds to the dictionary its position in the paragraph
process until no more words

techniques:
find a memorable paragraph online from book/text

'''

def read_book():

    myfile = open("H:/github/12CS-2025-26/Practice/Book_challenge/my_book.txt", "r", encoding = "utf-8")

    textline = myfile.readline().replace(",", "").split(" ")

    myfile.close()

    return textline

#enddef



#main starts here

result = read_book()
print(result, len(result))

#write a loop to process each word and add to the dictionary with its position 


words = {}
index = 0

exit = False
while not exit:

    if result[index] not in words:
        words = result[index]
    #endif

    if index == len(result):
        print(words)
        break
#endwhile

print(words)

