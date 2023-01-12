import configparser
import csv
import fileinput
import locale
import os
import sys
from os import walk

import numpy as np
import pandas

# from pathlib import Path


# import pyodbc

# cnxn = pyodbc.connect(
#     "Driver={SQL Server Native Client 11.0};"
#     "Server=server_name;"
#     "Database=db_name;"
#     "Trusted_Connection=yes;"
# )
# cursor = cnxn.cursor()
# cursor.execute("SELECT * FROM Table")

# for row in cursor:
#     print("row = %r" % (row,))

locale.setlocale(locale.LC_ALL, "ru_RU")
csvlist = {}
maplist = {}
# with open("CSVDecodeLAN\\citmapping.csv", encoding="UTF8") as csvfile:
# reader = csv.DictReader(csvfile, delimiter=";")

# for row in reader:
# csvlist[row["fieldName"]] = row["Name"]
# maplist[row["SOURCE"]] = row["DESTINATION"]
# print(csvlist["cModelName"])
# print(maplist["Подтип КЭ"])

# del maplist[""]

# print(maplist)

curdir = os.path.basename(sys.path[0])

outfile = ""
for (dirpath, dirnames, filenames) in walk("{}\\OUT\\".format(curdir)):
    # type: ignore
    outfile = os.path.join(dirpath, filenames[0])

df = pandas.read_csv(outfile, sep=r";", index_col=False, keep_default_na=False)

# Одиночные подстановки
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, "config.ini")
config = configparser.ConfigParser()
config.read(initfile)
ufk = config.get("kazna", "ufk")

# print("ufk = {}".format(ufk))

df["cCity"] = ""
df["cFKtofk"] = str(ufk)
df["cAdmin"] = 0

updated = df["cMaterial"] == ""
df.loc[updated, "cMaterial"] = "Не присвоен матответственный"

# Преобразования
updated = df["cStatus"] == "На складе"
df.loc[updated, "cStore"] = "FKIndefined_для миграции"

updated = df["cCiSubType"] == "WiFi роутер"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Видеопанель"
df.loc[updated, "cNatureName"] = "Несетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "ИБП"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Интерактивная панель"
df.loc[updated, "cNatureName"] = "Несетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Колонки"
df.loc[updated, "cNatureName"] = "Несетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Коммутатор пользовательский"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Монитор"
df.loc[updated, "cNatureName"] = "Монитор"
updated = df["cCiSubType"] == "Моноблок"
df.loc[updated, "cNatureName"] = "Computer"
updated = df["cCiSubType"] == "Многофункциональное устройство (МФУ)"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Ноутбук"
df.loc[updated, "cNatureName"] = "Computer"
updated = df["cCiSubType"] == "Оборудование IP-телефонии"
df.loc[updated, "cNatureName"] = "Телефонный аппарат"
updated = df["cCiSubType"] == "Оборудование ВКС"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Переключатель КВМ"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Плазменная панель"
df.loc[updated, "cNatureName"] = "Несетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Планшетный компьютер"
df.loc[updated, "cNatureName"] = "Computer"
updated = df["cCiSubType"] == "Принтер"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Принт-сервер"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Проектор"
df.loc[updated, "cNatureName"] = "Несетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Системный блок"
df.loc[updated, "cNatureName"] = "Computer"
updated = df["cCiSubType"] == "Сканер"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"
updated = df["cCiSubType"] == "Факс"
df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"

updated = (
    (df["cNatureName"] != "Несетевое аппаратное обеспечение")
    & (df["cNatureName"] != "Сетевое аппаратное обеспечение")
    & (df["cNatureName"] != "Монитор")
    & (df["cNatureName"] != "Computer")
    & (df["cNatureName"] != "Телефонный аппарат")
)
df.loc[updated, "cNatureName"] = "Misc"

