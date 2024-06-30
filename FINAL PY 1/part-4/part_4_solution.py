

current_books = [
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.5,
        "pages": 309
    },
    {
        "title": "Twilight",
        "author": "Stephenie Meyer",
        "year": 2005,
        "rating": 3.6,
        "pages": 498
    },
    {
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "year": 2012,
        "rating": 4.2,
        "pages": 313
    },
    {
        "title": "Divergent",
        "author": "Veronica Roth",
        "year": 2011,
        "rating": 4.2,
        "pages": 487
    }
]

def create_new_book():
    title = input("\nWhat is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type a number? - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = int(input("Please type a number? - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please type a number? - "))


    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

def print_all_books(list_of_books):

    print("\nHere are all your books...\n")

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
        choice = input("\nChoose 1 to add a book...\nChoose 2 to see all your books...\nChoose 3 to see a count of your books...\nChoose 4 to see a count of the pages of your books...\nChoose 5 to exit.\nType here: ")

        if choice == "1":
            books_source.append(create_new_book())
        elif choice == "2":
            print_all_books(books_source)
        elif choice == "3":
            print(f"\nYou have a total of {len(books_source)} books.\n")
        elif choice == "4":
            print(f"\nYour books have a total of {sum([x['pages'] for x in books_source])} pages!\n")
        elif choice == "5":
            print("\nGoodbye")
            active = False
        else:
            print("\nSorry, please type a number for one of the options.\n")

main_menu(current_books)