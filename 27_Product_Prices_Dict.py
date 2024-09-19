product_prices_dict = {
    "Laptop" : "$999.99",
    "Smartphone" : "$799.99",
    "Headphones" : "$199.99",
    "Smartwatch" : "$299.99",
    "Tablet" : "$499.99",
    "Bluetooth Speaker" : "$149.99",
    "Camera" : "$1,299.99",
    "Gaming Console" : "$399.99",
    "External Hard Drive" : "$89.99",
    "Fitness Tracker" : "$129.99",
}

# 2
print("The whole dictionary contains:")
print(product_prices_dict)

# 3
print("")
print("The price of the 4th product is: ")
print(product_prices_dict["Smartwatch"])
      
# 4
print("")
print("After updating the price of the 9th product: ")
product_prices_dict["External Hard Drive"] = ["$100.00"]
print(product_prices_dict)

# 5
print("")
print("after deleting the 6th product from the dictionary: ")
del product_prices_dict["Bluetooth Speaker"]
print(product_prices_dict)

# 6
print("")
last_key = list(product_prices_dict.keys())[-1]
last_value = product_prices_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)