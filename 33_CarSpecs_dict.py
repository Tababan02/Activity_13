car_specs_dict = {
   "Tesla Model S" : "Horsepower: 670, Top Speed: 200 mph, Range: 405 miles",
  "Ford Mustang" : "Horsepower: 450, Top Speed: 155 mph", "Engine": "5.0L V8",
  "Chevrolet Corvette" : "Horsepower: 495, Top Speed: 194 mph, Engine: 6.2L V8",
  "Toyota Camry" : "Horsepower: 203, Top Speed: 130 mph, Fuel Economy: 28 mpg city / 39 mpg highway",
  "Honda Accord" : "Horsepower: 192, Top Speed: 130 mph, Fuel Economy: 30 mpg city / 38 mpg highway",
  "BMW M3" : "Horsepower: 473, Top Speed: 155 mph, Engine: 3.0L I6",
"Mercedes-Benz C-Class" : "Horsepower: 255, Top Speed: 130 mph, Engine: 2.0L I4",
  "Subaru Outback" : "Horsepower: 182, Top Speed: 130 mph, AWD: Yes",
  "Volkswagen Golf" : "Horsepower: 228, Top Speed: 155 mph, Fuel Economy: 28 mpg city / 36 mpg highway",
  "Audi A4" : "Horsepower: 201, Top Speed: 130 mph, Engine: 2.0L I4" 
}
  
# 2
print("The whole dictionary contains: ")
print(car_specs_dict)

# 3
print("")
print("The specification of the 4th car model are ")
print(car_specs_dict ["Toyota Camry"])
      
# 4
print("")
print("after updating  the specifications of the 9th car model: ")
car_specs_dict["Volkswagen Gold"] = "Horsepower: 228, Top Speed: 155 mph, Fuel Economy: 30 mpg city / 40 mpg highway"
print(car_specs_dict)

# 5
print("")
print("after deleting the 5th car model from the dictionary.")
del car_specs_dict["Honda Accord"]
print(car_specs_dict)

# 6
print("")
last_key = list(car_specs_dict.keys())[-1]
last_value = car_specs_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)