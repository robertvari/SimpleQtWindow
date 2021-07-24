from PySide6.QtWidgets import QWidget, QApplication
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registration Form")
        self.resize(400, 600)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = RegistrationForm()
    win.show()

    app.exec()