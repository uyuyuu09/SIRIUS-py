import csv
import json

def club_convert(csv_file, json_file_name):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        club_json = {}
        for row in reader:
            club_name = row[0]
            members = row[1:]
            club_json[club_name] = members

    with open(f"data/club/json/{json_file_name}.json", 'w', encoding='utf-8') as f:
        json.dump(club_json, f, indent=4, ensure_ascii=False)
    return club_json
