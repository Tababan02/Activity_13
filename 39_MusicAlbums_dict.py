music_albums_dict = {
    "The Dark Side of the Moon" : 1973,
    "Thriller" : 1982,
    "Back in Black" : 1980,
    "Abbey Road" : 1969,
    "Rumours" : 1977,
    "Nevermind" : 1991,
    "21" : 2011,
    "Born to Run" : 1975,
    "Hotel California" : 1976,
    "1989" : 2014

}
# 2
print("The whole dictionary contains: ")
print(music_albums_dict)

# 3
print("")
print("The release year of the 3rd album is ")
print(music_albums_dict ["Back in Black"])
      
# 4
print("")
print("after updating  the release year of the 8th album: ")
music_albums_dict["Born to Run "] = "2000"
print(music_albums_dict)

# 5
print("")
print("after deleting the 5th album from the dictionary: ")
del music_albums_dict["Rumours"]
print(music_albums_dict)


# 6
print("")
last_key = list(music_albums_dict.keys())[-1]
last_value = music_albums_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)