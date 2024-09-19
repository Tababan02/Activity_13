city_landmarks_dict = {
  "Paris" : "Eiffel Tower",
  "New York" : "Statue of Liberty",
  "Rome" : "Colosseum",
  "London" : "Big Ben",
  "Tokyo" : "Tokyo Tower",
  "Sydney" : "Sydney Opera House",
  "Dubai" : "Burj Khalifa",
  "Cairo" : "Pyramids of Giza"
}
# 2
print("The whole dictionary contains: ")
print(city_landmarks_dict)

# 3
print("")
print("The landmark of the 6th city is: ")
print(city_landmarks_dict["Sydney"])
      
# 4
print("")
print("after updating the landmark of the 2nd city: ")
city_landmarks_dict["New York"] = "SUMMIT one"
print(city_landmarks_dict)

# 5
print("")
print("after deleting the 7th city from the dictionary: ")
del city_landmarks_dict["Dubai"]
print(city_landmarks_dict)

# 6
print("")
last_key = list(city_landmarks_dict.keys())[-1]
last_value = city_landmarks_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)