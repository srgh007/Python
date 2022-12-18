import csv
import locale

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
