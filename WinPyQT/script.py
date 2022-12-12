from mainform import Ui_MainWindow
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

# from WinPyQT.* import loadUiType

# Form, Window = uic.load_ui.loadUiType("WinPyQT\\untitled.ui")

app = QApplication([])
window = QMainWindow()
form = Ui_MainWindow()
form.setupUi(window)
# form.pushButton.addAction()
window.show()
app.exec()
