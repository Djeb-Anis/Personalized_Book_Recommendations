
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


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
    def __init__(self):
        pass

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

        book_table.create_table()
        ratings_table.create_table()
        reading_history_table.create_table()
        reading_list_table.create_table()
        users_table.create_table()
        mood_tags_table.create_table()


    def DisplayBooksMainWindow(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE") # Database Type
        self.db.setDatabaseName("/Book_Store.db") # Path to database

        if not self.db.open():
            # Error handling logic
            pass

        self.sql_table_model = QSqlTableModel
        self.sql_table_model.setTable("Books")
        self.sql_table_model.select() # Load the data

        return self.sql_table_model







