from datetime import date, datetime, timedelta

from PyQt5 import QtSql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtWidgets import *


class LoadSQL:
    def __init__(self, delta=0):
        self.delta = delta

    delta = 0

    def setQuery(self, delta=0):
        data = datetime.now() + timedelta(days=delta)
        query = """SELECT       public.queue_tasks.id,
                                public.tasks.title , 
                                id_task,  
                                created_at, 
                                plan_date, 
                                tasktime 
                                FROM public.queue_tasks join public.tasks on 
                                (public.queue_tasks.id_task = public.tasks.id) 
                                where plan_date ='{}'
                    """.format(
            data.strftime("%Y-%m-%d")
        )
        return query

    # def QDBConnect(self):

    # return database

    # QDBConnect().open()

    # # Тодо оптимизации 2 добавить данные

    # x = [(1, 3, 5), (2, 4, 6)]
    # bl = dict('True':'yes','False':'no')

    # n = QDBConnect    # return true;

    def loadData(self, x, model):
        raw = 0
        col = 0
        for i in x:
            for o in i:
                if col == 2:
                    if o == "True":
                        o = "YES"
                    if o == "False":
                        o = "NO"
                    item = QStandardItem("{}".format(o))
                    model.setItem(raw, col, item)
                    col += 1
                    if col > 2:
                        col = 0
            raw += 1
        return model

    def getSQLModel(self, query):
        model = QtSql.QSqlQueryModel()
        model.setQuery(query)
        # model.setHorizontalHeaderLabels(["Name",])
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Задача")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Плановая дата")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Затрачено часов")

        return model

    # def gettodaytasklist(self):
    #     tasklist = []
    #     p_today_tasks = self.postLoad()
    #     tasklist = p_today_tasks.setListFromDb()
    #     loadData(tasklist)

    #     gettodaytasklist()