updated = df["cCiSubType"] == "WiFi роутер"
df.loc[updated, "cParentModelName"] = "Wi-Fi роутер"
updated = df["cCiSubType"] == "Видеопанель"
df.loc[updated, "cParentModelName"] = "Видеопанель"
updated = df["cCiSubType"] == "ИБП"
df.loc[updated, "cParentModelName"] = "ИБП"
updated = df["cCiSubType"] == "Интерактивная панель"
df.loc[updated, "cParentModelName"] = "Интерактивная панель"
updated = df["cCiSubType"] == "Колонки"
df.loc[updated, "cParentModelName"] = "Колонки"
updated = df["cCiSubType"] == "Коммутатор пользовательский"
df.loc[updated, "cParentModelName"] = "Коммутатор пользовательский"
updated = df["cCiSubType"] == "Монитор"
df.loc[updated, "cParentModelName"] = "Монитор"
updated = df["cCiSubType"] == "Моноблок"
df.loc[updated, "cParentModelName"] = "Моноблок"
updated = df["cCiSubType"] == "МФУ"
df.loc[updated, "cParentModelName"] = "Многофункциональное устройство (МФУ)"
updated = df["cCiSubType"] == "Ноутбук"
df.loc[updated, "cParentModelName"] = "Ноутбук"
updated = df["cCiSubType"] == "Оборудование ВКС"
df.loc[updated, "cParentModelName"] = "Оборудование ВКС"
updated = df["cCiSubType"] == "Переключатель КВМ"
df.loc[updated, "cParentModelName"] = "KVM-перключатель"
updated = df["cCiSubType"] == "Плазменная панель"
df.loc[updated, "cParentModelName"] = "Плазменная панель"
updated = df["cCiSubType"] == "Планшетный компьютер"
df.loc[updated, "cParentModelName"] = "Планшетный компьютер"
updated = df["cCiSubType"] == "Принтер"
df.loc[updated, "cParentModelName"] = "Принтер"
updated = df["cCiSubType"] == "Принт-сервер"
df.loc[updated, "cParentModelName"] = "Принт-сервер"
updated = df["cCiSubType"] == "Проектор"
df.loc[updated, "cParentModelName"] = "Проектор"
updated = df["cCiSubType"] == "Системный блок"
df.loc[updated, "cParentModelName"] = "Системный блок"
updated = df["cCiSubType"] == "Сканер"
df.loc[updated, "cParentModelName"] = "Сканер"
updated = df["cCiSubType"] == "Факс"
df.loc[updated, "cParentModelName"] = "Факс"

updated = (
    (df["cParentModelName"] != "Wi-Fi роутер")
    & (df["cParentModelName"] != "Видеопанель")
    & (df["cParentModelName"] != "ИБП")
    & (df["cParentModelName"] != "Интерактивная панель")
    & (df["cParentModelName"] != "Колонки")
    & (df["cParentModelName"] != "Коммутатор пользовательский")
    & (df["cParentModelName"] != "Монитор")
    & (df["cParentModelName"] != "Моноблок")
    & (df["cParentModelName"] != "Многофункциональное устройство (МФУ)")
    & (df["cParentModelName"] != "Ноутбук")
    & (df["cParentModelName"] != "Оборудование ВКС")
    & (df["cParentModelName"] != "KVM-перключатель")
    & (df["cParentModelName"] != "Плазменная панель")
    & (df["cParentModelName"] != "Планшетный компьютер")
    & (df["cParentModelName"] != "Принтер")
    & (df["cParentModelName"] != "Принт-сервер")
    & (df["cParentModelName"] != "Проектор")
    & (df["cParentModelName"] != "Системный блок")
    & (df["cParentModelName"] != "Сканер")
    & (df["cParentModelName"] != "Факс")
)
df.loc[updated, "cParentModelName"] = "Misc"

updated = df["cUser"] == ""
df.loc[updated, "cUser"] = "Не присвоен Юзер"

df.to_csv(outfile, sep=";", index=False, quoting=csv.QUOTE_NONE)

# df.rename(columns=maplist, inplace=True)
# df.to_csv(outfile, sep=";", index=False)

# list to store the names of columns
# list_of_column_names = []

# print("List of column names : ".format(list_of_column_names[0]))

# Одиночные значения


# df["cFKtofk"] = "99"  # Код ТоФК ПРОСТАВИТЬ!
# df["cUser"] = 0
#     # df["bUseCupboard"] = 1
#     # df["Activated"] = 1
# df["cCity"] = ""
# df["PartNo"] = df["cFKPartNumber"]
# df["cLocation"] = df["cLocation"]
# df["iLoadNum"] = 035
# df["cGarSupplier"] = ##
# Обработчики

# np.logical_or("Коммутатор управляемый (L3)",
#                         "Коммутатор (L2)",
#                         "Балансировщик нагрузки",
#     and (df["cParentModelName"] != "Маршрутизатор")
#     and (df["cParentModelName"] != "")
# )

#     if "admin" in list_of_column_names[0]:
#         updated = df["admin"] == ""
#         df.loc[updated, "cAdmin"] = "Куратор не присвоен"

#     if "cStatus" in list_of_column_names[0]:
#         updated = df["cStatus"] != "На складе"
#         df.loc[updated, "cStore"] = "0"
#         updated = df["cStatus"] == "На складе"
#         df.loc[updated, "cStore"] = "FKIndefined_для миграции"

#     # print(list_of_column_names[0][0])

#     if "cCiSubType" in list_of_column_names[0]:
#         updated = df["cCiSubType"] == ""
#         df.loc[updated, "cNatureName"] = ""
#         updated = df["cCiSubType"] != ""
#         df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"

# print(df["cLocation"])

# if "cNatureName" in list_of_column_names[0]:
