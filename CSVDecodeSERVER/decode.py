import csv
import fileinput
import locale
import os
import sys
from os import walk

import pandas

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
with open("CSVDecodeSERVER\\citmapping.csv", encoding="UTF8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")

    for row in reader:
        # csvlist[row["fieldName"]] = row["Name"]
        maplist[row["SOURCE"]] = row["DESTINATION"]
    # print(csvlist["cModelName"])
    # print(maplist["Подтип КЭ"])

# del maplist[""]

# print(maplist)

outfile = ""
for (dirpath, dirnames, filenames) in walk("E:\\Python\\CSVDecodeSERVER\\OUT"):
    outfile = os.path.join(dirpath, filenames[0])

df = pandas.read_csv(outfile, sep=r";", index_col=False, keep_default_na=False)

df.rename(columns=maplist, inplace=True)
df.to_csv(outfile, sep=";", index=False)

# list to store the names of columns
list_of_column_names = []

with open(outfile, encoding="UTF8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    # loop to iterate through the rows of csv
    for row in csv_reader:
        # adding the first row
        list_of_column_names.append(row)
        # breaking the loop after the
        # first iteration itself
        break
    # printing the result
    print("List of column names : ", list_of_column_names[0])

    # Одиночные значения
    df["cFKtofk"] = 99
    df["cUser"] = 0
    df["bUseCupboard"] = 1
    df["Activated"] = 1
    df["cCity"] = ""
    df["iLoadNum"] = 999
    # df["cGarSupplier"] = ##
    # Обработчики
    updated = df["cCiSubType"] == "Сервер x86"
    df.loc[updated, "cParentModelName"] = "Сервер х86"
    updated = df["cCiSubType"] == "Сервер х86"
    df.loc[updated, "cParentModelName"] = "Сервер х86"
    updated = df["cCiSubType"] == "Серверное шасси"
    df.loc[updated, "cParentModelName"] = "Серверное шасси"
    updated = df["cCiSubType"] == "Консоль (KVM)"
    df.loc[updated, "cParentModelName"] = "Серверная консоль"
    updated = df["cCiSubType"] == "IBM Series P"
    df.loc[updated, "cParentModelName"] = "Сервер RISC"
    updated = df["cParentModelName"] == ""
    df.loc[updated, "cParentModelName"] = "Сервер RISC"

    if "admin" in list_of_column_names[0]:
        updated = df["admin"] == ""
        df.loc[updated, "cAdmin"] = "Куратор не присвоен"

    if "cStatus" in list_of_column_names[0]:
        updated = df["cStatus"] != "На складе"
        df.loc[updated, "cStore"] = "0"
        updated = df["cStatus"] == "На складе"
        df.loc[updated, "cStore"] = "FKIndefined_для миграции"

    # print(list_of_column_names[0][0])

    if "cCiSubType" in list_of_column_names[0]:
        updated = df["cCiSubType"] != "Серверная консоль (KVM)"
        df.loc[updated, "cNatureName"] = "Computer"
        updated = df["cCiSubType"] == "Серверная консоль (KVM)"
        df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"

        # if "cNatureName" in list_of_column_names[0]:
df.to_csv(outfile, sep=";", index=False)

# updated = df["cCiSubType"] == "Сервер x86"
# df.loc[updated, "cNatureName"] = "Computer"

# df.to_csv(outfile, sep=";", index=False)

# Select case ['ci.subtype']
# case "Сервер х86"       res = "Computer"
# case "Серверное шасси"       res = "Computer"
# case "Серверная консоль (KVM)"       res = "Сетевое аппаратное обеспечение"
# case "IBM Power Systems (Series P)"       res = "Computer"
# case "Виртуальная машина"       res = "Computer"
# case "HP Superdome"       res= "Computer"
# case else       res = "Computer"End selectRetVal = res
