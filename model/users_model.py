
import sqlite3
import os
class UserModel:
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
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEST,
                password_hash TEXT,
                password_clear TEXT,
                email TEXT,
                list_id TEXT
            );
        ''')
        self.connection.commit()

    # Will need to define functions for the root user (Create, modify credentials, cannot delete)

    def add_user(self, username, password_clear, email):

        # Will need logic to check for duplicates in the database


        # password hash
        password_hash = hash(password_clear)

        self.cursor.execute('''
            INSERT INTO Users (username, password_hash, password_clear, email)
            VALUES (?, ?, ?, ?)
        ''', (username, password_hash, password_clear, email))
        self.connection.commit()

        # fetching the user_id created
        self.cursor.execute('''
            SELECT DISTINCT 
                user_id
            FROM
                Users
            WHERE
                password_hash = ?
        ''', (password_hash,))

        user_id = self.cursor.fetchone()

        # Check if a user_id was found
        if user_id is not None:
            # Extract the user_id from the tuple
            # Converting it to string, because hashing an integer in python does nothing
            user_id = str(user_id[0])

            # list_id unique hash
            list_tuple = (user_id, password_hash)
            list_id = hash(list_tuple)

            # Updating the existing user with the unique list_id
            self.cursor.execute('''
                    UPDATE Users
                    SET list_id = ?
                    WHERE user_id = ?
                ''', (list_id, user_id))
            self.connection.commit()

        else:
            error = ("No user found with the provided password.")
            # CONTINUE HERE, ONCE GUI IS SET, PRINT OUT ERROR

    def delete_user(self,user_id):
        self.cursor.execute('''
        DELETE FROM Users 
        WHERE user_id = ?
        ''', (user_id,))
        self.connection.commit()

    def modify_user(self):
        pass
        # Will create a GUI for this, therefore, the logic can't be written here yet


    def get_user(self, username):
        self.cursor.execute('''
        SELECT * FROM Users
        WHERE user_id = ?
        ''', (username,))

        return self.cursor.fetchone()

    def close(self):
        self.connection.close()

