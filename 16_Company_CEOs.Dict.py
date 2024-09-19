company_ceos_dict = {
    "Apple": "Tim Cook",
    "Microsoft": "Satya Nadella",
    "Amazon": "Andy Jassy",
    "Google (Alphabet Inc.)": "Sundar Pichai",
    "Facebook": "Mark Zuckerberg",
    "Tesla": "Elon Musk",
    "Berkshire Hathaway": "Warren Buffett",
    "IBM": "Arvind Krishna",
    "Oracle": "Safra Catz",
    "Coca-Cola": "James Quincey",
}

# 2
print("The whole dictionary contains: ")
print(company_ceos_dict)

# 3
print("")
print("the CEO of the 6th company: ")
print(company_ceos_dict["Tesla"])

# 4
print("")
print("after updating the CEO of the 3rd company: ")
company_ceos_dict["Amazon"] = "Sandara"
print(company_ceos_dict)

# 5
print("")
print("After deleting the 9th company from the dictionary: ")
del company_ceos_dict['Oracle']
print(company_ceos_dict)

# 6
print("")
last_key = list(company_ceos_dict.keys())[-1]
last_value = company_ceos_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)