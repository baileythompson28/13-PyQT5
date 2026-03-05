import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

"""
sys: This is a built-in Python module that provides access to variables and functions that interact with the Python interpreter.
PyQt5.QtWidgets: This module contains all the main GUI “widgets” such as buttons, labels, and windows.
QApplication: This class manages the GUI application itself.
QMainWindow: This class provides a main application window that you can customize.
"""

# Create a custom window:
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CMP 25-26 Year 1")
        self.setGeometry(00, 00, 500, 500)  # (x,y,width, height)
        # x: distance from the left edge of your screen
        # y: distance from the top of your screen
        self.setWindowIcon(QIcon("images/Greg.png"))
        self.label = QLabel("Hello", self)
        self.label.setFont(QFont("Ariel", 40))
        self.label.setGeometry(0, 0, 500, 100)
        self.label.setStyleSheet(
            "color: Black; "
            "background-color: #87CeFA;"
            "border: 10px solid black;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )
        self.label.setAlignment(Qt.AlignCenter)

        self.piclabel = QLabel
        self.piclabel.setGeometry(0, 100, 100,250)

        self.pixmap = QPixmap("images/Greg.png")
        self.piclabel.setPixmap(self.pixmap)
        self.piclabel.setScaledContents(True)
        self.piclabel.setGeometry(self.width(
        ) - self.piclabel.width(), self.height() - self.piclabel.height(), 300, 250)

        self.piclabel.setGeometry((self.width(
        ) - self.piclabel.width())//2, (self.height() - self.piclabel.height()) //2, 300, 250)

def main():
    # Creates the main application and passes in an y command line arguments
    app = QApplication(sys.argv)
    window = MainWindow()  # Instatiate our main window
    window.show()  # Make the window visible

    # Starts the application loop. The program will keep running until you close the Window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
 