book_authors_dict = {
	"Pride and Prejudice" : "Jane Austen",
	"1984" : "George Orwell",
	"The Great Gatsby" : "F. Scott Fitzgerald",
	"Moby-Dick" : "Herman Melville",
	"To kill a mockingbird" : "Harper Lee",
	"The catcher in the Rye" : "J.D. Salinger",
	"The Adventures of Huckleberry Finn" : "Mark Twain",
	"Brave New World" : "Aldous Huxley",
	"The Picture of Dorian Gray" : "Oscar Wilde",
	"Fahrenheit 451" : "Ray Bradbury",
	"The Odyssey" : "Homer",
	"Frankenstein" : "Mary Shelley"
}

# 2
print("The whole dictionary contains; ")
print(book_authors_dict)

# 3
print("")
print("The author of the 9th book:  ")
print(book_authors_dict['The Picture of Dorian Gray'])
print(book_authors_dict)

# 4
print("")
print("After updating the author of the 5th book: ")
book_authors_dict["To kill a mockingbird"] = 'SANDARA'
print(book_authors_dict)

# 5
print("")
print("After deleting the 3rd book from the dictionary.")
del book_authors_dict['The Great Gatsby']
print(book_authors_dict)

# 5
print("")
last_key = list(book_authors_dict.keys())[-1]
last_value = book_authors_dict[last_key]
print("The last key-value is:", last_key, ":", last_value)

