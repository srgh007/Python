import csv
import fileinput
import locale
import os
import sys
from os import walk

import pandas
from openpyxl import load_workbook

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")
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

outfile = ""
for (dirpath, dirnames, filenames) in walk("E:\\Python\\CSVDecode\\IN"):
    print(filenames)
    for file in filenames:
        if "xls" in file:
            outfile = os.path.join(dirpath, file)
            print(outfile)

wb_form = load_workbook(filename=outfile)
wb_val = load_workbook(filename=outfile, data_only=True)

sheet_val = wb_val["Тело"]

cell_vals = sheet_val["{}4".format(chr(65))].value
print(cell_vals)

# listprms = []


def listOfparams():
    listprms = []
    for i in range(65, 90):
        listprms.append(sheet_val["{}4".format(chr(i))].value)

    for g in range(65, 66):
        for i in range(65, 90):
            if sheet_val["{}{}4".format(chr(g), chr(i))].value != None:
                listprms.append(sheet_val["A{}4".format(chr(i))].value)
            else:
                return listprms

    # for i in range(65, 90):
    #     if sheet_val["B{}4".format(chr(i))].value != None:
    #         listprms.append(sheet_val["A{}4".format(chr(i))].value)
    #     else:
    #         return listprms


# print(listOfparams()[0])

# type: ignore
csvlist = {}
maplist = {}
with open("CSVDecode\\mapping.csv", encoding="UTF8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")

    for row in reader:
        csvlist[row["fieldName"]] = row["Name"]
        maplist[row["integrName"]] = row["fieldName"]
    # print(csvlist["cModelName"])
    # print(maplist["Подтип КЭ"])

del maplist[""]

outfile = ""
for (dirpath, dirnames, filenames) in walk("E:\\Python\\CSVDecode\\OUT"):
    outfile = os.path.join(dirpath, filenames[0])

df = pandas.read_csv(outfile, sep=r";", index_col=False)

df.rename(columns=maplist, inplace=True)
df.to_csv(outfile, sep=";", index=False)
