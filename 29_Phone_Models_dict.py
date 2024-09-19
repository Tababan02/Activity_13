phone_models_dict = {
    "iPhone 14" : "Apple",
    "Galaxy S23" : "Samsung",
    "Pixel 7" : "Google",
    "OnePlus 11" : "OnePlus", 
    "Xperia 1 IV" : "Sony",
    "Mi 13" : "Xiaomi",
    "Nokia G400" : "Nokia",
    "Vivo X90" : "Vivo",
    "OPPO Find X5" : "OPPO",
    "Motorola Edge 30" : "Motorola"

}
    
# 2
print("The whole dictionary contains: ")
print(phone_models_dict)

# 3
print("")
print("The manufacturer of the 2nd phone model is: ")
print(phone_models_dict ["Galaxy S23"])

      
# 4
print("")
print("after updating the manufacturer of the 8th phone model: ")
phone_models_dict["Vivo X90"] = "Google"
print(phone_models_dict)

# 5
print("")
print("after deleting the 6th phone model from the dictionary.")
del phone_models_dict["Mi 13"]
print(phone_models_dict)

# 6
print("")
last_key = list(phone_models_dict.keys())[-1]
last_value = phone_models_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)