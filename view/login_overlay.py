# login_overlay.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGraphicsBlurEffect
from PyQt6.QtCore import Qt


class LoginOverlay(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)

        # Storing the controller instance
        self.controller = controller


        # Will need to style these elements appropriately
        self.setStyleSheet(""" 
        background-color: rgba(0, 0, 0, 0.9);
        color: rgba(100,100,100);
        
        """)
        self.setGeometry(0, 0, 800, 650)  # Cover the entire window

        # Create a layout for the login elements
        self.login_layout = QVBoxLayout(self)
        self.login_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the login elements
        self.login_layout.setContentsMargins(50, 50, 50, 50)  # Add margins

        # Creating the widgets necessary for the login dialog
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Login")
        self.login_status = QLabel("")

        # Adding the widgets to the login layout
        self.login_layout.addWidget(self.username_label)
        self.login_layout.addWidget(self.username_input)
        self.login_layout.addWidget(self.password_label)
        self.login_layout.addWidget(self.password_input)
        self.login_layout.addWidget(self.login_button)
        self.login_layout.addWidget(self.login_status)

        # Connect the login button to a method
        self.login_button.clicked.connect(self.controller.handle_login(self.username_input, self.password_input))

    # ------------------------Hide & Show Event------------------------
    # We override the hide and show event methods to apply a QGraphicsBlurEffect to the main window's central widget
    def showEvent(self, event):
        # Apply blur effect to the central widget of the parent (main window) when the overlay is shown
        if self.parent():
            central_widget = self.parent().centralWidget()
            blur_effect = QGraphicsBlurEffect()
            blur_effect.setBlurRadius(10)  # I can adjust the blur radius as needed
            central_widget.setGraphicsEffect(blur_effect)
        super().showEvent(event)

    def hideEvent(self, event):
        # Remove blur effect from the central widget of the parent (main window) when the overlay is hidden
        if self.parent():
            central_widget = self.parent().centralWidget()
            central_widget.setGraphicsEffect(None)
        super().hideEvent(event)

