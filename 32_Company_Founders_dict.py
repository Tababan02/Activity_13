company_founders_dict = {
    "Apple" : "Steve Jobs, Steve Wozniak, Ronald Wayne",
    "Microsoft" : "Bill Gates, Paul Allen",
    "Amazon" : "Jeff Bezos",
    "Google" : "Larry Page, Sergey Brin",
    "Facebook" : "Mark Zuckerberg, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, Chris Hughes",
    "Tesla" : "Elon Musk, JB Straubel, Martin Eberhard, Marc Tarpenning, Ian Wright",
    "Alibaba" : "Jack Ma",
    "IBM" : "Charles Ranlett Flint",
}   
    
# 2
print(company_founders_dict)

# 3
print("")
print("Thefounder of the 6th company is ")
print(company_founders_dict ["Tesla"])
      
# 4
print("")
print("after updating the founder of the 2nd company: ")
company_founders_dict["Microsoft"] = "SANDARA"
print(company_founders_dict)
# 5
print("")
print("after deleting the 8th company from the dictionary: ")
del company_founders_dict["IBM"]
print(company_founders_dict) 

# 6
print("")
last_key = list(company_founders_dict.keys())[-1]
last_value = company_founders_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)