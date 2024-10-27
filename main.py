from library.cli import (
    main_menu, book_operations_menu, user_operations_menu, 
    author_operations_menu, genre_operations_menu
)
from library.database import create_connection
from library.operations import (
    add_new_book, add_new_user, add_new_author, add_new_genre, 
    view_books, view_users, view_authors, view_genres,
    update_book, update_user, update_author, update_genre,
    delete_book, delete_user, delete_author, delete_genre
)

def main():
    conn = create_connection()

    while True:
        choice = main_menu()

        if choice == '1':  # Book operations
            book_operations_choice = book_operations_menu()
            if book_operations_choice == '1':
                add_new_book(conn)
            elif book_operations_choice == '2':
                view_books(conn)
            elif book_operations_choice == '3':
                update_book(conn)
            elif book_operations_choice == '4':
                delete_book(conn)

        elif choice == '2':  # User operations
            user_operations_choice = user_operations_menu()
            if user_operations_choice == '1':
                add_new_user(conn)
            elif user_operations_choice == '2':
                view_users(conn)
            elif user_operations_choice == '3':
                update_user(conn)
            elif user_operations_choice == '4':
                delete_user(conn)

        elif choice == '3':  # Author operations
            author_operations_choice = author_operations_menu()
            if author_operations_choice == '1':
                add_new_author(conn)
            elif author_operations_choice == '2':
                view_authors(conn)
            elif author_operations_choice == '3':
                update_author(conn)
            elif author_operations_choice == '4':
                delete_author(conn)

        elif choice == '4':  # Genre operations
            genre_operations_choice = genre_operations_menu()
            if genre_operations_choice == '1':
                add_new_genre(conn)
            elif genre_operations_choice == '2':
                view_genres(conn)
            elif genre_operations_choice == '3':
                update_genre(conn)
            elif genre_operations_choice == '4':
                delete_genre(conn)

        elif choice == '5':  # Exit
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

