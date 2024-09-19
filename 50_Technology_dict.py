technology_innovators_dict = {
  "Personal Computer" : "Steve Jobs, Bill Gates",
  "Internet" : "Tim Berners-Lee",
  "Electric Light Bulb" : "Thomas Edison",
  "Telephone" : "Alexander Graham Bell",
  "Automobile" : "Henry Ford",
  "Airplane" : "Wright Brothers",
  "Smartphone" : "Steve Jobs",
  "GPS" : "Roger L. Easton"
}

# 2
print("The whole dictionary contains: ")
print(technology_innovators_dict)

# 3
print("")
print("the  innovator of the 4th technology is ")
print(technology_innovators_dict["Telephone"])
      
# 4
print("")
print("after updating the innovator of the 2nd technology: ")
technology_innovators_dict["Internet"] = "Sandara"
print(technology_innovators_dict)

# 5
print("")
print("after deleting the 6th technology from the dictionary: ")
del technology_innovators_dict ["Airplane"]
print(technology_innovators_dict)

# 6
print("")
last_key = list(technology_innovators_dict.keys())[-1]
last_value = technology_innovators_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)