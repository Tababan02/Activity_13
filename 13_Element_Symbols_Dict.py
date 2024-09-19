element_symbols_dict = {
    "Hydrogen": "H",
    "Helium": "He",
    "Lithium": "Li",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne",
}

# 2
print("The whole dictionary contains: ")
print(element_symbols_dict)

# 3
print("")
print("The symbol of the 6th element is: ")
print(element_symbols_dict['Carbon'])

# 4
print("")
print("After updating the symbol of the 8th element: ")
element_symbols_dict["Oxygen"] = 'A'
print(element_symbols_dict)

# 5
print("")
print("After deleting 9th element from the dictionary: ")
del element_symbols_dict["Fluorine"]
print(element_symbols_dict)

# 6
print("")
last_key = list(element_symbols_dict.keys())[-1]
last_value = element_symbols_dict[last_key]
print("The last key-value pair is ", last_key, ":" , last_value)
 