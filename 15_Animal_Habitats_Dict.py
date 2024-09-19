animal_habitats_dict = {
  "Lion": "Savanna",
  "Penguin": "Antarctic Ice",
  "Elephant": "Grasslands",
  "Polar Bear": "Arctic Tundra",
  "Dolphin": "Oceans",
  "Kangaroo": "Australian Bush",
  "Giraffe": "Savanna",
  "Tiger": "Tropical Rainforest",   
}

# 2 
print("The whole dictionary contains: ")
print(animal_habitats_dict)

# 3 
print("")
print("The habitat of the 3rd animal: ")
print(animal_habitats_dict["Elephant"])

# 4
print("")
print("After updating the habitat of the 5th animal: ")
animal_habitats_dict["Dolphin"] = 'Mountains'
print(animal_habitats_dict)

# 5
print("")
print("After deleting the 7th animal from the dictionary: ")
del animal_habitats_dict["Giraffe"]
print(animal_habitats_dict)

# 6
print("")
last_key = list(animal_habitats_dict.keys())[-1]
last_value = animal_habitats_dict[last_key]
print("The last key-value pair is " ,last_value, ":", last_key)
