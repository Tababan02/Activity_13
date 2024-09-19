continent_countries_dict = {
   "Asia": "China, KenyaJapan",
    "Africa": "Nigeria, Kenya, Egypt",
    "North America": "USA, Canada, Mexico",
    "South America": "Brazil, Argentina, Chile",
    "Europe": "Germany, France, Italy",
    "Australia": "Australia, New Zealand, Papua New Guinea"
}
# 2
print("The whole dictionary contains: ")
print(continent_countries_dict)

# 3
print("")
print("The countries of the 4th continent are: ")
print(continent_countries_dict['South America'])

# 4
print("")
print("After Updating the countries of the 5th continent: ")
continent_countries_dict['Europe'] = "Philippines, Korea, China"
print(continent_countries_dict)

# 5
print("")
print("After deleting the 6th continent from the dictionary: ")
del continent_countries_dict["Australia"] 
print(continent_countries_dict)

# 6
print("")
last_key = list(continent_countries_dict.keys())[-1]
last_value = continent_countries_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)

