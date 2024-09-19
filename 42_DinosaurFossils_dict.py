dinosaur_fossils_dict = {
    "Tyrannosaurus Rex" : "North America",
    "Triceratops" : "North America",
    "Brachiosaurus" : "North America, Africa",
    "Velociraptor" : "Mongolia",
    "Stegosaurus" : "North America",
    "Spinosaurus" : "North Africa",
    "Ankylosaurus" : "North America",
} 

# 2
print("The whole dictionary contains: ")
print(dinosaur_fossils_dict)

# 3
print("")
print("The location of the 4th dinousaur's fossils: ") 
print(dinosaur_fossils_dict["Velociraptor"])

# 4
print("")
print("after updating the location of the 2nd dinosaur's fossils: ")
dinosaur_fossils_dict["Triceratops"] = "Philippines"
print(dinosaur_fossils_dict)

# 5
print("")
print("after deleting the 6th dinosaur from the dictionary: ")
del dinosaur_fossils_dict["Spinosaurus"]
print(dinosaur_fossils_dict)

# 6
print("")
last_key = list(dinosaur_fossils_dict.keys())[-1]
last_value = dinosaur_fossils_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)