
import sqlite3
import os

class MoodTagModel:
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
            CREATE TABLE IF NOT EXISTS Moood_Tags (
                Mood_Tag_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Mood_Tag TEXT
            );
        ''')
        self.connection.commit()

    def add_mood_tag(self, new_mood_tag):
        pass
    def modify_mood_tag(self):
        pass
        # Will create a GUI for this

    def close(self):
        self.connection.close()

