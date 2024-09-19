university_courses_dict = {
	"Harvard University": "Law, Economics",
	"Stanford University": "Psychology",
	"MIT": "Engineering",
	"UC Berkeley": "Environmental Science",
	"Oxford": "Philosophy, Literature",
	"Cambridge": "Mathematics, Engineering",
	"Columbia": " Business",
	"University of Chicago" : "Economics Law",
	"Yale": "Drama, History,",
	"Caltech": "Astrophysics"
}

# 2
print("The whole dictionary contains: ")
print(university_courses_dict)

# 3
print("")
print("The course of the 3rd university is ")
university_courses_dict["UC Berkeley"]
print(university_courses_dict)

# 4
print("")
print("After updating the course of the 5th university.")
university_courses_dict["Cambridge"] = "BSIT"
print(university_courses_dict)

# 5
print("")
print("After Deleting the 7th university from the dictionary.")
del university_courses_dict["University of Chicago"]
print(university_courses_dict)

# 6
print("")
last_key = list(university_courses_dict.keys())[-1]
last_value = university_courses_dict[last_key]
print("The last value-key pair is ", last_key, ":", last_value)	