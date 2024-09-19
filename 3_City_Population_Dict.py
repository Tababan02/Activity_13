city_population_dict = {
	"Quezon City": "2,761,720",
	"Manila" : "1,600,000",
	"Caloocan City" : "1,500,000",
	"Davao" : "1,212,504",
	"Cebu City" : "798,634",
	"Taguig" : "644,473",
	"Pasig City" : "617,301",
	"Las Pinas" : "590,000",
	"Antipolo" : "549,543",
	"Makati City" : "510,383" 
}

# 2
print("The whole dictionary contains: ")
print(city_population_dict)

# 3
print("")
print("The population of the 6th city is: ")
print(city_population_dict['Taguig'])

# 4
print("")
print("After updating the 3rd city: ")
city_population_dict['Caloocan'] = '1,800,000'
print(city_population_dict)


# 5
print("")
print("After deleting the 9th city ")
del city_population_dict["Antipolo"]
print(city_population_dict)
print("")


# 6
last_key = list(city_population_dict.keys())[-1]
last_value = city_population_dict[last_key]
print("The last key-value is ", last_key, ":", last_value)