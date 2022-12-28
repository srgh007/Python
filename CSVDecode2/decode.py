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
with open("CSVDecode2\\citmapping.csv", encoding="UTF8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")

    for row in reader:
        # csvlist[row["fieldName"]] = row["Name"]
        maplist[row["SOURCE"]] = row["DESTINATION"]
    # print(csvlist["cModelName"])
    # print(maplist["Подтип КЭ"])

# del maplist[""]

print(maplist)

outfile = ""
for (dirpath, dirnames, filenames) in walk("E:\\Python\\CSVDecode2\\OUT"):
    outfile = os.path.join(dirpath, filenames[0])

df = pandas.read_csv(outfile, sep=r";", index_col=False)

df.rename(columns=maplist, inplace=True)
df.to_csv(outfile, sep=";", index=False)
