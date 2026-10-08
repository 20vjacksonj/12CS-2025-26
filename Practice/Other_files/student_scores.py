'''
lets look at dicitionaries
a dictionary has a term and its defenition
a python dictionary has a {key:value} pair 
'''

student_scores = {
    "james" : {
        "maths" : 30,
        "english" : 50,
        "science" : 70
    },
    "walton" : {
        "maths" : 30,
        "english" : 50,
        "science" : 70
    },
    "nate" : {
        "maths" : 30,
        "english" : 50,
        "science" : 70
    },
    "jacob j" : {
        "maths" : 30,
        "english" : 50,
        "science" : 70
    },
    "aayan" : {
        "maths" : 30,
        "english" : 50,
        "science" : 70
    },
    "harry" : {
        "maths" : 30,
        "english" : 50,
        "science" : 70
    },
    "jacob c" : {
        "maths" : 30,
        "english" : 50,
        "science" : 70
    }
}


def get_score(ask):
    exit = False

    while not exit:
        subject = input("Enter subject: ").lower()
        if subject not in ["maths", "english", "science"]:
            print("not available")
        else:
            exit = True

    return subject, student_scores[ask][subject]
#endfunc


run = True
while run:
    ask = input("Enter name of student or x to exit: ").lower()

    if ask == "x":
        run = False
    elif ask not in student_scores:   
        print("Not in students")
    else:
        subject, score = get_score(ask)
        print(score)
#endwhile