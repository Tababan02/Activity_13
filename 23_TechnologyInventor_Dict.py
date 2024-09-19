technology_inventors_dict = {
    "Telephone" : "Alexander Graham Bell",
    "Light Bulb" : "Thomas Edison",
    "Internet" : "Tim Berners-Lee",
    "Radio" : "Guglielmo Marconi",
    "Airplane" : "Wright Brothers",
    "Computer" : "Charles Babbage"
}
# 2
print(technology_inventors_dict)

# 3
print("")
print("The inventor of the 4th genre is: ")
print(technology_inventors_dict["Radio"])
      
# 4
print("")
print("After updating the inventor of the 2nd technology: ")
technology_inventors_dict["Light Bulb"] = ['Sandara']
print(technology_inventors_dict)

# 5
print("")
print("After deleting the 6th technology from the dictionary: ")
del technology_inventors_dict["Computer"]
print(technology_inventors_dict)

# 6
print("")
last_key = list(technology_inventors_dict.keys())[-1]
last_value = technology_inventors_dict[last_key]
print("The last key-value pair is ", last_key, ":",last_value)