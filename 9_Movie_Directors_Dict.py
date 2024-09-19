movie_directors_dict = {
	"Inception" : "Christopher Nolan",
	"The Godfather" : "Francis Ford Coppola",
	"Pulp Fiction" : "Quentin Tarantino",
	"Schindler's List" : "Steven Spielberg",
	"The Shawshank Redemption" : "Frank Darabont",
	"The Dark Knight" : "Christopher Nolan",
	"Forrest Gump" : "Robert Zemeckis",
	"Fight Club" : "David Fincher",
	"Interstellar" : "Christopher Nolan",
	"Get Out" : "Jordan Peele"
	}

# 2 
print("The whole dictionary contains: ")
print(movie_directors_dict)
print("")

# 3
print("The director of the 5th movie is: ")
print(movie_directors_dict ['The Shawshank Redemption'])
print(movie_directors_dict)
print("")

# 4
print("After updating director of the 9th movie: ")
movie_directors_dict["Interstellar"] = 'SANDARA'
print(movie_directors_dict)
print("")

# 5
print("After deleting the 7th movie from the dictionary ")
del movie_directors_dict['Forrest Gump']
print(movie_directors_dict)
print("")

# 6
last_key = list(movie_directors_dict.keys())[-1]
last_value = movie_directors_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)