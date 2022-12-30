import sys
from datetime import date, datetime, timedelta

from LoadData import postLoad
from LoadSQLdata import LoadSQL
from PyQt5 import QtSql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtWidgets import *
from SelForm import SecondForm


class Table(QWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        # Установить заголовок и начальный размер
        self.setWindowTitle("Organizer")
        self.resize(500, 300)
        self.secondForm = SecondForm()
        # Установить иерархию данных, 4 строки и 4 столбца
        # self.model = QStandardItemModel(4, 3)
        # Установить текстовое содержимое четырех меток заголовка в горизонтальном направлении
        # self.model.setHorizontalHeaderLabels(["Задача", "Плановая дата", "Выполнено"])
        ls = LoadSQL()
        database = QSqlDatabase.addDatabase(
            "QODBC"
        )  # TODO find out if I want QPSQL or QPSQL7
        database.setHostName("localhost")
        database.setDatabaseName("PostgreSQL35W")
        database.setUserName("postgres")
        database.setPassword("postgres")
        database.open()
        # self.tableView = QTableView()
        self.tableView = TableView()
        self.model = ls.getSQLModel(ls.setQuery(0))
        # self.sqlmodel = QSqlQueryModel()

        self.tableView.setModel(self.model)
        self.tableView.hideColumn(0)
        self.tableView.hideColumn(2)
        self.tableView.hideColumn(3)

        self.msgSc = QShortcut(QKeySequence("Del"), self.tableView)
        self.msgSc.activated.connect(self.tableView.setFocus)

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
        # todaytasklist = []
        # todaytasklist = p.setListFromDb()
        # print(dbdict)
        tasklist = {}
        tasklist = p.getTasks()

        combobox = QComboBox(self)
        combobox.addItems(list(tasklist))
        # combobox.setText("Push")
        # layout = QVBoxLayout()
        layout = QFormLayout(self)
        layout.addRow(combobox)

        buttonToday = QPushButton(self)
        buttonToday.setText("Сегодня")

        buttonToday.clicked.connect(
            lambda: self.insert_data(
                tasklist[combobox.currentText()]["id"], datetime.now()
            )
            # self.tableView
        )
        self.tableView.doubleClicked.connect(self.view_form)
        self.tableView.keyReleaseEvent
        buttonToday.setMinimumSize(QSize(230, 30))
        buttonToday.setMaximumSize(QSize(230, 30))
        buttonTomorrow = QPushButton(self)
        buttonTomorrow.setText("Завтра")
        buttonTomorrow.setMinimumSize(QSize(230, 30))
        buttonTomorrow.setMaximumSize(QSize(230, 30))
        layout.addRow(buttonToday, buttonTomorrow)
        layout.addRow(self.tableView)
        self.setLayout(layout)

        # it = self.currentItem()
        # print(it)
        # if it is not None:
        # print(it.text())

    # def updModel(self, mod):

    # return inssql

    def insert_data(self, id, data):
        inssql = "INSERT INTO public.queue_tasks (id_task, created_at, plan_date) VALUES({}, now(), '{}');".format(
            id,
            data,
        )
        ls = LoadSQL()
        query = QtSql.QSqlQuery()
        query.exec(inssql)
        self.model.setQuery(ls.setQuery(0))
        # self.tableView.setModel(mod)
        self.update()

    def view_form(self):
        self.secondForm.show()

    def delete_data(self, id):
        delsql = "DELETE FROM public.queue_tasks WHERE id = {}".format(id)
        ls = LoadSQL()
        query = QtSql.QSqlQuery()
        query.exec()
        self.model.setQuery(ls.setQuery(0))
        # self.tableView.setModel(mod)
        self.update()

    # for row in range(4):
    #     for column in range(3):
    #         item = QStandardItem("row %s,column %s" % (row, column))
    #         # Установить текстовое значение каждой позиции
    #         self.model.setItem(row, column, item)

    # Создать представление таблицы, установить модель на пользовательскую модель

    # layout.addWidget(hlayout)


class TableView(QTableView):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, qKeyEvent):
        print(qKeyEvent.key())
        if qKeyEvent.key() == 68:
            print("ctrl d pressed")
            rows = set()
            index = self.selectedIndexes()[0]
            id = index.siblingAtColumn(0).data()
            delsql = "DELETE FROM public.queue_tasks WHERE id = {}".format(id)
            print(delsql)
            # self.delete_data(delsql)

            # self.model.setQuery(ls.setQuery(0))
            # # self.tableView.setModel(mod)
            # self.update()
            # rows.add(id)
            # print("IDs to delete: {}".format(sorted(rows)))

            # indexes = self.selectionModel().selectedRows()
            # indexes = self.selectedIndexes()
            # for index in sorted(indexes):
            #     print("Value {} is selected".format(index.data()))

            # print(index.column.)
        else:
            super().keyPressEvent(qKeyEvent)
        super(TableView, self).keyPressEvent(qKeyEvent)

    def delete_data(self, id):
        delsql = "DELETE FROM public.queue_tasks WHERE id = {}".format(id)
        ls = LoadSQL()
        query = QtSql.QSqlQuery()
        query.exec()
        self.model.setQuery(ls.setQuery(0))
        # self.tableView.setModel(mod)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())
