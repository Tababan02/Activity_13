fruit_colors_dict = {
	"Apple" : "Red",
	"Banana" : "Yellow",
	"Orange" : "Orange",
	"Grapes" : "Green",
	"Lemon" : "Yellow",
	"Strawberry" : "Red",
	"Watermelon" : "Green",
	"Blueberry" : "Blue"
}

# 2
print("The whole dictionaries contains: ")
print(fruit_colors_dict)

# 3
print("")
print("The color of the 6th fruit is: ", ['Strawberry'])
print(fruit_colors_dict)

# 4
print("")
print("After Updating the color of the 4th fruit: ")
fruit_colors_dict["Grapes"] = 'Red'
print(fruit_colors_dict)

# 5
print("")
print("After Delete the 7th fruit from the dictionary ")
del fruit_colors_dict['Watermelon']
print(fruit_colors_dict)

#6
print("")
last_key = list(fruit_colors_dict.keys())[-1]
last_value = fruit_colors_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)
