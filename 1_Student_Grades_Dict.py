student_grades_dict = {
	"Student1" : "80",
	"Student2" : "85",
	"Student3": "90",
	"Student4" : "95",
	"Student5" : "97"
}

# 2
print("")
print("The whole Dictionary")
print(student_grades_dict)

# 3
print("")
print("Grade of the third student is ",student_grades_dict['Student3'])

# 4
print("")
student_grades_dict['Student2'] = 'A'
print("After Updating: ")
print(student_grades_dict)

# 5
print("")
del student_grades_dict['Student5']
print("After Deleting: ")
print(student_grades_dict)



# 6
print("")
last_key = list(student_grades_dict.keys())[-1]
last_value = student_grades_dict[last_key]
print("The last key-value is ", last_key, ":" ,last_value)