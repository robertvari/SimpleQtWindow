from PySide6.QtWidgets import QWidget, QApplication, QLineEdit, \
    QPushButton, QVBoxLayout
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        # window config
        self.setWindowTitle("Registration Form")
        self.resize(400, 600)

        # window content (widgets)
        main_layout = QVBoxLayout(self)

        hello_button = QPushButton("Say Hello!")
        main_layout.addWidget(hello_button)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = RegistrationForm()
    win.show()

    app.exec()