from PyQt5.QtWidgets import *
from PyQt6.QtCore import Qt


class SecondForm(QWidget):
    def __init__(self):
        super().__init__()
        # Установить заголовок и начальный размер
        self.setWindowTitle("Organizer")
        self.resize(300, 300)
        # self.mod = true
        layout = QFormLayout(self)
