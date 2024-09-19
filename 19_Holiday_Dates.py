holiday_dates_dict = {
    "New Year's Day" : "January 1",
    "Valentines Day" : "February 14",
    "Easter" : "March 25",
    "Independence Day" : "July 4",
    "Halloween" : "October 31",
    "Thanksgiving" : "November 21",
    "Christmas" : "December 25",
    "New Year's Eve" : "December 31",
    "Labor Day" : "September 9",
    "Memorial Day" : "May 5"
}
# 2
print("The whole dictionary contains: ")
print(holiday_dates_dict)

# 3
print("")
print("The date of the 4th holiday is: ")
print(holiday_dates_dict["Independence Day"])

# 4
print("")
print("after updating the date of the 9th holiday: ")
holiday_dates_dict["Labor Day"] = 'September 2'
print(holiday_dates_dict)

# 5
print("")
print("after deleting the 2nd holiday from the dictionary: ")
del holiday_dates_dict["Valentines Day"]
print(holiday_dates_dict)

# 6
print("")
last_key = list(holiday_dates_dict.keys())[-1]
last_value = holiday_dates_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)