
import sqlite3
from datetime import datetime
import os


class RatingModel:
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
            CREATE TABLE IF NOT EXISTS Ratings (
                rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                book_id INTEGER,
                rating TEXT
            );
        ''')
        self.connection.commit()

    def add_rating(self, book_id, user_id, rating):

        # Saving the date, in order to add it to the history table
        current_date = str(datetime.now())

        # fetching the entry_id associated with the book and user id
        self.cursor.execute('''
              SELECT DISTINCT 
                  entry_id,
              FROM
                  Reading_hitsory
              WHERE
                  book_id = ?,
                  user_id = ?
                  
          ''', (book_id, user_id,))

        entry_id = self.cursor.fetchone()

        # Check if a list_id was found
        if entry_id is not None:
            list_id = entry_id[0]  # Extract the list_id from the tuple
        else:
            error = ("It seems there was an error fetching your entry ID.")
            # CONTINUE HERE, ONCE GUI IS SET, PRINT OUT

        # Updating the reading history date_rated field
        self.cursor.execute('''
            UPDATE Reading_history
            SET date_rated = ?
            WHERE entry_id = ?
        ''', (current_date, entry_id,))

        # Inserting my new rating
        self.cursor.execute('''
            INSERT INTO Ratings (rating)
            VALUES (?, ?, ?)
        ''', (book_id, user_id, rating))
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

