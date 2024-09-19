car_brands_dict = {
	"Toyota" : "Japan",
	"Ford" : "United States",
	"Honda" : "Japan",
	"BMW" : "Germany",
	"Mercedes-Benz" : "Germany",
	"Nissan" : "Japan",
	"Hyundai" : "South Korea",
	"Subaru" : "japan",
	"Audi" : "Germany",
	"Tesla" : "United States"
	}

# 2
print(car_brands_dict)

# 3
print("")
print("The 3rd car brand is: ")
print(car_brands_dict["Honda"])
print(car_brands_dict)

# 4
print("")
print("After updating the country of origin of the 7th car brand ")
car_brands_dict["Hyundai"] = 'Philippines'
print(car_brands_dict)

# 5
print("")
print("After deleting the 8th car brand in the dictionary: ")
del car_brands_dict['Subaru']
print(car_brands_dict)

# 6
print("")
last_key = list(car_brands_dict.keys())[-1]
last_value = car_brands_dict[last_key]
print("The last key-value is : " ,last_key, ":", last_value)