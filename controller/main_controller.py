
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtCore import Qt, QRegularExpression
import os


# ------------------------Importing all Local Files------------------------
# Models
from model.books_model import BookModel
from model.mood_tags_model import MoodTagModel
from model.ratings_model import RatingModel
from model.reading_history_model import ReadingHistoryModel
from model.reading_list_model import ReadingListModel
from model.users_model import UserModel

# ------------------------Controller Class------------------------

class MainController:
    def __init__(self, db_name='Book_Store.db'):

        # Get the directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Create the full path to the database file in the parent directory
        self.db_path = os.path.join(base_dir, '..', db_name)

        # Declaring global variables which will store all my model instances
        global book_table
        global ratings_table
        global reading_history_table
        global reading_list_table
        global users_table
        global mood_tags_table

        # Assigning to all global variables created my model instances
        book_table = BookModel()
        ratings_table = RatingModel()
        reading_history_table = ReadingHistoryModel()
        reading_list_table = ReadingListModel()
        users_table = UserModel()
        mood_tags_table = MoodTagModel()

    # ------------------------Methods------------------------
    # Each method here will take input given by the user from the view Classes
    # This input will then be sent to the model Classes for them to use for various transformations

    def AllSqlTablesCreation(self):
        book_table.create()
        ratings_table.create()
        reading_history_table.create()
        reading_list_table.create()
        users_table.create()
        mood_tags_table.create()

    def InitialRootUserCreation(self):
        # Creating root user only if he does not yet exist
        if not users_table.get_user("root"):
            users_table.add_user("root", "changeme", "none")
        else:
            pass

        # Will need logic to be able to log in as the root user

        # Will need logic to change passwords in the model

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


    def filter_table(self, text, proxy_model):
        # Set the filter fixed string to the proxy model
        proxy_model.setFilterFixedString(text)
        # WOULD LIKE TO USE REGEX
        # But the setFilterRegExp method of the QSortFilterProxyModel object doesn't seem to exist??
        # My QSortFilterProxyModel object is in home_window in the load_sql_model method

    def LoginOverlayShow(self):
        login_overlay.show()

    def handle_login(self, username, password):
        username = username.setText()
        password = password.setText()

        login_data = users_table.get_user(username)

        # Fetch the login data from the users table
        if not login_data:
            login_overlay.login_status.setText("Invalid credentials!")
        else:
            if login_data[1] == username and login_data[3] == password:
                login_overlay.login_status.setText("Login successful!")
                login_overlay.hide()  # Hide the overlay on successful login


# ------------------------Main Application------------------------
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_controller = MainController()
#     main_window = HomeWindow(main_controller)
#     login_overlay = LoginOverlay(main_controller)
#     main_window.show()
#     sys.exit(app.exec())



