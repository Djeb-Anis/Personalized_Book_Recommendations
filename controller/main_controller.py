
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
import os


# ------------------------Importing all Local Files------------------------
# Models
from model.books_model import BookModel
from model.mood_tags_model import MoodTagModel
from model.ratings_model import RatingModel
from model.reading_history_model import ReadingHistoryModel
from model.reading_list_model import ReadingListModel
from model.users_model import UserModel

# View



# ------------------------Controller Class------------------------

class MainController:
    def __init__(self, db_name='Book_Store.db'):

        # Get the directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Create the full path to the database file in the parent directory
        self.db_path = os.path.join(base_dir, '..', db_name)

    # ------------------------Methods------------------------
    # Each method here will take input given by the user from the view Classes
    # This input will then be sent to the model Classes for them to use for various transformations

    def AllSqlTablesCreation(self):
        book_table = BookModel()
        ratings_table = RatingModel()
        reading_history_table = ReadingHistoryModel()
        reading_list_table = ReadingListModel()
        users_table = UserModel()
        mood_tags_table = MoodTagModel()

        book_table.create()
        ratings_table.create()
        reading_history_table.create()
        reading_list_table.create()
        users_table.create()
        mood_tags_table.create()


    def DisplayBooksMainWindow(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE") # Database Type
        self.db.setDatabaseName(self.db_path) # Path to database

        if not self.db.open():
            # Error handling logic
            pass

        self.sql_table_model = QSqlTableModel()
        self.sql_table_model.setTable("Books")
        self.sql_table_model.select() # Load the data

        return self.sql_table_model







