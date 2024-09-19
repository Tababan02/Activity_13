space_telescope_missions_dict = {
  "Hubble Space Telescope" : "Deep space observation.",
  "Chandra X-ray Observatory" : "X-ray study of high-energy regions.",
  "Kepler Space Telescope" : "Exoplanet search.",
  "James Webb Space Telescope" : "Infrared observation of stars and galaxies.",
  "Spitzer Space Telescope" : "Infrared study of celestial objects."
} 

# 2
print("The whole dictionary contains: ")
print(space_telescope_missions_dict)

# 3
print("")
print("The missopm of the 1st Telescope is ")
print(space_telescope_missions_dict["Hubble Space Telescope"])
      
# 4
print("")
print("after updating the mission of the 1st telescope: ")
space_telescope_missions_dict["Hubble Space Telescope"] = "Magnify"
print(space_telescope_missions_dict)

# 5
print("")
print("after deleting the 4th telescope from the dictionary: ")
del space_telescope_missions_dict["James Webb Space Telescope"]
print(space_telescope_missions_dict)

# 6
print("")
last_key = list(space_telescope_missions_dict.keys())[-1]
last_value = space_telescope_missions_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)