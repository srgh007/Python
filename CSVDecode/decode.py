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
with open("CSVDecode\\mapping.csv", encoding="UTF8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")

    for row in reader:
        csvlist[row["fieldName"]] = row["Name"]
        maplist[row["integrName"]] = row["fieldName"]
    # print(csvlist["cModelName"])
    # print(maplist["Подтип КЭ"])

# f = []
out = ""
outfile = ""
for (dirpath, dirnames, filenames) in walk("E:\\Python\\CSVDecode\\OUT"):
    out = "{}\\{}".format(dirpath, filenames[0])
    out = os.path.join(dirpath, filenames[0])
    outfile = filenames[0]
    break

# tempFile = open(out, "w")
# line = fileinput.input(tempFile)[0]

# with open(out, "r") as file:
#     filedata = file.read()


# tempFile.write(line.replace(maps, maplist[maps]))
# with fileinput.FileInput(out, inplace=True, backup=".bak") as file:
# for line in file:
# file[0].replace(maps, maplist[maps])


# with open(out, "w") as file:
#     file.write(filedata)

# file.close()


def replace_word(infile, old_word, new_word):
    if not os.path.isfile(infile):
        print("Error on replace_word, not a regular file: " + infile)
        sys.exit(1)

    f1 = open(infile, "r", encoding="UTF8").read()
    f2 = open(infile, "w", encoding="UTF8")
    m = f1.replace(old_word, new_word)
    if new_word != "" or old_word != "":
        f2.write(m)


df = pandas.read_csv(out, delimiter=";")

# print(df)

# print(maps)
# print(maplist[maps])
# if maps == "":
del maplist[""]

# print(maplist)


# replace_word(out, maps, maplist[maps])
# df.rename(
#     columns=maplist,
#     inplace=True,
# )
# df.to_csv(sep=";")
# type: ignore

# df.set_index('Custom field (Verified Date)').to_csv(out, index=None)


# def rename_column(old_col_name, new_col_name, optional_file=True):
outfile = ""
for (dirpath, dirnames, filenames) in walk("E:\\Python\\CSVDecode\\OUT"):
    outfile = os.path.join(dirpath, filenames[0])

df = pandas.read_csv(outfile, sep=r";", index_col=False)


# for maps in maplist:
df.rename(columns=maplist, inplace=True)
df.to_csv(outfile, sep=";", index=False)

# rename_column(outfile, , )
