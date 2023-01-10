import csv
import fileinput
import locale
import os
import re
import sys
from os import walk

import numpy as np
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
with open("CSVDecodeLAN\\citmapping.csv", encoding="UTF8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")

    for row in reader:
        # csvlist[row["fieldName"]] = row["Name"]
        maplist[row["SOURCE"]] = row["DESTINATION"]
    # print(csvlist["cModelName"])
    # print(maplist["Подтип КЭ"])

# del maplist[""]

# print(maplist)

outfile = ""
for (dirpath, dirnames, filenames) in walk("E:\\Python\\CSVDecodeLAN\\OUT"):
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
    # print("List of column names : ".format(list_of_column_names[0]))

    # Одиночные значения
    df["cFKtofk"] = "99"  # Код ТоФК ПРОСТАВИТЬ!
    df["cUser"] = 0
    # df["bUseCupboard"] = 1
    # df["Activated"] = 1
    df["cCity"] = ""
    df["PartNo"] = df["cFKPartNumber"]
    # df["cLocation"] = df["cLocation"]
    # df["iLoadNum"] = 035
    # df["cGarSupplier"] = ##
    # Обработчики
    updated = df["cCiSubType"] == "Коммутатор управляемый (L3)"
    df.loc[updated, "cParentModelName"] = "Коммутатор управляемый (L3)"
    updated = df["cCiSubType"] == "Коммутатор (L2)"
    df.loc[updated, "cParentModelName"] = "Коммутатор (L2)"
    updated = df["cCiSubType"] == "Балансировщик нагрузки"
    df.loc[updated, "cParentModelName"] = "Балансировщик нагрузки"
    updated = df["cCiSubType"] == "Маршрутизатор (router)"
    df.loc[updated, "cParentModelName"] = "Маршрутизатор"
    updated = df["cCiSubType"] == ""
    df.loc[updated, "cParentModelName"] = ""
    updated = (
        (df["cCiSubType"] != "Коммутатор управляемый (L3)")
        & (df["cCiSubType"] != "Коммутатор (L2)")
        & (df["cCiSubType"] != "Балансировщик нагрузки")
        & (df["cCiSubType"] != "Маршрутизатор")
        & (df["cCiSubType"] != "")
    )
    df.loc[updated, "cParentModelName"] = "Misc"

    # np.logical_or("Коммутатор управляемый (L3)",
    #                         "Коммутатор (L2)",
    #                         "Балансировщик нагрузки",
    #     and (df["cParentModelName"] != "Маршрутизатор")
    #     and (df["cParentModelName"] != "")
    # )

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
        updated = df["cCiSubType"] == ""
        df.loc[updated, "cNatureName"] = ""
        updated = df["cCiSubType"] != ""
        df.loc[updated, "cNatureName"] = "Сетевое аппаратное обеспечение"


def repl(x):
    return x.replace(chr(171), chr(34)).replace(chr(187), chr(34))


df["cGarSupplier"] = df["cGarSupplier"].apply(repl)
df.to_csv(outfile, sep=";", index=False, quoting=csv.QUOTE_NONE)


# a = []
# for i in x:
#     if i == chr(171) or i == chr(187):
#         a.append("|")
#     else:
#         a.append(i)

# x = x.replace(chr(187), "")
# StrInfo = StrInfo.replace(chr(191), chr(172))
# StrInfo = StrInfo.replace(chr(172), chr(39))
# print("".join(a))
# return "".join(a)


# print(chr(187))
# print(chr(171))


# df["cGarSupplier2"] = df["cGarSupplier2"].apply(lambda x: x.replace("|", "\""))

# del df["cGarSupplier2"]

# print(df["cGarSupplier"])

# df.to_csv(outfile, sep=";", index=False,quoting=csv.QUOTE_NONE)
