
# ------------------------Importing outside modules------------------------
import sys
from PyQt6.QtWidgets import QApplication

# ------------------------Importing all Local Files------------------------
# Models
from model.books_model import BookModel
from model.mood_tags_model import MoodTagModel
from model.ratings_model import RatingModel
from model.reading_history_model import ReadingHistoryModel
from model.reading_list_model import ReadingListModel
from model.users_model import UserModel

# View
from view.home_window import HomeWindow
from view.login_overlay import LoginOverlay

# Controller
from controller.main_controller import MainController

# ------------------------Main app Code------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Controller
    main_controller = MainController()

    # All View windows
    main_window = HomeWindow(main_controller)
    login_overlay = LoginOverlay(main_controller)

    main_window.show()
    sys.exit(app.exec())