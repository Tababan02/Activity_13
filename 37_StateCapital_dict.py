state_capitals_dict = {
  "Alabama" : "Montgomery",
  "Alaska" : "Juneau",
  "Arizona" : "Phoenix",
  "Arkansas" : "Little Rock",
  "California" : "Sacramento",
  "Colorado" : "Denver",
  "Connecticut" : "Hartford",
  "Delaware" : "Dover",
  "Florida" : "Tallahassee",
  "Georgia" : "Atlanta",
} 
# 2
print("The whole dictionary contains: ")
print(state_capitals_dict)

# 3
print("")
print("The capital of the 4th state is ")
print(state_capitals_dict["Arkansas"])
      
# 4
print("")
print("after updating the capital of the 9th state: ")
state_capitals_dict["Florida"] = "Manila"
print(state_capitals_dict)

# 5
print("")
print("after deleting the 7th state from the dictionary: ")
del state_capitals_dict["Connecticut"]
print(state_capitals_dict)

# 6
print("")
last_key = list(state_capitals_dict.keys())[-1]
last_value = state_capitals_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)