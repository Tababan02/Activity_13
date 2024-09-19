plant_types_dict = {
    "Oak" : "Tree",
    "Rose" : "Shrub",
    "Basil" : "Herb",
    "Maple" : "Tree",
    "Lavender" : "Herb",
    "Holly" : "Shrub",
    "Sunflower" : "Annual",
    "Cactus" : "Succulent"
} 
# 2
print("The whole dictionary contains: ")
print(plant_types_dict)

# 3
print("")
print("The type of the 5th plant is: ")
print(plant_types_dict ["Lavender"])
      
# 4
print("")
print("after updating the type of the 2nd plant: ")
plant_types_dict["Rose"] = "Annual"
print(plant_types_dict)

# 5
print("")
print("after deleting the 6th plant from the dictionary: ")
del plant_types_dict["Holly"]
print(plant_types_dict)

# 6
print("")
last_key = list(plant_types_dict.keys())[-1]
last_value = plant_types_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)