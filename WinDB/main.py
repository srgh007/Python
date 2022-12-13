import sys

from LoadData import postLoad
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Table(QWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        # Установить заголовок и начальный размер
        self.setWindowTitle("Organizer")
        self.resize(500, 300)

        # Установить иерархию данных, 4 строки и 4 столбца
        self.model = QStandardItemModel(4, 3)
        # Установить текстовое содержимое четырех меток заголовка в горизонтальном направлении
        self.model.setHorizontalHeaderLabels(["Задача", "Плановая дата", "Выполнено"])

        # # Тодо оптимизации 2 добавить данные

        for row in range(4):
            for column in range(3):
                item = QStandardItem("row %s,column %s" % (row, column))
                # Установить текстовое значение каждой позиции
                self.model.setItem(row, column, item)

        # Создать представление таблицы, установить модель на пользовательскую модель
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # #todo Оптимизация 1 Форма заполняет окно
        # #Горизонтальная метка расширяет остальную часть окна и заполняет форму
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # # Горизонтальное направление, размер таблицы увеличивается до соответствующего размера
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #
        # #TODO Optimization 3 Удалить текущие выбранные данные
        # indexs=self.tableView.selectionModel().selection().indexes()
        # print(indexs)
        # if len(indexs)>0:
        #     index=indexs[0]
        #     self.model.removeRows(index.row(),1)

        # Установить макет

        p = postLoad()
        # db = postLoad.getData
        todaytasklist = []
        todaytasklist = p.setListFromDb()
        # print(dbdict)
        tasklist = []
        tasklist = p.getTasks()

        combobox = QComboBox(self)
        combobox.addItems(tasklist)
        # combobox.setText("Push")
        # layout = QVBoxLayout()
        layout = QFormLayout(self)
        layout.addRow(combobox)

        buttonToday = QPushButton(self)
        buttonToday.setText("Сегодня")
        buttonToday.setMinimumSize(QSize(230, 30))
        buttonToday.setMaximumSize(QSize(230, 30))
        buttonTomorrow = QPushButton(self)
        buttonTomorrow.setText("Завтра")
        buttonTomorrow.setMinimumSize(QSize(230, 30))
        buttonTomorrow.setMaximumSize(QSize(230, 30))
        layout.addRow(buttonToday, buttonTomorrow)
        layout.addRow(self.tableView)
        self.setLayout(layout)

        # layout.addWidget(hlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())
