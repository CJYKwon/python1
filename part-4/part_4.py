### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# title = input("\nTitle of the book to add: ")
# author = input("Author of the book: ")
# year = input("Year the book was published: ")
# rating = input("Rating of the book: ")
# pages = input("Total page count: ")

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# title = input("\nTitle of the book to add: ")
# author = input("Author of the book: ")
# year = int(input("Year the book was published: "))
# rating = float(input("Rating of the book: "))
# pages = int(input("Total page count: "))


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# title = input("\nTitle of the book to add: ")
# author = input("Author of the book: ")
# try:
#     year = int(input("Year the book was published: "))
# except:
#     year = int(input("Input number please: "))
# try:
#     rating = float(input("Rating of the book: "))
# except:
#     rating = int(input("Input number please: "))
# try:
#     pages = int(input("Total page count: "))
# except:
#     pages = int(input("Input number please: "))


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# def main_menu(books_source):
#     choice = input("Choose 1 to add a book. Choose 2 to see all your books. Choose 3 to exit. - ")

#     if choice == "1":
#         books_source.append(create_new_book())
#     elif choice == "2":
#         print_all_books(books_source)
#     elif choice == "3":
#         print("\nBye")
#         active = False
#     else:
#         print("\nA choice is required!.\n")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

current_books = [
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

def create_new_book():
    title = input("\nTitle of the book to add: ")
    author = input("Author of the book: ")
    try:
        year = int(input("Year the book was published: "))
    except:
        year = int(input("Input number please: "))
    try:
        rating = float(input("Rating of the book: "))
    except:
        rating = int(input("Input number please: "))
    try:
        pages = int(input("Total page count: "))
    except:
        pages = int(input("Input number please: "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

def print_all_books(list_of_books):

    print("\nHere is your list of books...\n")

    for book in list_of_books:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

def main_menu(books_source):

    active = True
    
    while active:
        choice = input("Choose 1 to add a book. Choose 2 to see all your books. Choose 3 to exit. - ")

        if choice == "1":
            books_source.append(create_new_book())
        elif choice == "2":
            print_all_books(books_source)
        elif choice == "3":
            print(f"\nTotal of {len(books_source)} books.\n")
        elif choice == "4":
            print(f"\nPage count totals {sum([x['pages'] for x in books_source])} pages!\n")
        elif choice == "5":
            print("\nBye")
            active = False
        else:
            print("\nA choice is required!.\n")

main_menu(current_books)