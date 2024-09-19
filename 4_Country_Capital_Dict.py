 country_capital_dict = {
	"Russia" : "Moscow",
	"United Kingdom" : "London",
	"Germany" : "Berlin",
	"Spain" : "Madrid",
	"Ukraine" : "Kiev",
	"Italy" : "Rome",
	"France" : "Paris",
	"Belarus" : "Minsk",
	"Austria" : "Vienna",
	"Romania" : "Bucharest",
	"Poland" : "Warsaw", 
	"Hungary" : "Budapest" 
}

# 2
print("The whole dictionary contains: ")
print(country_capital_dict)
print("")

# 3
print("The capital of the 5th country is ")
print(country_capital_dict['Ukraine'])
print("")

# 4
print("After updating the 8th country: ")
country_capital_dict["Belarus"] = "Manila"
print(country_capital_dict)
print("")
# 5
print("After deleting the 11th country: ")
del country_capital_dict["Poland"]
print(country_capital_dict)
print("")

# 6
last_key = list(country_capital_dict.keys())[-1]
last_value = country_capital_dict[last_key]
print("The last key-value is: ", last_key, ":",last_value)

