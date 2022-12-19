import csv
import locale

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
    print(csvlist["cModelName"])
    print(maplist["Подтип КЭ"])
