import sys # This is imported for testing purposes only
from login_overlay import LoginOverlay  # Import the LoginOverlay class, don't know if fits the Model, Controller, View methodology
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTableView

# Importing the controller
from controller.main_controller import MainController

class HomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Creating an instance of my MainController Class I can manipulate
        main_controller = MainController()

        # Creating all SQL tables needed
        main_controller.AllSqlTablesCreation()

        # Création d'une liste pour garder les variables contenant les autres fenêtres vivantes, might need it
        self.other_windows = []

        # Dimension de la fenêtre principale
        self.setGeometry(250, 150, 800, 650)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # ------------------------Labels & Buttons------------------------

        # Creating the buttons and labels which go above the window content
        self.quit_app = QPushButton()

        self.username = QLabel() # Missing the logic to fetch user information

        self.version = QLabel("Version 1.0.0")

        # Creating the window content


        # Creating all the buttons that go below the window content
        self.ratings_button = QPushButton("Ratings")

        self.add_to_reading_list_button = QPushButton("Add to Reading List")

        self.view_reading_list_button = QPushButton("View Reading List")

        # Don't forget the button for the super user
        # Will either need to create an if statement here or create separate files for each super user window

        self.history_button = QPushButton("History")

        # ------------------------Layout------------------------

        # Setting the horizontal layout for the top buttons and information
        self.horizontal_up_layout = QHBoxLayout()
        # Adding to the layout
        self.horizontal_up_layout.addWidget(self.quit_app)
        self.horizontal_up_layout.addWidget(self.username)
        self.horizontal_up_layout.addWidget(self.version)

        # Setting the horizontal layout I'll need for the buttons below
        self.horizontal_down_layout = QHBoxLayout()
        # Adding to the layout
        self.horizontal_down_layout.addWidget(self.ratings_button)
        self.horizontal_down_layout.addWidget(self.add_to_reading_list_button)
        self.horizontal_down_layout.addWidget(self.view_reading_list_button)
        self.horizontal_down_layout.addWidget(self.history_button)

        # Setting the main vertical layout I'll be using
        self.vertical_layout = QVBoxLayout()
        # Adding to the layout
        self.vertical_layout.addLayout(self.horizontal_up_layout) # Nested layout

        # Creating a variable on which the controller can assign its Sql table model
        imported_model = main_controller.DisplayBooksMainWindow()

        # displaying said sql table model
        self.sql_table_view = QTableView()
        self.sql_table_view.setModel(imported_model)
        self.sql_table_view.setWindowTitle("Books Database")

        # Adding the table to my main layout
        self.vertical_layout.addWidget(self.sql_table_view)

        # Adding to the layout
        self.vertical_layout.addLayout(self.horizontal_down_layout) # Nested layout

        # Set the layout for the central widget
        central_widget.setLayout(self.vertical_layout)

        # ------------------------Login Call------------------------

        # Create and show the login overlay
        self.login_overlay = LoginOverlay(self)
        self.login_overlay.show()  # Show the login overlay

# ------------------------Testing Code------------------------
# This code will need to go when I'm done coding, only the controller can call these windows
if __name__ == "__main__":
    app = QApplication(sys.argv)
    test_window = HomeWindow()
    test_window.show()
    sys.exit(app.exec())
# ------------------------Testing Code------------------------
