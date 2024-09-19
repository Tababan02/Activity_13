space_missions_dict = {
  "Apollo 11": "1969",
  "Voyager 1": "1977",
  "Space Shuttle Columbia": "1981",
  "Mars Rover Spirit": "2004",
  "International Space Station (ISS)": "1998"
}

# 2
print("The whole dictionary contains: ")
print(space_missions_dict)

# 3
print("")
print("the year of the 3rd mission: ")
print(space_missions_dict['Space Shuttle Columbia'])

# 4
print("")
print("After updating the year of the 2nd mission: ")
space_missions_dict["Voyager 1"] = "2024"
print(space_missions_dict)

# 5
print("")
print("After deleting the 4th mission from the dictionary.")
del space_missions_dict['Mars Rover Spirit']
print(space_missions_dict)


# 6
print("")
last_key = list(space_missions_dict.keys())[-1]
last_value = space_missions_dict[last_key]
print("The last key-value pair is ", last_value, ":",last_key)