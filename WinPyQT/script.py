import pandas as pd
from LoadData import postLoad
from mainform import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

# from WinPyQT.* import loadUiType

# Form, Window = uic.load_ui.loadUiType("WinPyQT\\untitled.ui")


app = QApplication([])
window = QMainWindow()
form = Ui_MainWindow()
form.setupUi(window)
# form.pushButton.addAction()
data = postLoad().getData()
dictlist = postLoad().setDictFromRecords(data)
dicttable = []


# dictlist = postLoad().setDictFromRecords(data)
print(dicttable)
# data.getData()
# type: ignore
# form.tableWidget.setModel(model)

# window.setModel(model)
window.show()
app.exec()
