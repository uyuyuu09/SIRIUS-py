import csv
import json

def names_convert(csv_file, json_file_name):
    with open(csv_file, "r", encoding="utf-8") as csv_file:
        data = csv.reader(csv_file)
        json_data = {}
        for row in data:
            name = row[0]
            read = row[1:]
            json_data[name] = read

    with open(f"./data/names/json/{json_file_name}.json", "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)
    return json_data