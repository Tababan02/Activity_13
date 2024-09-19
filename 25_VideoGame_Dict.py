video_game_platforms_dict = {
    "The Legend of Zelda: Breath of the Wild" : "Nintendo Switch",
    "God of War" : "PlayStation 4",
    "Minecraft" : "Multi-platform",
    "Call of Duty: Warzone" : "PC, PlayStation, Xbox",
    "Super Mario Odyssey" : "Nintendo Switch",
    "Red Dead Redemption 2" : "PC, PlayStation, Xbox",
    "Fortnite" : "Multi-platform",
    "The Witcher 3: Wild Hunt" : "PC, PlayStation, Xbox, Switch",
    "Animal Crossing: New Horizons" : "Nintendo Switch",
    "Cyberpunk 2077" : "PC, PlayStation, Xbox",
}

# 2
print("The whole dictionary contains: ")
print(video_game_platforms_dict)

# 3
print("")
print("The platform of the 2nd Video game is: ")
print(video_game_platforms_dict["God of War"])

# 4
print("")
print("after updating the platform of the 6th video game: ")
video_game_platforms_dict["Red Dead Redemption"] = ["Computer"]
print(video_game_platforms_dict)

# 5
print("")
print("after deleting the platform of the 6th video game: ")
del video_game_platforms_dict["Call of Duty: Warzone"]
print(video_game_platforms_dict)

# 6
print("")
last_key = list(video_game_platforms_dict.keys())[-1]
last_value = video_game_platforms_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)