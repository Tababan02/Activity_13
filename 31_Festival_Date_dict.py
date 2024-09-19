festival_dates_dict = {
    "New Year's Day" : "January 1",
    "Diwali" : "October or november",
    "Christmas" : "December 25",
    "Eid al-Fitr" : "August",
    "Thanksgiving" : "November 19",
    "Halloween" : "October 31",
   "Holi" : "March 25",
    "Chinese New Year" : " January or February",
    "Oktoberfest" : "October 6",
    "Valentine's Day" : "February 14"

}   
    
    
# 2
print("The whole dictionary contains: ")
print(festival_dates_dict)

# 3
print("")
print("The date of the 3rd festival is: ")
print(festival_dates_dict["Christmas"]

)# 4
print("")
print("after updating the date of the 7th festival: ")
festival_dates_dict["Holi"] = "September 13"
print(festival_dates_dict)

# 5
print("")
print("after deleting 5th festival from the dictionary: ")
del festival_dates_dict["Thanksgiving"]
print(festival_dates_dict)

# 6
print("")
last_key = list(festival_dates_dict.keys())[-1]
last_value = festival_dates_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)