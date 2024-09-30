import sys # This is imported for testing purposes only
from login_overlay import LoginOverlay  # Import the LoginOverlay class, don't know if fits the Model, Controller, View methodology
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTableView
from PyQt6.QtCore import QSortFilterProxyModel


class HomeWindow(QMainWindow):

    def __init__(self, controller):
        super().__init__()

        # Creating an instance of my MainController Class I can manipulate
        self.controller = controller

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
        self.quit_app.setFixedSize(70, 30)
        self.quit_app.setText("Quit")

        self.username = QLabel() # Missing the logic to fetch user information

        self.version = QLabel("Version 1.0.0")

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
        self.horizontal_up_layout.addStretch() #This will push the user and version info to the right
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

        # Creating my search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")

        # Adding to the layout
        self.vertical_layout.addWidget(self.search_bar)

        # Creating a QTableView object which will store the sql table
        self.sql_table_view = QTableView()

        # Adding the table to my main layout
        self.vertical_layout.addWidget(self.sql_table_view)

        # Completing the layout
        self.vertical_layout.addLayout(self.horizontal_down_layout) # Nested layout

        # Setting the layout for the central widget
        central_widget.setLayout(self.vertical_layout)

        # Load the SQL model and set it to the table view
        self.load_sql_model()

        # Connecting the search bar to my filter function
        self.search_bar.textChanged.connect(self.on_search_text_changed)

        # ------------------------Login Call------------------------

        # Create and show the login overlay
        self.login_overlay = LoginOverlay(self)
        self.login_overlay.show()  # Show the login overlay

        # ------------------------Search Bar Functions------------------------

    def load_sql_model(self):
        # Get the SQL model from the controller
        imported_model = self.controller.DisplayBooksMainWindow()
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(imported_model)
        self.sql_table_view.setModel(self.proxy_model)
        self.sql_table_view.setWindowTitle("Books Database")

    def on_search_text_changed(self, text):
        # Call the controller's filter function
        self.controller.filter_table(text, self.proxy_model)



# ------------------------Testing Code------------------------
# This code will need to go when I'm done coding, only the controller can call these windows
if __name__ == "__main__":
    from controller.main_controller import MainController  # Import here to avoid circular import
    app = QApplication(sys.argv)
    main_controller = MainController()
    test_window = HomeWindow(main_controller)
    test_window.show()
    sys.exit(app.exec())
# ------------------------Testing Code------------------------
