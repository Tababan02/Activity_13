historical_events_dict ={
  "American Declaration of Independence" : 1776,
  "French Revolution" : 1789,
  "World War I Begins" : 1914,
  "World War II Begins" : 1939,
  "Moon Landing" : 1969,
  "Fall of the Berlin Wall" : 1989,
  "September 11 Attacks" : 2001,
  "COVID-19 Pandemic Declared" : 2020,
}   
  
# 2
print("The whole dictionary contains: ")
print(historical_events_dict)

# 3
print("")
print("The year of the 2nd event is: ")
print(historical_events_dict["French Revolution"])

# 4
print("")
print("after updating the year of the 7th event: ")
historical_events_dict["September 11 attacks"] = "2002"
print(historical_events_dict)

# 5
print("")
print("after deleting the 5th event from the dictionary: ")
del historical_events_dict["Moon Landing"]
print(historical_events_dict)

# 6
print("")
last_key = list(historical_events_dict.keys())[-1]
last_value = historical_events_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)