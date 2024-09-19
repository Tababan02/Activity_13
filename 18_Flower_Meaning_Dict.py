flower_meanings_dict = {
  "Rose" : "Love and passion",
  "Lily" : "Purity and renewal",
  "Tulip" : "Perfect love",
  "Daisy" : "Innocence and purity",
  "Sunflower" : "Adoration and loyalty",
  "Orchid" : "Beauty and strength",
  "Chrysanthemum" : "Friendship and joy",
  "Peony" : "Romance and prosperity"
} 
# 2
print(flower_meanings_dict)

# 3
print("")
print("The meaning of the 5th flower is: ")
print(flower_meanings_dict ['Sunflower'])

# 4 
print("")
print("After updating the meaning of the 7th flower: ")
flower_meanings_dict["Chrysanthemum"] = 'Love'
print(flower_meanings_dict)

# 5
print("")
print("After deleting the 6th flower from the dictionary: ")
del flower_meanings_dict["Orchid"]
print(flower_meanings_dict)

# 7
print("")
last_key = list(flower_meanings_dict.keys())[-1]
last_value = flower_meanings_dict[last_key]
print("The last key-value pair is " , last_key, ":", last_value)