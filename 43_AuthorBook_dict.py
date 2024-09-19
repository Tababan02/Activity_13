author_books_dict = {
   "Jane Austen" : "Pride and Prejudice",
    "George Orwell" : "1984",
    "F. Scott Fitzgerald" : "The Great Gatsby",
    "Harper Lee" : "To Kill a Mockingbird",
    "J.K. Rowling" : "Harry Potter and the Sorcerer's Stone",
    "Mark Twain" : "The Adventures of Tom Sawyer",
    "J.R.R. Tolkien" : "The Hobbit",
    "Gabriel Garcia Marquez" : "One Hundred Years of Solitude",
}

# 2
print("the whole dictionary contains: ")
print(author_books_dict)

# 3
print("")
print("The book of the 5th author is ")
print(author_books_dict["J.K. Rowling"])
      
# 4
print("")
print("after updating the book of the 7th author: ")
author_books_dict["J.R.R. Tolkien"] = "The Lord of the Rings"
print(author_books_dict)

# 5
print("")
print("after deleting the 6th author from the dictionary: ")
del author_books_dict["Mark Twain"]
print(author_books_dict)

# 6
print("")
last_key = list(author_books_dict.keys())[-1]
last_value = author_books_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)