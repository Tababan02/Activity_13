currency_symbols_dict = {
    "US Dollar" : "$",
    "Euro" : "€",
    "British Pound" : "£",
    "Japanese Yen" : "¥",
    "Swiss Franc" : "CHF",
    "Canadian Dollar" : "C$",
    "Australian Dollar" : "A$",
    "Chinese Yuan" : "¥",
    "Indian Rupee" : "₹",
    "Brazilian Real" : "R$",
}
# 2
print(currency_symbols_dict)

# 3
print("")
print("the inventor of the 5th genre is ",["Swiss Franc"])
      
# 4
print("")
print("After updating the symbol of the 9th currency :")
currency_symbols_dict["Indian Rupee"] = ['&']
print(currency_symbols_dict)

# 5
print("")
print("After deleting the 3rd currency from the dictionary: ")
del currency_symbols_dict["British Pound"]
print(currency_symbols_dict)

# 6
print("")
last_key = list(currency_symbols_dict.keys())[-1]
last_value = currency_symbols_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)