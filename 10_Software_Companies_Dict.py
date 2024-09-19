software_companies_dict = {
	"Microsoft": "Redmond, Washington, USA",
	"Apple": "Cupertino, California, USA",
	"Google": "Mountain View, California, USA",
	"Oracle": "Austin, Texas, USA",
	"SAP": "Walldorf, Germany",
	"IBM": "Armonk, New York, USA",
	"Salesforce": "San Francisco, California, USA",
	"Adobe": "San Jose, California, USA",
	"Intuit": "Mountain View, California, USA",
	"VMware": "Palo Alto, California, USA"
}

# 2
print("The whole dictionary contains: ")
print(software_companies_dict)

# 3
print("")
print("The headquarters of the 3rd company is: ")
print(software_companies_dict['Google'])
print(software_companies_dict)

# 4
print("")
print("After updating the headquarters of the 8th company: ")
software_companies_dict["Adobe"] = 'Manila'
print(software_companies_dict)

# 5
print("")
print("After deleting the 9th company from the dictionary: ")
del software_companies_dict['Intuit']
print(software_companies_dict)

# 6
print("")
last_key = list(software_companies_dict.keys())[-1]
last_value = software_companies_dict[last_key]
print("The last key-value is ",last_key, ":", last_value)