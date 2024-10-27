from library.book import Book
from library.user import User
from library.author import Author
from library.genre import Genre

# Function to view all books
def view_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

# Function to view all users
def view_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

# Function to view all authors
def view_authors(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

# Function to view all genres
def view_genres(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM genres")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

# Function to update a book
def update_book(conn):
    book_id = input("Enter book ID to update: ")
    new_title = input("Enter new title: ")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = %s WHERE id = %s", (new_title, book_id))
    conn.commit()
    print(f"Book ID {book_id} updated successfully.")
    cursor.close()

# Function to update a user
def update_user(conn):
    user_id = input("Enter user ID to update: ")
    new_name = input("Enter new name: ")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s WHERE id = %s", (new_name, user_id))
    conn.commit()
    print(f"User ID {user_id} updated successfully.")
    cursor.close()

# Function to update an author
def update_author(conn):
    author_id = input("Enter author ID to update: ")
    new_name = input("Enter new name: ")
    cursor = conn.cursor()
    cursor.execute("UPDATE authors SET name = %s WHERE id = %s", (new_name, author_id))
    conn.commit()
    print(f"Author ID {author_id} updated successfully.")
    cursor.close()

# Function to update a genre
def update_genre(conn):
    genre_id = input("Enter genre ID to update: ")
    new_name = input("Enter new name: ")
    cursor = conn.cursor()
    cursor.execute("UPDATE genres SET name = %s WHERE id = %s", (new_name, genre_id))
    conn.commit()
    print(f"Genre ID {genre_id} updated successfully.")
    cursor.close()

# Function to delete a book
def delete_book(conn):
    book_id = input("Enter book ID to delete: ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    print(f"Book ID {book_id} deleted successfully.")
    cursor.close()

# Function to delete a user
def delete_user(conn):
    user_id = input("Enter user ID to delete: ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    print(f"User ID {user_id} deleted successfully.")
    cursor.close()

# Function to delete an author
def delete_author(conn):
    author_id = input("Enter author ID to delete: ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors WHERE id = %s", (author_id,))
    conn.commit()
    print(f"Author ID {author_id} deleted successfully.")
    cursor.close()

# Function to delete a genre
def delete_genre(conn):
    genre_id = input("Enter genre ID to delete: ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM genres WHERE id = %s", (genre_id,))
    conn.commit()
    print(f"Genre ID {genre_id} deleted successfully.")
    cursor.close()
