import csv
import json

def names_convert(csv_path, json_file_name):
    with open(csv_path, "r", encoding="utf-8") as csv_file:
        data = csv.reader(csv_file)
        names_data = []
        for row in data:
            name = row[0].strip()
            read = row[1].strip()
            if name in "　":
                name.replace("　", " ")
            if read in "　":
                read.replace("　", " ")
            names_data.append([name, read])

    with open(f"./data/names/json/{json_file_name}.json", "w", encoding="utf-8") as json_file:
        json.dump(names_data, json_file, indent=4, ensure_ascii=False)
