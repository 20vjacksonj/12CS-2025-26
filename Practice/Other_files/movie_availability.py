'''
simple project to create a ticketng system that uses;
.json/dictionary to store ticket data
.OO objects from classes to manage data through methods

features;
.find ticket availability for a specific film
.find price for a specific film at a specific time and venue
.print available tickets report for each film
'''

#define a suitable, named dictionary to look after this data

cinema_tickets = {
    "huntingdon" : {
        "movies":{
            1 : "batman",
            2 : "minions"
        },
        "times":{
            1 : [10.00, 11.30],
            2 : [08.30, 09.00]
        },
        "prices": {
            1 : [10.00, 15.00],
            2 : [20.00, 30.00]
        },
        "availability" : {
            1 : [14,45],
            2 : [33, 12]
        }
    },
    "cornwall" : {
        "movies":{
            1 : "batman",
            2 : "minions"
        },
        "times":{
            1 : [10.00, 11.30],
            2 : [08.30, 09.00]
        },
        "prices": {
            1 : [10.00, 15.00],
            2 : [20.00, 30.00]
        },
        "availability" : {
            1 : [14,45],
            2 : [33, 12]
        }
    },
    "aberdeen" : {
        "movies":{
            1 : "batman",
            2 : "minions"
        },
        "times":{
            1 : [10.00, 11.30],
            2 : [08.30, 09.00]
        },
        "prices": {
            1 : [10.00, 15.00],
            2 : [20.00, 30.00]
        },
        "availability" : {
            1 : [14,45],
            2 : [33, 12]
        }
    }

}

print("1. Check movie availability")
print("2. Check ticket price")
print("3. Print available tickets")
print("4. exit")


def check_availability():
    for movie in cinema_tickets["huntingdon"]["movies"]:
        print(movie)


def menu():
    run = True
    while run:
        choice = input("Enter your choice of 1-4: ")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice")
        else:
            run = False
    return choice

def main():
    menu()
    if choice == "1":
        check_availability()

exit = False
while not exit:
    main()




































'''def ask_movie_func(ask_place):
    exit = False

    while not exit:
        ask_movie = input("Enter name of movie: ").lower()
        if ask_movie not in ["batman", "minions", "titanic"]:
            print("not available")
        else:
            exit = True
    return ask_movie, cinema_tickets[ask_place][ask_movie]

#endfunc

def ask_time_func(ask_movie):
    exit = False

    while not exit:
        ask_time = input("Enter time: ")
        if ask_time not in ["10:30", "12:00","14:00"]:
            print("Not available")
        else:
            exit = True
    return ask_time , cinema_tickets[ask_movie][ask_time]



run = True
while run:

    ask_place = input("Enter place: ").lower()

    if ask_place not in cinema_tickets:
        print("Not available")

    else:
        ask_movie = ask_movie_func(ask_place)
        ask_time = ask_time_func(ask_movie)'''
