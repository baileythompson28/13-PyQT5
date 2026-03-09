import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5")
        self.setGeometry(700, 300, 600, 400)
        self.initUI()

    def create_label(self, image_path):
        label = QLabel()
        pixmap = QPixmap(image_path)

        label.setPixmap(pixmap.scaled(
            300, 200, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation))

        label.setAlignment(Qt.AlignCenter)
        return label

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        label1 = self.create_label("catzilla.jpg")
        label2 = self.create_label("illiterate.jpg")
        label3 = self.create_label("money.jpg")
        label4 = self.create_label("yelling.jpg")
        label5 = self.create_label("Mr.T.jpg")

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(label1)
        hbox.addWidget(label2)

        vbox.addLayout(hbox)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        self.central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()