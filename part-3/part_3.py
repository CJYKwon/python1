my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_list = [
    {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
    },
    {
    "title": "Think and Grow Rich",
    "author": "Napoleon Hill",
    "year": 1937,
    "rating": 4.5,
    "pages": 320
    },
    {
    "title": "The Subtle Art Of Not Giving a F*ck",
    "author": "Mark Manson",
    "year": 2016,
    "rating": 4.58,
    "pages": 374
    }
]
# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(book_dictionary):

    book_string = f"{book_dictionary['title']} was written by {book_dictionary['author']}, published in the year {book_dictionary['year']}, has a rating of {book_dictionary['rating']} and consists of {book_dictionary['pages']}."

    return book_string

print(book_parser(my_book))



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_book_title(book_ditionary):
    book_title = book_ditionary["title"]
    return book_title

print(get_book_title(my_book))

def get_book_author(book_ditionary):
    book_author = book_ditionary["author"]
    return book_author

print(get_book_author(my_book))

def get_book_pages(book_ditionary):
    book_pages = book_ditionary["pages"]
    return book_pages

print(get_book_pages(my_book))




# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def book_parser_from_list(book_dictionary_list):
    for book_dictionary in book_dictionary_list:
        print(book_parser(book_dictionary))

book_parser_from_list(my_book_list)

def get_list_of_authors(book_dictionary_list):
    author_set = set()

    for book_dictionary in book_dictionary_list:
        author_set.add(book_dictionary["author"])

    return author_set

print(get_list_of_authors(my_book_list))

def get_total_pages(book_dictionary_list):
    total_pages = 0

    for book_dictionary in book_dictionary_list:
        total_pages += book_dictionary["pages"]

        return total_pages
    
print(get_total_pages(my_book_list))