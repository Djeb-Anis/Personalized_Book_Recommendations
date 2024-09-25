
import sqlite3

class ReadingHistoryModel:
    def __init__(self, db_name = '/Book_Store.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Reading_history (
                    entry_id TEXT PRIMARY KEY AUTOINCREMENT,
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

