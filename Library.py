class Book:
    def __init__(self, title, author, ISBN, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self._quantity = quantity
    
    # show book details
    def get_book_details(self):
        return f"Book Title: {self.title} Author(s): {self.author} ISBN: {self.ISBN} Quantity Available: {self._quantity}"
 
    def is_book_available(self):
        return self._quantity >= 1
    
    def update_quantity(self, new_quantity):
        self._quantity = new_quantity


class User:
    def __init__(self, name, ID, group):
        self.name = name 
        self.ID = ID 
        self.group = group
        self.books_borrowed = []

    # show user details
    def get_user_details(self):
        return f"Name: {self.name} ID: {self.ID} Group: {self.group} Books Borrowed: {', '.join(self.books_borrowed)}"

    def borrow_book(self, book):
        if book.is_book_available():
            self.books_borrowed.append(book.title)
            book.update_quantity(book._quantity - 1)

    def return_book(self, book):
        if book.title in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.update_quantity(book._quantity + 1)


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def initialize_instances(self):
        # Create instances of books, users, and transactions
        self.books = [
            Book("Python Basics", "John Doe", "123456789", 5),
            Book("Data Science Handbook", "Jane Smith", "987654321", 3),
        ]

        self.users = [
            User("Ree", "A001", "Students"),
            User("Bob", "B002", "Faculty"),
        ]

    # show the menu to users whenever they visit the library
    def display_menu(self):
        print("\nMenu:")
        print("1. View Available Books")
        print("2. Display User Information")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

    def handle_user_interaction(self):
        while True: # Ensure the menu is always alive
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.view_available_books()
            elif choice == "2":
                self.display_user_information()
            elif choice == "3":
                self.borrow_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                print("Exiting the library. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def view_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book.get_book_details())

# user information is hardcoded so only the initialised users can be recognised when running the code
    def display_user_information(self):
        user_id = input("Enter your user ID: ")
        user = next((u for u in self.users if u.ID == user_id), None)
        if user:
            print(user.get_user_details())
        else:
            print("User not found. Please check your user ID.")

    def borrow_book(self):
        user_id = input("Enter your user ID: ")
        book_title = input("Enter the title of the book you want to borrow: ")

        user = next((u for u in self.users if u.ID == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if user and book: # Ensures that only registered users can borrow a book
            user.borrow_book(book)
            self.transactions.append(f"{user.name} borrowed {book.title}")
            print(f"{user.name} successfully borrowed {book.title}.")
        else:
            print("User or book not found. Please check your user ID and book title.")

    def return_book(self):
        user_id = input("Enter your user ID: ")
        book_title = input("Enter the title of the book you want to return: ")

        user = next((u for u in self.users if u.ID == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if user and book:
            user.return_book(book)
            self.transactions.append(f"{user.name} returned {book.title}")
            print(f"{user.name} successfully returned {book.title}.")
        else:
            print("User or book not found. Please check your user ID and book title.")


# Usage
library = Library()
library.initialize_instances()
library.handle_user_interaction()


