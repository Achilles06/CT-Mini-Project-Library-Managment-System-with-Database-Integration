# library/book.py

class Book:
    def __init__(self, title, author_id, genre_id, isbn, publication_date, availability=True):
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = availability
