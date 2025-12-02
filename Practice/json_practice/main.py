'''
This program allows me to book a cinema ticket.
It loads the dictionary (key:value) from a json file to show the movies, prices, times, availability and rating.
'''

import json

def load_json_data():

	try:
		f = open("data.json","r") 
		# returns JSON object as a dictionary
		data = json.load(f)
		f.close()
	except FileNotFoundError:
		return 0
	#endexcept

	print(json.dumps(data, indent = 4, sort_keys=False))

	return data

#enddef


def print_movie_details(movie_data):

	print("\nMovies available today...\n")
	for movie in movie_data["movies"]:

		movie_name = movie["movie"]
		movie_times = movie["opening_times"]
		movie_price = movie["price"]
		movie_rating = movie["rating"]
		print(f"\n'{movie_name}' \nshow times: {movie_times} \n£{movie_price:5.2f} {movie_rating:4}")
		
	#endfor

#enddef


def check_movie(json_data):

	found = False
	i = 0
	while not found and i < num_movies:

		movie_detail = json_data["movies"][i].values()

		if movie_choice not in movie_detail or movie_choice == "":
			print("\nMovie not available or movie name not valid")
			i+=1
		else:
			found = True
			movie_times = json_data["movies"][i]["opening_times"]
		#endif

	#endwhile

#enddef


def check_movie_choice(json_data, movie_choice):

	num_movies = len(json_data["movies"])

	found = False
	movie_index = 0

	while not found and movie_index < num_movies:

		movie_detail = json_data["movies"][movie_index].values()

		if movie_choice not in movie_detail or movie_choice == "":
			movie_index += 1
		else:
			found = True
		#endif

	#endwhile

	return movie_index, num_movies

#enddef



def pick_a_movie(json_data):

	total_cost = 0
	movie_cost = 0

	while True:

		print_movie_details(json_data)

		# choose a movie
		while True:
			
			movie_choice = input("\nWhich movie do you want to watch? Q=Quit ==> ")
			if movie_choice in "Qq":
				exit(1)
			#endif

			movie_number,num_movies = check_movie_choice(json_data,movie_choice)

			if movie_number < num_movies:
				movie_times = json_data["movies"][movie_number]["opening_times"]
				break
			else:
				print("\nMovie not available or movie name not valid")
			#endif

		#endwhile

		# pick a time

		while True:

			print(f"\n{movie_choice} is available at these times {movie_times}")
			view_time = input(f"\nWhat time do you want to watch {movie_choice}? ==> ")

			if view_time not in movie_times:
				print(f"\n{movie_choice} not available at: {view_time}")
				continue
			else:
				avail_index = movie_times.index(view_time)
				movie_seats_avail = json_data["movies"][movie_number]["availability"][avail_index]
				break
			#endif

		#endwhile

		# check availability

		while True:

			num_tickets = int(input("\nHow many tickets would you like? ==> "))
			if num_tickets < 1:
				print("Number must be greater than 0")
				continue
			elif num_tickets > movie_seats_avail:
				print(f"\nSorry, there are {movie_seats_avail} tickets at {view_time}")
				break
			else:
				# update number tickets available for that movei at thayt time

				json_data["movies"][movie_number]["availability"][avail_index] -= num_tickets

				# calcualte movie cost
		
				movie_cost = json_data["movies"][movie_number]["price"]

				print(f"\nMovie cost: {num_tickets}  tickets to watch {movie_choice} = £{movie_cost:5.2f}")
				#calculate total cost
				total_cost = total_cost + (num_tickets * movie_cost)
				print(f"\nTotal cost: £{total_cost:5.2f}")
				break
			#endif

		#endwhile

		again = input("\nDo you want to order more tickets [Y or N] ? ==> ").upper()
		if again == "Y":
			continue
		else:
			break
		#endif

	#endwhile

#enddef


#main starts here
movie_data = load_json_data()
if not movie_data:
	print("Error Opening File")
else:
	#print(movie_data)
	pick_a_movie(movie_data)
#endif
