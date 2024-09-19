app_store_ratings_dict = {
    "WhatsApp" : "4.7",
    "Instagram" : "4.6",
    "Spotify" : "4.5",
    "Google Maps" : "4.8",
    "Zoom" : "4.6",
    "TikTok" : "4.7",
    "Facebook" : "4.1",
    "Twitter" : "4.4",
    "Snapchat" : "4.5",
    "Netflix" : "4.6",
}

# 2
print("The whole dictionary contains: ")
print(app_store_ratings_dict)

# 3
print("")
print("The rating of the 6th app is: ")
print(app_store_ratings_dict['TikTok'])

# 4
print("")
print("After updating the rating of the 8th app: ")
app_store_ratings_dict['Twitter'] = ['5.00']
print(app_store_ratings_dict)

# 5
print("")
print("after deleting the 9th app from the dictionary: ")
del app_store_ratings_dict["Snapchat"]
print(app_store_ratings_dict)

# 6
print("")
last_key = list(app_store_ratings_dict.keys())[-1]
last_value = app_store_ratings_dict[last_key]
print("The last key-value pair is ", last_key, ":",last_value)