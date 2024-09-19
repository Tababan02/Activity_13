festival_locations_dict = {
  "Oktoberfest" : "Munich, Germany",
  "Carnival" : "Rio de Janeiro, Brazil",
  "Holi" : "India",
  "Diwali" : "India",
  "Coachella" : "California, USA",
  "Running of the Bulls" : "Pamplona, Spain",
  "Harbin Ice Festival" : "Harbin, China",
  "Tomorrowland" : "Boom, Belgium",
  "Burning Man" : "Black Rock City, Nevada, USA",
  "Chinese New Year" : "China and worldwide",

}

# 2
print("The whole dictionary contains: ")
print(festival_locations_dict)

# 3
print("")
print("the  location of the 4th festival is ")
print(festival_locations_dict["Diwali"])
      
# 4
print("")
print("after updating the location of the 6th festival: ")
festival_locations_dict["Running of the Bulls"] = "Philippines"
print(festival_locations_dict)

# 5
print("")
print("after deleting the 2nd festival from the dictionary: ")
del festival_locations_dict["Carnival"]
print(festival_locations_dict)

# 6
print("")
last_key = list(print(festival_locations_dict.keys())[-1]
last_value = (festival_locations_dict)[last_key]
print("The last key-value pair is ", last_key ,":",last_value)