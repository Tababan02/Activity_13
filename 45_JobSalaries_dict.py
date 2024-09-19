job_salaries_dict = {
  "Software Engineer" : "$110,000",
  "Data Scientist" : "$120,000",
  "Registered Nurse" : "$75,000",
  "Marketing Manager" : "$90,000",
  "Graphic Designer" : "$55,000",
  "Accountant" : "$70,000",
  "Web Developer" : "$80,000",
  "Project Manager" : "$85,000",
  "Mechanical Engineer" : "$85,000",
  "Teacher" : "$60,000"
}

# 2
print("The whole dictionary contains: ")
print(job_salaries_dict)

# 3
print("")
print("the salary of the 3rd job is ")
print(job_salaries_dict["Registered Nurse"])
      
# 4
print("")
print("after updating the salary of the 7th job: ")
job_salaries_dict["Web Developer"] = "$100,000"
print(job_salaries_dict)

# 5
print("")
print("after deleting the 9th job from the dictionary: ")
del job_salaries_dict["Mechanical Engineer"]
print(job_salaries_dict)

# 6
print("")
last_key = list(job_salaries_dict.keys())[-1]
last_value = job_salaries_dict[last_key]
print("The last key-value pair is", last_key ,":",last_value)