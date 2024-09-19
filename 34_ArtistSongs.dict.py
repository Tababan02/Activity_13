artist_songs_dict = {
   "Adele" : "Rolling in the Deep",
  "Taylor Swift" : "Shake It Off",
  "Drake" : "God's Plan",
  "Ed Sheeran" : "Shape of You",
  "Beyoncé" : "Crazy in Love",
  "Bruno Mars" : "Uptown Funk",
  "Billie Eilish" : "Bad Guy",
  "Justin Bieber" : "Sorry",
  "Katy Perry" : "Firework",
  "Post Malone" : "Circles",
}
  
# 2
print("The whole dictionary contains: ")
print(artist_songs_dict)

# 3
print("")
print("The top song of the 3rd artist is ") 
print(artist_songs_dict ["Drake"])

# 4
print("")
print("After updating the top song of the 6th artist: ")
artist_songs_dict["Bruno Mars"] = "Thats what i like"
print(artist_songs_dict)

# 5
print("")
print("after deleting the 7th artist from the dictionary: ")
del artist_songs_dict["Katy Perry"]
print(artist_songs_dict)

# 6
print("")
last_key = list(artist_songs_dict.keys())[-1]
last_value = artist_songs_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)