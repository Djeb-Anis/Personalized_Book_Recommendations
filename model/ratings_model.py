
import sqlite3

class RatingModel:
    def __init__(self, db_name='/Book_Store.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ratings (
                rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                book_id INTEGER,
                rating TEXT,
                reveiew TEXT
            );
        ''')
        self.connection.commit()

    def add_rating(self, rating_id, book_id, user_id, rating, review):
        self.cursor.execute('''
            INSERT INTO Ratings (book_id, rating_id, user_id, rating, review)
            VALUES (?, ?, ?, ?, ?)
        ''', (rating_id, book_id, user_id, rating, review))
        self.connection.commit()


    def delete_rating(self,rating_id):
        self.cursor.execute('''
        DELETE FROM Ratings 
        WHERE rating_id = ?
        '''), (rating_id)
        self.connection.commit()

    def modify_rating(self):
        pass
        # Will create a GUI for this, therefore, the logic can't be written here yet


    def get_ratings(self):
        self.cursor.execute('SELECT * FROM Ratings')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

