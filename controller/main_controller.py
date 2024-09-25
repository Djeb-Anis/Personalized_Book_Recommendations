
import sys
from PyQt6.QtWidgets import QApplication

# ------------------------Importing all Local Files------------------------
# Models
from model.books_model import BookModel
# Still needs to be coded up from model.mood_tags_model import
from model.ratings_model import RatingModel
from model.reading_history_model import ReadingHistoryModel
from model.reading_list_model import ReadingListModel
from model.users_model import UserModel

# View
from view.home_window import HomeWindow
from view.login_overlay import LoginOverlay


# ------------------------Controller Class------------------------

class MainController:
    def __init__(self):
        pass

        # ------------------------Methods------------------------
        # Each method here will take input given by the user from the view Classes
        # This input will then be sent to the model Classes for them to use for various transformations



