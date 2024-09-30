
import sqlite3
import os

class ReadingHistoryModel:
    def __init__(self, db_name = 'Book_Store.db'):

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
                CREATE TABLE IF NOT EXISTS Reading_history (
                    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    book_id INTEGER,
                    date_added_to_reading_list TEXT,
                    date_rated TEXT
                );
            ''')
        self.connection.commit()

    # Reading history is added automatically
    # Each entry to a reading list will add a row and fill entry_id, user_id, book_id, and date_added_to_reading_list
    # Each entry to ratings, will fill date_rated
    def delete_history_entry(self, entry_id):
        self.cursor.execute('''
            DELETE FROM Reading_lists 
            WHERE entry_id = ?
            '''), (entry_id) # Since we'll be selecting with the mouse which entry to delete, I'll make sure we can fetch it using PyQT
        self.connection.commit()

    def modify_reading_list(self):
        pass
        # Will create a GUI for this, therefore, the logic can't be written here yet

    def get_reading_lists(self):
        self.cursor.execute('SELECT * FROM Reading_Lists')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

