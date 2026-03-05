"""
layout managers
a layout manager is a class that arranges widgets automatically in a certain pattern.
3 common LM types on PyQt5 are:
- QVBoxLayout - stacks widgets vertically 
- QHBoxLayout - places widgets horizontally 
- QGridLayout - arranges widgets in a grid of rows and collumns
"""
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("layout example")
        self.setGeometry(700, 300, 400, 400)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        #creating labels
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")
        label4 = QLabel("Label 4")
        label5 = QLabel("Label 5")

        #give labels color
        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: yellow")
        label4.setStyleSheet("background-color: green")
        label5.setStyleSheet("background-color: purple")
        #labels dont show up, needed to specifiy parent container

        #vertical - QVBoxLayout
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


