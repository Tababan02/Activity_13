movie_genres_dict = {
    "Action" : "Mad Max: Fury Road",
    "Comedy" : "Superbad",
    "Drama" : "The Shawshank Redemption",
    "Horror" : "Get Out",
    "Science Fiction" : "Inception",
    "Romance" : "The Notebook",
    "Thriller" : "Se7en",
    "Fantasy" : "The Lord of the Rings: The Fellowship of the Ring",
}

# 2
print("The whole dictionary contains: ")
print(movie_genres_dict)

# 3
print("")
print("the example movie of the 3rd genre is ")
print(movie_genres_dict["Drama"])
      
# 4
print("")
print("after updating the example movie of the 5th genre.")
movie_genres_dict["Science Fiction"] = ['Arrival']
print(movie_genres_dict)

# 5
print("")
print("After deleting the 7th genre from the dictionary. ")
del movie_genres_dict["Thriller"]
print(movie_genres_dict)

# 6
print("")
last_key = list(movie_genres_dict.keys())[-1]
last_value = movie_genres_dict[last_key]
print("The last key-value pair is ", last_value, ":",last_key)