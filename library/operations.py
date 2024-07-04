# library/operations.py

# library/operations.py

from library.book import Book
from library.user import User
from library.author import Author
from library.genre import Genre
from library.database import create_connection

import re

def add_book(conn, book):
    cursor = conn.cursor()
    sql = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (book.title, book.author_id, book.genre_id, book.isbn, book.publication_date, book.availability)
    cursor.execute(sql, values)
    conn.commit()

def add_user(conn, user):
    cursor = conn.cursor()
    sql = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
    values = (user.name, user.library_id)
    cursor.execute(sql, values)
    conn.commit()

def add_author(conn, author):
    cursor = conn.cursor()
    sql = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    values = (author.name, author.biography)
    cursor.execute(sql, values)
    conn.commit()

def add_genre(conn, genre):
    cursor = conn.cursor()
    sql = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
    values = (genre.name, genre.description, genre.category)
    cursor.execute(sql, values)
    conn.commit()

def get_valid_isbn():
    while True:
        isbn = input("Enter ISBN: ")
        if re.match(r'^\d{13}$', isbn):
            return isbn
        else:
            print("Invalid ISBN. Please enter a 13-digit number.")

def add_new_book(conn):
    title = input("Enter book title: ")
    author_id = int(input("Enter author ID: "))
    genre_id = int(input("Enter genre ID: "))
    isbn = get_valid_isbn()
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    
    book = Book(title, author_id, genre_id, isbn, publication_date)
    add_book(conn, book)
    print("Book added successfully.")

def add_new_user(conn):
    try:
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        
        user = User(name, library_id)
        add_user(conn, user)
        print("User added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print("Operation completed successfully.")
    finally:
        if conn.is_connected():
            conn.close()

def add_new_author(conn):
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    
    author = Author(name, biography)
    add_author(conn, author)
    print("Author added successfully.")

def add_new_genre(conn):
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    
    genre = Genre(name, description, category)
    add_genre(conn, genre)
    print("Genre added successfully.")
