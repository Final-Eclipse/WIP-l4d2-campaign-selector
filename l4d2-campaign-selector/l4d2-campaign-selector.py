from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QSizePolicy, QVBoxLayout, QLabel, QHBoxLayout, QGraphicsDropShadowEffect, QGraphicsEffect, QTextEdit
from PyQt5.QtCore import Qt, QPropertyAnimation, QPointF, QTimer, QDateTime, QDate
from PyQt5.QtGui import QFont, QLinearGradient, QPainter, QBrush, QPen, QColor
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 400)

        self.setStyleSheet("background-color: #8B0000")


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)


        label = QLabel("Left 4 Dead 2 Campaign Selector")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Chewy", 20))
        label.setStyleSheet("color: #F2F2E6")
        main_layout.addWidget(label)

        





app = QApplication([])
window = MainWindow()
window.show()
app.exec()
