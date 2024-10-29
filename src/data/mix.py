import csv
import json

def set_full_names(teatchers_json_file_name, names_club_json_file_name):
    with open(f"./data/names/json/{teatchers_json_file_name}.json", "r", encoding="utf-8") as f:
        full_name_data = json.load(f)

    with open(f"./data/club/json/{names_club_json_file_name}.json", "r", encoding="utf-8") as f:
        names_club_data = json.load(f)

    for i, name_club in enumerate(names_club_data):
        for full_name in full_name_data:
            if full_name[0].startswith(name_club[0]):
                names_club_data[i][0] = full_name[0]

    with open(f"./data/club/json/{names_club_json_file_name}.json", "w", encoding="utf-8") as json_file:
        json.dump(names_club_data, json_file, indent=4, ensure_ascii=False)
