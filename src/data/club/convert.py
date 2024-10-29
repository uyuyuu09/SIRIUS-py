import csv
import json

def names_club(csv_path, json_file_name):
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        advisor_data = {}
        for row in reader:
            club_name = row[0]
            advisors = row[1:]

            for advisor in advisors:
                if advisor:
                    advisor = advisor.strip()
                    if advisor not in advisor_data:
                        advisor_data[advisor] = []
                    advisor_data[advisor].append(club_name)

    names_data = []
    for advisor, clubs in advisor_data.items():
        names_data.append([advisor, "・".join(clubs)])

    with open(f"./data/club/json/{json_file_name}.json", 'w', encoding='utf-8') as f:
        json.dump(names_data, f, indent=4, ensure_ascii=False)

def club_names(csv_path, json_file_name):
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        club_json = {}
        for row in reader:
            club_name = row[0]
            members = row[1:]
            club_json[club_name] = members

    with open(f"./data/club/json/{json_file_name}.json", 'w', encoding='utf-8') as json_file:
        json.dump(club_json, json_file, indent=4, ensure_ascii=False)
