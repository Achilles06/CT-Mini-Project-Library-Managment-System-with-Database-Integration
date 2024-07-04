# library/cli.py

def main_menu():
    print("Welcome to the Library Management System with Database Integration!")
    print("****")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    return choice

def book_operations_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    
    choice = input("Enter your choice: ")
    return choice

def user_operations_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    
    choice = input("Enter your choice: ")
    return choice

def author_operations_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    
    choice = input("Enter your choice: ")
    return choice

def genre_operations_menu():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")
    
    choice = input("Enter your choice: ")
    return choice
