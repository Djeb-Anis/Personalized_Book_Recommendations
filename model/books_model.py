import sqlite3

class BookModel:
    def __init__(self, db_name='/Book_Store.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
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

    def add_book(self,book_id,  title, author, genre, summary, mood_tags):
        self.cursor.execute('''
            INSERT INTO Books (title, author, genre, summary, mood_tags)
            VALUES (?, ?, ?, ?, ?)
        ''', (book_id, title, author, genre, summary, mood_tags))
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