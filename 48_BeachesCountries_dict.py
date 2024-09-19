beaches_countries_dict = {
  "Copacabana Beach" : "Brazil",
  "Bondi Beach" : "Australia",
  "Waikiki Beach" : "USA",
  "Playa del Carmen" : "Mexico",
  "Phra Nang Beach" : "Thailand",
  "Whitehaven Beach" : "Australia",
  "Anse Source d'Argent" : "Seychelles",
  "Malibu Beach" : "USA"
}

# 2
print("The whole dictionary contains: ")
print(beaches_countries_dict)

# 3
print("")
print("the country of the 3rd beach is ")
print(beaches_countries_dict["Waikiki Beach"])
      
# 4
print("")
print("after updating the country of the 6th beach: ")
beaches_countries_dict["Whitehaven Beach"] = "Philippines"
print(beaches_countries_dict)

# 5
print("")
print("after deleting the 5th beach from the dictionary: ")
del beaches_countries_dict["Phra Nang Beach"]
print(beaches_countries_dict)

# 6
print("")
last_key = list(beaches_countries_dict.keys())[-1]
last_value = beaches_countries_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)