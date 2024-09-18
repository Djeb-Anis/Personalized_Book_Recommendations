
import sqlite3

class UserModel:
    def __init__(self, db_name='/Book_Store.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username INTEGER,
                password_hash TEXT,
                email TEXT
            );
        ''')
        self.connection.commit()

    def add_user(self, user_id, username, password_hash, email):
        self.cursor.execute('''
            INSERT INTO Users (user_id, username, password_hash, email)
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, password_hash, email))
        self.connection.commit()

    def delete_user(self,user_id):
        self.cursor.execute('''
        DELETE FROM Users 
        WHERE user_id = ?
        '''), (user_id)
        self.connection.commit()

    def modify_user(self):
        pass
        # Will create a GUI for this, therefore, the logic can't be written here yet


    def get_users(self):
        self.cursor.execute('SELECT * FROM Users')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

