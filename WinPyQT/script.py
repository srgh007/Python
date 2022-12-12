from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

# from WinPyQT.* import loadUiType

Form, Window = uic.load_ui.loadUiType("WinPyQT\\untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
