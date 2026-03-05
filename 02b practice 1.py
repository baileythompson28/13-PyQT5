# Try to make an application that is 600px tall and 800px wide, 
# and put 3 labels and 3 pictures on it. Make them all visible. 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CMP 25-26 year 1")
        self.setGeometry(00, 00, 800, 600)  # (x,y,width, height)
        # x: distance from the left edge of your screen
        # y: distance from the top of your screen
        self.setWindowIcon(QIcon("")) # add image
        """text one"""
        self.label = QLabel("text one", self)
        self.label.setFont(QFont("Ariel", 40))
        self.label.setGeometry(0, 0, 800, 100)
        self.label.setStyleSheet(
            "color: White; "
            "background-color: #003754;"
            "font-weight: bold;"
            "text-decoration: underline;"
        )
        self.label.setAlignment(Qt.AlignCenter)
    
        """text two"""
        self.label = QLabel("text two", self)
        self.label.setFont(QFont("Ariel", 20))
        self.label.setGeometry(0, 100, 500, 300)
        self.label.setStyleSheet(
            "color: White; "
            "background-color: #006094;"
            "font-style: italic;"
        )
        self.label.setAlignment(Qt.AlignCenter)

        """text three"""
        self.label = QLabel("text three", self)
        self.label.setFont(QFont("Ariel", 20))
        self.label.setGeometry(200, 400, 600, 200)
        self.label.setStyleSheet(
            "color: White; "
            "background-color: #0D2940;"
        )
        self.label.setAlignment(Qt.AlignCenter)

        """pictures"""
        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(0, 100, 100,250)

        self.pixmap = QPixmap("hangman.drawio.png") # add image
        self.piclabel.setPixmap(self.pixmap)
        self.piclabel.setScaledContents(True)
        self.piclabel.setGeometry(self.width(
        ) - self.piclabel.width(), self.height() - self.piclabel.height(), 300, 250)

        self.piclabel.setGeometry((self.width(
        ) - self.piclabel.width())//2, (self.height() - self.piclabel.height()) //2, 300, 250) 


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

