
import sqlite3

class ReadingListModel:
    def __init__(self, db_name='/Book_Store.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Reading_Lists (
                list_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                book_id INTEGER
            );
        ''')
        self.connection.commit()

    def add_reading_list(self, list_id, book_id, user_id):
        self.cursor.execute('''
            INSERT INTO Reading_lists (list_id, book_id, user_id)
            VALUES (?, ?, ?)
        ''', (list_id, book_id,  user_id))
        self.connection.commit()

    def delete_reading_list(self,list_id):
        self.cursor.execute('''
        DELETE FROM Reading_lists 
        WHERE list_id = ?
        '''), (list_id)
        self.connection.commit()

    def modify_reading_list(self):
        pass
        # Will create a GUI for this, therefore, the logic can't be written here yet

    def get_reading_lists(self):
        self.cursor.execute('SELECT * FROM Reading_Lists')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

