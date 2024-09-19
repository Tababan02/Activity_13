planet_distances_dict = {
    "Mercury" : "57.91",
    "Venus" : "108.21",
    "Earth" : "149.60",
    "Mars" : "227.92",
    "Jupiter" : "778.57",
    "Saturn" : "1,426.73",
    "Uranus" : "2,870.97",
    "Neptune" : "4,498.25",
}

# 2
print("the whole dictionary contains: ")
print(planet_distances_dict)

# 3
print("")
print("The distance of the 3rd planet is ")
print(planet_distances_dict["Earth"])
      
# 4
print("")
print("after updating  the distance of the 5th planet: ")
planet_distances_dict["Jupiter"] = ['800.43']
print(planet_distances_dict)

# 5
print("")
print("after deleting the 7th planet from the dictionary: ")
del planet_distances_dict["Uranus"]
print(planet_distances_dict)

# 6
print("")
last_key = list(planet_distances_dict.keys())[-1]
last_value = planet_distances_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)