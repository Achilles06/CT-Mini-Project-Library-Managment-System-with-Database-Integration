# main.py

from library.cli import main_menu, book_operations_menu, user_operations_menu, author_operations_menu, genre_operations_menu
from library.database import create_connection
from library.operations import add_new_book, add_new_user, add_new_author, add_new_genre

def main():
    conn = create_connection()
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            book_operations_choice = book_operations_menu()
            if book_operations_choice == '1':
                add_new_book(conn)
            # Add other book operations here
        elif choice == '2':
            user_operations_choice = user_operations_menu()
            if user_operations_choice == '1':
                add_new_user(conn)
            # Add other user operations here
        elif choice == '3':
            author_operations_choice = author_operations_menu()
            if author_operations_choice == '1':
                add_new_author(conn)
            # Add other author operations here
        elif choice == '4':
            genre_operations_choice = genre_operations_menu()
            if genre_operations_choice == '1':
                add_new_genre(conn)
            # Add other genre operations here
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

