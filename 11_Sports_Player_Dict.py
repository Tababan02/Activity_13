sports_players_dict = { 
		"Soccer": "Pelé",
		"Basketball": "Michael Jordan",
		"Tennis": "Serena Williams",
		"Golf": "Tiger Woods",
		"American Football": "Tom Brady",
		"Baseball": "Babe Ruth",
		"Hockey": "Wayne Gretzky",
		"Cricket": "Sachin Tendulkar",
		"Boxing": "Muhammad Ali",
		"Rugby": "Richie McCaw"
}


# 2
print("The whole dictionary contains: ") 
print(sports_players_dict)

# 3
print("")
print("The player of the 4th sports is: ")
print(sports_players_dict["Golf"])
print(sports_players_dict)

# 4
print("")
print("After Updating the player of the 6th sport: ")
sports_players_dict['Baseball'] = "SANDARA"
print(sports_players_dict)

# 5
print("")
print("After Deleting the 10th sport from the dictionary: ")
del sports_players_dict['Rugby']
print(sports_players_dict)

# 6
print("")
last_key = list(sports_players_dict.keys())[-1]
last_value = sports_players_dict[last_key]
print("The last key-value pair is: ", last_key , ":", last_value)
