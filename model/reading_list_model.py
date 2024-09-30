
import sqlite3
from datetime import datetime
import os

class ReadingListModel:
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
            CREATE TABLE IF NOT EXISTS Reading_List (
                list_id TEXT,
                user_id INTEGER,
                book_id INTEGER,
                PRIMARY KEY (list_id, user_id, book_id)
            );
        ''')
        self.connection.commit()

    def add_reading_list(self, list_id, book_id, user_id):

        # LOGIC TO FETCH USER_ID FROM THE USER WE'RE LOGGED INTO
        # WILL NEED A LOGIN PAGE

        # fetching the list_id associated with our user
        self.cursor.execute('''
            SELECT DISTINCT 
                list_id,
            FROM
                Users
            WHERE
                user_id = ?
        ''', (user_id,))

        list_id = self.cursor.fetchone()

        # Check if a list_id was found
        if list_id is not None:
            list_id = list_id[0]  # Extract the list_id from the tuple
        else:
            error = ("It seems there was an error fetching your list ID.")
            # CONTINUE HERE, ONCE GUI IS SET, PRINT OUT

        # Find the book_id by creating an input field where you'll be able to search by title, author, or ID
        # Logic to choose book_id if given as input
        # This interactive window is in the home page


        self.cursor.execute('''
            INSERT INTO Reading_lists (list_id, book_id, user_id)
            VALUES (?, ?, ?)
        ''', (list_id, book_id,  user_id))
        self.connection.commit()


        # Saving the date, in order to add it to the history table
        current_date = str(datetime.now())

        # Adding an entry to the reading history table
        self.cursor.execute('''
            INSERT INTO Reading_history (user_id, book_id, date_added_to_reading_list)
            VALUES (?, ?, ?)
        ''',(user_id, book_id, current_date))

    def delete_reading_list(self,list_id, user_id, book_id):
        self.cursor.execute('''
        DELETE FROM Reading_lists 
        WHERE list_id = ? AND user_id = ? AND book_id = ?
        '''), (list_id, user_id, book_id)
        self.connection.commit()

    def modify_reading_list(self):
        pass
        # Will create a GUI for this, therefore, the logic can't be written here yet

    def get_reading_lists(self):
        self.cursor.execute('SELECT * FROM Reading_Lists')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

