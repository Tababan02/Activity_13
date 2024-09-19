coffee_types_dict = {
  "Espresso" : "Strong, concentrated coffee brewed under pressure.",
  "Americano" : "Espresso diluted with hot water.",
  "Cappuccino" : "Espresso with steamed milk and milk foam.", 
  "Latte" : "Espresso with steamed milk, topped with foam.",
  "Mocha" : "Latte with chocolate syrup and whipped cream.",
  "Macchiato" : "Espresso 'stained' with a bit of milk.",
  "Flat White" : "Strong coffee with velvety microfoam.",
  "Cold Brew" : "Coffee brewed cold for a smooth flavor.",
  "Affogato" : "Espresso poured over vanilla ice cream.",
  "Turkish Coffee" : "Finely ground coffee brewed unfiltered."
}

# 2
print("The whole dictionary contains: ")
print(coffee_types_dict)

# 3
print()
print("The description of the 4th type of coffee is: ") 
print(coffee_types_dict["Latte"])
      
# 4
print("")
print("after updating the description of the 8th type of coffee: ")
coffee_types_dict["Cold Brew"] = "Brewed with cold rather than hot water"
print(coffee_types_dict)

# 
print("")
print("after deleting the 5th type of coffee from the dictionary: ")
del coffee_types_dict["Mocha"]
print(coffee_types_dict)

# 6
print("")
last_key = list(coffee_types_dict.keys())[-1]
last_value = coffee_types_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)