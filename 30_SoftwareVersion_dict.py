software_versions_dict = {
    "Windows" : "Windows 11",
    "macOS" : "macOS Ventura",
    "Ubuntu" : "Ubuntu 22.04 LTS",
    "Android" : "Android 13",
    "iOS" : "iOS 16",
    "Microsoft Office" : "Office 2021",
    "Photoshop" : "Adobe Photoshop 2023",
    "Chrome" : "Google Chrome 117",
    "Firefox" : "Mozilla Firefox 117",
    "Visual Studio Code" : "VS Code 1.78"
}
    
    
# 2
print("The whole dictionary contains: ")
print(software_versions_dict)

# 3
print("")
print("The version of the 4th software is: ") 
print(software_versions_dict ["Android"])

# 4
print("")
print("after updating the version of the 2nd software:")
software_versions_dict["macOS"] = "Version 13"
print(software_versions_dict)

# 5
print("")
print("after deleting the 5th software from the dictionary: ")
del software_versions_dict["iOS"]
print(software_versions_dict)

# 6
print("")
last_key = list(software_versions_dict.keys())[-1]
last_value = software_versions_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)