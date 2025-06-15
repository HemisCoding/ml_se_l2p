## Composition vs Inheritance
# Exercise 6: Author and Book

# Define Author with name and email
# Define Book with title, author (Author object), and price

# In Book, add a method `get_author_email()` that uses the Author object

# Show how composition is used instead of inheritance here.


class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Book:
    def __init__(self, title, author, price):
        if not isinstance(author, Author):
            raise TypeError("author should be in Author class!!!")
        self.title = title
        self.author = author
        self.price = price

    def get_author_mail(self):
        print(f"Author mail for {self.title} is: {self.author.email}")

    
author1 = Author("creanga", "creanga@gmail.com")
book1 = Book("amintiri din copilarie", author1, 35)
print(book1.get_author_mail())


    