dog_breeds_dict = {
    "Chihuahua" : "Small",
    "Beagle" : "Medium",
    "Golden Retriever" : "Large",
    "Poodle" : "Medium",
    "Dachshund" : "Small",
    "Bulldog" : "Medium",
    "Siberian Husky" : "Large",
    "Shih Tzu" : "Small",
    "Boxer" : "Large",
    "Cocker Spaniel" : "Medium",
}
  
# 2
print("The whole dictionary contains: ")
print(dog_breeds_dict)

# 3
print("")
print("The size of the 5th breed is ")
print(dog_breeds_dict ["Dachshund"])
      
# 4
print("")
print("after updating the size of the 8th breed: ")
dog_breeds_dict["Shih Tzu"] = "Medium"
print(dog_breeds_dict)

# 5
print("")
print("after updating the 6th breed from the dictionary: ")
del dog_breeds_dict["Bulldog"]
print(dog_breeds_dict)

# 6
print("")
last_key = list(dog_breeds_dict.keys())[-1]
last_value = dog_breeds_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)