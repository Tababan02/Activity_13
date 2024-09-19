animal_sounds_dict = {
	"Cat": "Meow",
	"Dolphin": "click",
	"Zebra": "Whistle",	
	"Rooster": "Cluck",
	"Pig": "Snort" ,
	"Penguin": "Honk",
	"Leopard": "Growl",
	"Alligator": "Hiss"
}

# 2
print("The whole Dictionary Contains: ")
print(animal_sounds_dict)

# 3
print("")
print("The sounds of the 4th animal is: ")
print(animal_sounds_dict["Rooster"])

# 4
print("")
print("After Updating the Dictionary")
animal_sounds_dict["Leopard"] = 'Swiss'
print(animal_sounds_dict)

# 5
print("")
print("After deleting the 5th animal: ")
del animal_sounds_dict["Pig"]
print(animal_sounds_dict)
print("")


# 6
last_key = list(animal_sounds_dict.keys())[-1]
last_value = animal_sounds_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)