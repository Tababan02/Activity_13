athlete_achievements_dict = {
    "Michael Phelps" : "23 Olympic gold medals in swimming",
    "Usain Bolt" : "World record holder in 100m and 200m sprints",
    "Serena Williams" : "23 Grand Slam singles titles in tennis",
    "Tom Brady" : "7 Super Bowl championships in American football",
    "Michael Jordan" : "6 NBA championships and 5 MVP awards",
    "Roger Federer" : "20 Grand Slam singles titles in tennis",
    "Simone Biles" : "7 Olympic medals, including 4 golds in gymnastics",
    "Lionel Messi" : "7 Ballon d'Or awards in football (soccer)"
}

# 2
print("The whole dictionary contains: ")
print(athlete_achievements_dict)

# 3
print("")
print("The achievement of the 5th athlete are: ")
print(athlete_achievements_dict["Michael Jordan"])
  
# 4
print("")
print("after updating the achievement of the 3rd athlete: ")
athlete_achievements_dict["Serena Willian"] = ["champion in grand slam 2024"]
print(athlete_achievements_dict)

# 5
print("")
print("after deleting the 7th athlete from the dictionary.")
del athlete_achievements_dict["Simone Biles"]
print(athlete_achievements_dict)

# 6
print("")
last_key = list(athlete_achievements_dict.keys())[-1]
last_value = athlete_achievements_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)