programming_language_dict = {
	"Python" : "Guido van Rossum",
	"Java" : "James Gosling and Mike Sheridan at Sun Microsystems",
	"C" : "Dennis Ritchie and Bell Labs",
	"JavaScript" : "Brendan Eich",
	"C++" : "Bjarne Stroustrup",
	"Ruby" : "Yukihiro Matsumoto",
	"PHP" : "Rasmus Lerdof"
	}

# 2
print("The whole dictionary contains: ") 
print(programming_language_dict)
print("")

# 3
print("The 4th programming language and the developers is: ")
print(programming_language_dict["JavaScript"])
print("")

# 4
print("after updating the 6th prog language in dictionary: ")
programming_language_dict["Ruby"] = "SANDARA"
print(programming_language_dict)
print("")

# 5
print("After deleting the 2nd prog language: ")
del programming_language_dict["Java"]
print(programming_language_dict)
print("")
# 6
last_key = list(programming_language_dict.keys())[-1]
last_value = programming_language_dict[last_key]
print("The last key-value is: ", last_key, ":", last_value)