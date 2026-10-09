
class Book_class:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = 0

    def add_book(self):
        self.book_id = input("Enter book ID: ")
        self.book_title = input("Enter book title: ")
        self.author_id = input("Enter author ID: ")
        self.publisher = input("Enter publisher: ")
        self.year_of_publication = int(input("Enter year of publication: "))

    def display_book(self):
        print("---Book info---")
        print("Book ID:", self.book_id)
        print("Book title:", self.book_title)
        print("Author ID:", self.author_id)
        print("Publisher:", self.publisher)
        print("Year of publication:", self.year_of_publication)


class Author_class:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailid = ""

    def add_author(self):
        self.author_id = input("Enter author ID: ")
        self.author_name = input("Enter author name: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter country: ")
        self.phone = input("Enter phone: ")
        self.emailid = input("Enter email: ")

    def display_author(self):
        print("---Author info---")
        print("Author ID:", self.author_id)
        print("Author name:", self.author_name)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone:", self.phone)
        print("Email:", self.emailid)


class User_class:
    def __init__(self):
        self.user_id = ""
        self.name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.emailid = ""
        self.booksborrowed = []

    def add_user(self):
        self.user_id = input("Enter user ID: ")
        self.name = input("Enter user name: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.phone = input("Enter phone: ")
        self.emailid = input("Enter email: ")

    def display_user(self):
        print("---User info---")
        print("User ID:", self.user_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("Email:", self.emailid)




myBooksList = []
myAuthorsList = []
myUsersList = []

while 1:
    print("MAIN MENU")
    print("1. Add book")
    print("2. Add author")
    print("3. Add user")
    print("4. Display info")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting...")
        break

    elif choice == 1:
        book = Book_class()
        book.add_book()
        myBooksList.append(book)

    elif choice == 2:
        author = Author_class()
        author.add_author()
        myAuthorsList.append(author)

    elif choice == 3:
        user = User_class()
        user.add_user()
        myUsersList.append(user)

    elif choice == 4:
        print("DISPLAY MENU")
        print("1. Display books")
        print("2. Display authors")
        print("3. Display users")
        print("4. Display all info")

        choice2 = int(input("Enter your choice: "))

        if choice2 == 1:
            if not myBooksList:
                print("No books available.")
            else:
                for book in myBooksList:
                    book.display_book()

        elif choice2 == 2:
            if not myAuthorsList:
                print("No authors available.")
            else:
                for author in myAuthorsList:
                    author.display_author()

        elif choice2 == 3:
            if not myUsersList:
                print("No users available.")
            else:
                for user in myUsersList:
                    user.display_user()

        elif choice2 == 4:
            print("BOOKS")
            for book in myBooksList:
                book.display_book()

            print("AUTHORS")
            for author in myAuthorsList:
                author.display_author()

            print("USERS")
            for user in myUsersList:
                user.display_user()

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")