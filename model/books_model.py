import sqlite3
import os
class BookModel:
    def __init__(self, db_name='Book_Store.db'):

        # Get the directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Create the full path to the database file in the parent directory
        db_path = os.path.join(base_dir, '..', db_name)

        # Connect to my db
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print("Error connecting to database:", e)

    def create(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                genre TEXT,
                summary TEXT,
                mood_tags TEXT
            );
        ''')
        self.connection.commit()

    def add_book(self,  title, author, genre, summary, mood_tags):
        self.cursor.execute('''
            INSERT INTO Books (title, author, genre, summary, mood_tags)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, author, genre, summary, mood_tags))
        self.connection.commit()

    def delete_book(self,book_id):
        self.cursor.execute('''
        DELETE FROM Books 
        WHERE book_id = ?
        '''), (book_id)
        self.connection.commit()

    def modify_book(self):
        pass
        # Will create a GUI for this, therefore, the logic can't be written here yet

    def get_books(self):
        self.cursor.execute('SELECT * FROM Books')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

